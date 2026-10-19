<?php
/**
 * Métallerie BDO - Traitement du formulaire de demande de devis.
 *
 * Fonctionne sur un hebergement mutualise standard (OVH, o2switch, Ionos...)
 * avec la fonction mail() de PHP. Aucune dependance, aucune base de donnees.
 *
 * Securite mise en oeuvre :
 *  - methode POST uniquement ;
 *  - champ piege (honeypot) contre les robots ;
 *  - limitation de debit par session (1 envoi / 60 s, 5 envois / heure) ;
 *  - validation et normalisation de chaque champ cote serveur
 *    (la validation HTML5 du navigateur est contournable) ;
 *  - neutralisation des retours a la ligne dans les en-tetes
 *    (protection contre l'injection d'en-tetes SMTP) ;
 *  - l'adresse du visiteur n'est jamais placee dans "From" (rejet SPF/DMARC
 *    garanti) mais dans "Reply-To", apres validation stricte.
 *
 * Retour : redirection vers contact.html?envoi=ok|erreur|invalide|attente
 */

declare(strict_types=1);

/* --------------------------------------------------------------------------
   Configuration
   -------------------------------------------------------------------------- */
const MAIL_TO      = 'contact@metallerie-bdo.fr';      // Destinataire des demandes
const MAIL_FROM    = 'site@metallerie-bdo.fr';         // Expediteur : DOIT etre sur le domaine du site
const SITE_NAME    = 'Métallerie BDO';
const RETURN_URL   = 'contact.html';
const MIN_INTERVAL = 60;    // Secondes minimum entre deux envois d'une meme session
const MAX_PER_HOUR = 5;     // Envois maximum par session et par heure

/* --------------------------------------------------------------------------
   Fonctions utilitaires
   -------------------------------------------------------------------------- */

/** Redirige vers la page de contact avec un code de statut, puis termine. */
function redirect_with(string $status): never
{
    header('Location: ' . RETURN_URL . '?envoi=' . rawurlencode($status) . '#devis', true, 303);
    exit;
}

/**
 * Lit un champ texte POST, supprime les caracteres de controle et tronque.
 * Les retours a la ligne sont conserves uniquement si $multiline vaut true.
 */
function field(string $name, int $maxLength, bool $multiline = false): string
{
    $value = $_POST[$name] ?? '';
    if (!is_string($value)) {
        return '';
    }
    $value = trim($value);

    $value = $multiline
        // Garde \n et \t, supprime les autres caracteres de controle
        ? preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $value)
        // Une seule ligne : tout caractere de controle est retire (anti-injection)
        : preg_replace('/[\x00-\x1F\x7F]/u', ' ', $value);

    // preg_replace renvoie null si la chaine n'est pas de l'UTF-8 valide
    if ($value === null) {
        return '';
    }
    return mb_substr($value, 0, $maxLength, 'UTF-8');
}

/** Encode un texte pour un en-tete de mail (RFC 2047). */
function header_encode(string $text): string
{
    return '=?UTF-8?B?' . base64_encode($text) . '?=';
}

/* --------------------------------------------------------------------------
   1. Controles d'acces
   -------------------------------------------------------------------------- */
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST', true, 405);
    exit('Méthode non autorisée.');
}

// Robot : le champ piege est rempli. On simule un succes pour ne pas
// lui indiquer qu'il a ete detecte.
if (field('site_web', 200) !== '') {
    redirect_with('ok');
}

/* --------------------------------------------------------------------------
   2. Limitation de debit (par session)
   -------------------------------------------------------------------------- */
session_start([
    'cookie_httponly' => true,
    'cookie_secure'   => !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off',
    'cookie_samesite' => 'Strict',
    'use_strict_mode' => true,
]);

$now  = time();
$hits = array_filter(
    $_SESSION['contact_hits'] ?? [],
    static fn ($t): bool => is_int($t) && $t > $now - 3600
);

if ($hits && max($hits) > $now - MIN_INTERVAL) {
    redirect_with('attente');
}
if (count($hits) >= MAX_PER_HOUR) {
    redirect_with('attente');
}

/* --------------------------------------------------------------------------
   3. Lecture et validation des champs
   -------------------------------------------------------------------------- */
$nom       = field('nom', 100);
$societe   = field('societe', 120);
$email     = field('email', 150);
$telephone = field('telephone', 20);
$profil    = field('profil', 80);
$ouvrage   = field('ouvrage', 80);
$commune   = field('commune', 100);
$message   = field('message', 5000, true);
$rgpd      = ($_POST['rgpd'] ?? '') === '1';

// Listes fermees : seules les valeurs proposees dans le formulaire sont acceptees
$profils = [
    'Particulier',
    "Professionnel (entreprise, architecte, maître d'œuvre)",
    'Collectivité ou organisme public',
    'Bailleur social',
];
$ouvrages = [
    'Garde-corps / rampe', 'Portail / portillon / clôture', 'Grille de défense',
    'Escalier', 'Balcon / passerelle', 'Marquise', 'Verrière / châssis acier',
    'Façade / bardage', 'Petite charpente / structure',
    'Agencement (pare-douche, mobilier)', 'Restauration de ferronnerie', 'Autre',
];

$errors = [];
if (mb_strlen($nom) < 2)                                   { $errors[] = 'nom'; }
if (filter_var($email, FILTER_VALIDATE_EMAIL) === false)   { $errors[] = 'email'; }
if (!preg_match('/^[0-9 +().\-]{10,20}$/', $telephone))    { $errors[] = 'telephone'; }
if (!in_array($profil, $profils, true))                    { $errors[] = 'profil'; }
if (!in_array($ouvrage, $ouvrages, true))                  { $errors[] = 'ouvrage'; }
if (mb_strlen($commune) < 2)                               { $errors[] = 'commune'; }
if (mb_strlen($message) < 20)                              { $errors[] = 'message'; }
if (!$rgpd)                                                { $errors[] = 'rgpd'; }

// Heuristique anti-spam : plus de 3 liens dans le message
if (preg_match_all('#https?://#i', $message) > 3)          { $errors[] = 'message'; }

if ($errors) {
    redirect_with('invalide');
}

/* --------------------------------------------------------------------------
   4. Construction et envoi du mail
   -------------------------------------------------------------------------- */
$subject = sprintf('[Site web] Demande de devis — %s — %s', $ouvrage, $commune);

$body = implode("\n", [
    'Nouvelle demande de devis reçue depuis le site internet.',
    '',
    '--- Contact ---',
    'Nom       : ' . $nom,
    'Société   : ' . ($societe !== '' ? $societe : '-'),
    'E-mail    : ' . $email,
    'Téléphone : ' . $telephone,
    'Profil    : ' . $profil,
    '',
    '--- Projet ---',
    'Ouvrage   : ' . $ouvrage,
    'Commune   : ' . $commune,
    '',
    $message,
    '',
    '---',
    'Envoyé le ' . date('d/m/Y à H:i'),
    'Consentement RGPD : oui',
    'Répondez directement à ce message pour écrire au demandeur.',
]);

$headers = [
    'From'                      => header_encode(SITE_NAME . ' - Site web') . ' <' . MAIL_FROM . '>',
    'Reply-To'                  => header_encode($nom) . ' <' . $email . '>',
    'MIME-Version'              => '1.0',
    'Content-Type'              => 'text/plain; charset=UTF-8',
    'Content-Transfer-Encoding' => '8bit',
    'X-Mailer'                  => 'metallerie-bdo-site',
];

// Le 5e parametre (-f) fixe l'enveloppe d'expedition (Return-Path) :
// indispensable pour passer SPF sur la plupart des mutualises.
$sent = mail(MAIL_TO, header_encode($subject), $body, $headers, '-f' . MAIL_FROM);

if (!$sent) {
    error_log('[contact.php] Echec de mail() pour une demande de ' . $email);
    redirect_with('erreur');
}

$hits[] = $now;
$_SESSION['contact_hits'] = array_values($hits);

redirect_with('ok');
