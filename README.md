# Site internet — Métallerie BDO

Site vitrine de **Métallerie BDO**, atelier de métallerie, serrurerie d'art et dépannage à Marcilly-d'Azergues (69).
Il remplace le site actuel réalisé par Local.fr sur le domaine `metallerie-bdo.fr`.

Aperçu : <https://alexisbouchet6-del.github.io/metallerie-bdo-site/>

## Pages

| Page | Fichier | Contenu |
|---|---|---|
| Accueil | `index.html` | Bannière, références clients, 8 savoir-faire, domaines d'intervention, entreprise et chiffres clés, méthode, réalisations, zone d'intervention |
| Nos activités | `activites.html` | Détail des ouvrages : métallerie, serrurerie d'art, monuments historiques, marchés publics, dépannage, métaux, méthode |
| Réalisations | `realisations.html` | Projet à la une et galerie filtrable |
| Contact | `contact.html` + `contact.php` | Formulaire de devis, coordonnées, candidature spontanée |
| Mentions légales | `mentions-legales.html` | Éditeur, hébergeur, médiation, RGPD, cookies |
| Erreur 404 | `404.html` | Page d'erreur |

## Charte graphique

Reprise à l'identique du site historique et de la signature e-mail de l'entreprise.

| Rôle | Couleur | Origine |
|---|---|---|
| Bleu marine (fonds sombres, boutons) | `#020242` | Site historique |
| Bleu secondaire (bandeaux) | `#26356A` | Site historique |
| Bleu du logo (accents, pictogrammes) | `#284FA0` | Logo officiel |
| Bleu des liens | `#0563C1` | Signature e-mail |
| Police | Montserrat | Site historique (hébergée localement, licence OFL) |

Les couleurs sont définies une seule fois en tête de `assets/css/style.css` (variables `--navy`, `--navy-2`, `--brand`, `--link`).

## Choix techniques

- **HTML/CSS/JS sans framework ni CMS** : pas de mises à jour de sécurité à suivre, pas de base de données, chargement immédiat.
- **Aucune ressource tierce** (polices, statistiques, cartes) : aucune donnée de visiteur ne part chez un tiers, donc aucun bandeau cookies.
- **Aucun style ni script inline** : permet une Content-Security-Policy stricte (`.htaccess`).
- **Consultable sans JavaScript** : le JS n'apporte que le menu mobile, les filtres de galerie et le confort d'usage.
- **Données structurées Schema.org** pour le référencement local.
- **Redirections 301** des anciennes URL Local.fr.

## Modifier le site : le générateur

Les pages HTML sont **générées** par un script Python, pour que l'en-tête, le pied de page, les coordonnées et les pictogrammes ne soient écrits qu'une fois.

```bash
# Modifier les textes dans tools/build/build.py
# ou les éléments communs (téléphone, menu, pied de page) dans tools/build/parts.py, puis :
python tools/build/build.py
```

Ne modifiez pas les fichiers `.html` à la main : ils seraient écrasés à la génération suivante. Seuls `assets/css/style.css`, `assets/js/main.js` et `contact.php` se modifient directement.

Prérequis : Python 3.12 ou supérieur, aucune dépendance.

## Images à fournir

| Fichier | Où | Format conseillé |
|---|---|---|
| Logo officiel | remplace le logo texte `brand()` dans `tools/build/parts.py` | SVG, ou PNG transparent ≥ 600 px de large |
| `assets/img/hero.jpg` | fond de la bannière d'accueil, puis ajouter la classe `hero--photo` à la section `.hero` | JPG 1920×1080, ≤ 300 Ko |
| `assets/img/realisations/*.webp` | galerie (13 photos, noms dans `tools/fetch-images.ps1`) | WebP ou JPG 1200 px |
| Photos atelier, serrurerie, dépannage | blocs « Photo à venir » | JPG 1200×900 |

Les photos de l'ancien site peuvent être récupérées automatiquement :

```powershell
.\tools\fetch-images.ps1      # Windows
./tools/fetch-images.sh       # Linux / macOS
```

Tant qu'une photo manque, son cadre affiche « Photo à venir » au lieu d'une image cassée.

## Test en local

```bash
php -S localhost:8000
```

Le formulaire s'exécute mais l'envoi échoue en local faute de serveur mail : c'est attendu.

## Mise en ligne (hébergement OVH)

1. Vérifier `MAIL_TO` et `MAIL_FROM` en tête de `contact.php`.
2. Transférer par FTP le contenu du dépôt à la racine web (`www/`), **sans** `tools/` ni `README.md`.
3. Activer le certificat HTTPS (Let's Encrypt), puis décommenter `Strict-Transport-Security` dans `.htaccess`.
4. Déclarer `https://www.metallerie-bdo.fr/sitemap.xml` dans Google Search Console.
5. Envoyer un message de test depuis le formulaire.

GitHub Pages sert uniquement d'aperçu : le PHP n'y est pas exécuté, le formulaire n'y fonctionne donc pas.

## À valider avec l'entreprise

| Point | Pourquoi |
|---|---|
| **Médiateur de la consommation** | Obligation légale dès qu'il y a des clients particuliers (art. L612-1 Code de la consommation). Vide sur le site actuel. |
| **Mention « Damour.Odin »** | Le logo du site actuel indique « Damour.Odin », la signature e-mail « Baur.Damour.Odin ». Le site reprend le logo officiel. |
| **Labels et qualifications** | Qualibat, adhésion au GMH (monuments historiques), assurance décennale : les concurrents les mettent en avant. À ajouter s'ils existent. |
| **Bloc recrutement** | Ajouté sur la page Contact sur le modèle des concurrents. À retirer si l'entreprise ne recrute pas. |
| **Horaires d'ouverture** | Non publiés sur le site actuel ; à ajouter dans la barre du haut et les données Schema.org. |
| **Logos des partenaires** | Affichés en texte : l'usage des logos (HCL, Métropole, Ville de Lyon…) demande leur accord. |
| **Textes** | Rédigés à partir du site actuel ; à faire relire par les gérants. |

## Arborescence

```
├── index.html, activites.html, realisations.html, contact.html, mentions-legales.html, 404.html
├── contact.php          ← traitement du formulaire
├── .htaccess            ← HTTPS, redirections, en-têtes de sécurité, cache
├── robots.txt, sitemap.xml
├── assets/
│   ├── css/style.css
│   ├── js/main.js
│   ├── fonts/           ← Montserrat + licence OFL
│   └── img/             ← favicon, photos
└── tools/               ← non déployé
    ├── build/           ← générateur des pages HTML
    └── fetch-images.*   ← récupération des photos de l'ancien site
```

## Droits

Contenus, textes et photographies : © METALLERIE BDO, tous droits réservés.
Police Montserrat : SIL Open Font License 1.1 (`assets/fonts/OFL.txt`).
