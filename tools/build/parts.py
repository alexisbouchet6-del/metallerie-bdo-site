"""Elements partages : coordonnees, pictogrammes SVG, en-tete, pied de page."""

PHONE_TXT = "04 78 43 01 16"
PHONE_TEL = "+33478430116"
EMAIL = "contact@metallerie-bdo.fr"
ADDR_1 = "243 chemin des Ronzières"
ADDR_2 = "69380 Marcilly-d'Azergues"
FB = "https://www.facebook.com/metallerie69"
IG = "https://www.instagram.com/metallerie_b.d.o/"
LEGAL = "Métallerie BDO — SAS au capital de 52 500 € — RCS Lyon 853 435 667"

# Pictogrammes au trait (24x24, couleur heritee via currentColor)
_P = {
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.5 2.7.6a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "check": '<path d="M20 6L9 17l-5-5"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "award": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14.2L7 22l5-3 5 3-1.5-7.8"/>',
    "factory": '<path d="M2 21V9l6 4V9l6 4V5h6v16z"/><path d="M2 21h20"/>',
    "ruler": '<path d="M3 17L17 3l4 4L7 21z"/><path d="M7 13l2 2M10 10l2 2M13 7l2 2"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "stairs": '<path d="M3 21h4v-4h4v-4h4V9h4V5h2"/><path d="M3 21h18"/>',
    "railing": '<path d="M3 7h18M3 21h18M3 7v14M21 7v14M7.5 7v14M12 7v14M16.5 7v14"/>',
    "gate": '<path d="M3 21V7l4.5-3L12 7l4.5-3L21 7v14M3 21h18M7.5 4v17M12 7v14M16.5 4v17M3 12h18"/>',
    "window": '<rect x="3" y="3" width="18" height="18" rx="1"/><path d="M12 3v18M3 12h18M7.5 3v18M16.5 3v18"/>',
    "canopy": '<path d="M3 10h18l-2.5-5h-13z"/><path d="M6 10v11M18 10v11M4 21h4M16 21h4"/>',
    "facade": '<path d="M4 21V4h16v17M2 21h20"/><path d="M8 8h2M14 8h2M8 12h2M14 12h2M8 16h2M14 16h2"/>',
    "truss": '<path d="M2 18h20M2 18L12 6l10 12M7 18l5-6 5 6M12 6v12"/>',
    "bridge": '<path d="M2 13h20M3 13v6M21 13v6M7.5 13v6M12 13v6M16.5 13v6M2 9c4.5 3 15.5 3 20 0"/>',
    "column": '<path d="M3 21h18M4 18h16M12 3l8 3H4z"/><path d="M6 9h12M7 9v9M12 9v9M17 9v9"/>',
    "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>',
    "frame": '<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M5 9h14M12 9v12"/>',
    "fence": '<path d="M4 20V7l2-3 2 3v13M10 20V7l2-3 2 3v13M16 20V7l2-3 2 3v13M2 10h20M2 16h20"/>',
    "grid": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M8 3v18M12 3v18M16 3v18M4 9h16M4 15h16"/>',
    "balcony": '<path d="M6 4h12v7M3 11h18M3 11v9M21 11v9M3 20h18M7.5 11v9M12 11v9M16.5 11v9"/>',
    "lantern": '<path d="M9 3h6M12 3v2M7 8l2-3h6l2 3M7 8v9l2 3h6l2-3V8M7 8h10"/>',
    "spark": '<path d="M12 2v4M12 18v4M4.9 4.9l2.8 2.8M16.3 16.3l2.8 2.8M2 12h4M18 12h4M4.9 19.1l2.8-2.8M16.3 7.7l2.8-2.8"/>',
}
_FILLED = {
    "facebook": '<path d="M14 8.5V6.8c0-.8.2-1.3 1.4-1.3H17V2.2c-.3 0-1.3-.2-2.5-.2-2.5 0-4.2 1.5-4.2 4.3v2.2H7.5V12h2.8v10H14V12h2.8l.4-3.5H14z"/>',
    "instagram": '<path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 3.9 2.4 7.2 2.3 8.4 2.2 8.8 2.2 12 2.2zm0 4.9a4.9 4.9 0 1 0 0 9.8 4.9 4.9 0 0 0 0-9.8zm0 8.1a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zm5.1-9.4a1.2 1.2 0 1 0 0 2.3 1.2 1.2 0 0 0 0-2.3z"/>',
}


def icon(name: str) -> str:
    """Retourne le SVG inline d'un pictogramme (decoratif : aria-hidden)."""
    if name in _FILLED:
        return f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false">{_FILLED[name]}</svg>'
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{_P[name]}</svg>')


# Monogramme provisoire, a remplacer par le logo officiel (voir README)
MARK = ('<svg class="brand__mark" viewBox="0 0 48 48" aria-hidden="true" focusable="false">'
        '<rect width="48" height="48" rx="11" fill="#284FA0"/>'
        '<rect x="4" y="4" width="40" height="40" rx="8" fill="none" stroke="#fff" stroke-opacity=".35"/>'
        '<text x="24" y="29.5" text-anchor="middle" font-family="Montserrat, Arial, sans-serif" '
        'font-weight="700" font-size="14" letter-spacing=".6" fill="#fff">BDO</text></svg>')


def brand(light: bool = False) -> str:
    cls = "brand brand--light" if light else "brand"
    return (f'<a class="{cls}" href="index.html" aria-label="Métallerie B.D.O — accueil">{MARK}'
            '<span class="brand__text"><span class="brand__name">Métallerie B.D.O</span>'
            '<span class="brand__sub">Damour.Odin</span></span></a>')


NAV = [("index.html", "Accueil"), ("activites.html", "Nos activités"),
       ("realisations.html", "Réalisations"), ("contact.html", "Contact")]


def head(title: str, desc: str, path: str, extra: str = "", robots: str = "index, follow") -> str:
    url = "https://www.metallerie-bdo.fr/" + ("" if path == "index.html" else path)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#020242">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Métallerie BDO">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/montserrat-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/montserrat-bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">{extra}
</head>
<body>
<a class="skip-link" href="#main">Aller au contenu principal</a>
"""


def header(current: str) -> str:
    links = "\n".join(
        f'          <li><a class="nav__link" href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a></li>'
        for h, t in NAV)
    return f"""
<div class="topbar">
  <div class="wrap topbar__inner">
    <ul class="topbar__list">
      <li>{icon("phone")}<a href="tel:{PHONE_TEL}">{PHONE_TXT}</a></li>
      <li class="topbar__hide-sm">{icon("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li class="topbar__hide-sm">{icon("pin")}<span>Atelier à Marcilly-d'Azergues · Lyon, Rhône et Beaujolais</span></li>
    </ul>
    <div class="topbar__social">
      <a href="{FB}" rel="noopener noreferrer" target="_blank" aria-label="Facebook">{icon("facebook")}</a>
      <a href="{IG}" rel="noopener noreferrer" target="_blank" aria-label="Instagram">{icon("instagram")}</a>
    </div>
  </div>
</div>

<header class="header" data-header>
  <div class="wrap header__inner">
    {brand()}
    <button class="burger" type="button" data-burger aria-expanded="false" aria-controls="site-nav" aria-label="Ouvrir le menu">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="site-nav" data-nav data-open="false" aria-label="Navigation principale">
      <ul class="nav__links">
{links}
      </ul>
      <a class="btn btn--primary nav__cta" href="contact.html">Demander un devis</a>
    </nav>
  </div>
</header>
"""


def page_hero(eyebrow: str, h1: str, lead: str, crumb: str) -> str:
    return f"""
  <section class="page-hero">
    <div class="wrap page-hero__inner">
      <nav aria-label="Fil d'Ariane">
        <ol class="breadcrumb"><li><a href="index.html">Accueil</a></li><li aria-current="page">{crumb}</li></ol>
      </nav>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p>{lead}</p>
    </div>
  </section>
"""


def cta(title: str, text: str) -> str:
    return f"""
  <section class="cta">
    <div class="wrap cta__inner">
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--light" href="contact.html">Demander un devis {icon("arrow")}</a>
        <a class="btn btn--outline" href="tel:{PHONE_TEL}">{icon("phone")} {PHONE_TXT}</a>
      </div>
    </div>
  </section>
"""


def footer() -> str:
    return f"""
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__about">
        {brand(light=True)}
        <p>Métallerie, serrurerie d'art et restauration d'ouvrages métalliques. Fabrication et pose dans le Rhône et la métropole lyonnaise.</p>
        <div class="footer__social">
          <a href="{FB}" rel="noopener noreferrer" target="_blank" aria-label="Facebook">{icon("facebook")}</a>
          <a href="{IG}" rel="noopener noreferrer" target="_blank" aria-label="Instagram">{icon("instagram")}</a>
        </div>
      </div>
      <div>
        <h4>Navigation</h4>
        <ul>
          <li><a href="index.html">Accueil</a></li>
          <li><a href="activites.html">Nos activités</a></li>
          <li><a href="realisations.html">Réalisations</a></li>
          <li><a href="contact.html">Contact et devis</a></li>
        </ul>
      </div>
      <div>
        <h4>Activités</h4>
        <ul>
          <li><a href="activites.html#ouvrages">Métallerie</a></li>
          <li><a href="activites.html#serrurerie">Serrurerie d'art</a></li>
          <li><a href="activites.html#patrimoine">Monuments historiques</a></li>
          <li><a href="activites.html#publics">Marchés publics</a></li>
          <li><a href="activites.html#depannage">Dépannage</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><address>{ADDR_1}<br>{ADDR_2}</address></li>
          <li><a href="tel:{PHONE_TEL}">{PHONE_TXT}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span data-year>2026</span> {LEGAL}</span>
      <a href="mentions-legales.html">Mentions légales et données personnelles</a>
    </div>
  </div>
</footer>

<script src="assets/js/main.js" defer></script>
</body>
</html>
"""
