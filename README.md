# Site internet — Métallerie BDO

Site vitrine de **Métallerie BDO**, atelier de métallerie et de serrurerie d'art à Marcilly-d'Azergues (69).
Il remplace le site actuel hébergé par Local.fr sur le domaine `metallerie-bdo.fr`.

## Contenu

| Page | Fichier | Rôle |
|---|---|---|
| Accueil | `index.html` | Présentation, savoir-faire, clientèles, points forts, partenaires |
| Nos activités | `activites.html` | Énumération détaillée des ouvrages par domaine, métaux, méthode de travail |
| Réalisations | `realisations.html` | Galerie photo |
| Contact | `contact.html` + `contact.php` | Formulaire de demande de devis, coordonnées |
| Mentions légales | `mentions-legales.html` | Éditeur, hébergeur, médiation, RGPD, cookies |
| Erreur 404 | `404.html` | Page d'erreur, utile après la migration |

## Choix techniques

- **HTML/CSS/JS sans framework ni CMS.** Cinq pages statiques n'ont pas besoin d'un WordPress : pas de mises à jour de sécurité à suivre, pas de base de données, chargement immédiat, hébergement sur n'importe quel mutualisé.
- **Aucune ressource tierce** (pas de Google Fonts, pas de Google Analytics, pas de carte intégrée). Aucune donnée de visiteur ne part chez un tiers, donc aucun bandeau de consentement n'est nécessaire.
- **Aucun style ni script inline**, ce qui autorise une Content-Security-Policy stricte (voir `.htaccess`).
- **Site consultable sans JavaScript.** Le JS ne gère que le menu mobile, l'année du pied de page, le message de retour du formulaire et les photos manquantes.
- **Données structurées Schema.org** (`index.html`) pour le référencement local (fiche Google, adresse, téléphone).
- **Redirections 301** des anciennes URL Local.fr pour conserver le référencement acquis.

## Prérequis

- Hébergement Apache avec **PHP 8.1 ou supérieur** et la fonction `mail()` active (OVH Perso, o2switch, Ionos…).
- Une adresse e-mail sur le domaine pour l'expéditeur du formulaire (`site@metallerie-bdo.fr` par défaut).

## Récupération des photos

Les photos de l'ancien site sont stockées chez Local.fr et disparaîtront à la fin du contrat. Récupérez-les une fois pour toutes :

```powershell
# Windows (PowerShell)
cd metallerie-bdo-site
.\tools\fetch-images.ps1
```

```bash
# Linux / macOS
./tools/fetch-images.sh
```

Les fichiers sont placés dans `assets/img/realisations/`. Une photo manquante affiche un cadre neutre « Photo à venir » au lieu d'une image cassée.

Les emplacements `Photo d'atelier à insérer` (accueil) et `Photo de serrurerie à insérer` (activités) attendent des photos fournies par le client : remplacer le `<div class="placeholder">` par une balise `<img>`.

## Test en local

```bash
cd metallerie-bdo-site
php -S localhost:8000
```

Puis ouvrir <http://localhost:8000>. Le formulaire s'exécute, mais l'envoi échoue en local faute de serveur mail : c'est attendu (message « L'envoi a échoué »).

## Mise en ligne

1. Vérifier les constantes en tête de `contact.php` (`MAIL_TO`, `MAIL_FROM`).
2. Transférer par FTP/SFTP le contenu du dossier à la racine web (`www/` chez OVH), **sans** le dossier `tools/` ni ce `README.md`.
3. Activer le certificat HTTPS (Let's Encrypt, gratuit chez OVH et o2switch).
4. Une fois le HTTPS vérifié, décommenter la ligne `Strict-Transport-Security` dans `.htaccess`.
5. Déclarer `https://www.metallerie-bdo.fr/sitemap.xml` dans Google Search Console.
6. Envoyer un message de test depuis le formulaire et vérifier sa réception (y compris dans les indésirables).

## À compléter avant mise en ligne

| Élément | Fichier | Pourquoi |
|---|---|---|
| Médiateur de la consommation | `mentions-legales.html` §3 | **Obligation légale** dès qu'il y a des clients particuliers (art. L612-1 Code de la consommation). Rubrique vide sur le site actuel. |
| Hébergeur | `mentions-legales.html` §2 | OVH indiqué par défaut, à adapter à l'hébergeur retenu. |
| Assurance décennale | à ajouter dans `mentions-legales.html` | Mention de l'assureur et de la couverture géographique obligatoire sur les devis et factures (art. L243-2 Code des assurances) ; recommandée sur le site. |
| Photos d'atelier et de serrurerie | `index.html`, `activites.html` | Emplacements réservés. |
| Logos des partenaires | `index.html` | Affichés en texte : l'usage des logos (HCL, Métropole, Ville de Lyon…) nécessite leur accord. |
| Validation des textes | toutes les pages | Les descriptions d'ouvrages sont rédigées à partir du site actuel ; à faire relire par les gérants. |

## Arborescence

```
metallerie-bdo-site/
├── index.html
├── activites.html
├── realisations.html
├── contact.html
├── contact.php
├── mentions-legales.html
├── 404.html
├── robots.txt
├── sitemap.xml
├── .htaccess
├── .gitignore
├── assets/
│   ├── css/style.css
│   ├── js/main.js
│   └── img/
│       ├── favicon.svg
│       └── realisations/     ← photos récupérées par tools/fetch-images.*
└── tools/                    ← non déployé
    ├── fetch-images.ps1
    └── fetch-images.sh
```

## Droits

Contenus, textes et photographies : © METALLERIE BDO, tous droits réservés.
