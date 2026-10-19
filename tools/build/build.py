"""Genere les pages HTML statiques du site Metallerie BDO.

Usage (depuis la racine du depot) :
    python tools/build/build.py

Les coordonnees, le menu, l'en-tete, le pied de page et les pictogrammes sont
definis une seule fois dans parts.py. Modifier ces fichiers puis relancer le
script plutot que d'editer les .html a la main, sinon les modifications
seront ecrasees a la prochaine generation.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from parts import *  # noqa

# Racine du site : deux niveaux au-dessus de ce fichier (tools/build/ -> racine)
OUT = pathlib.Path(__file__).resolve().parents[2]

def write(name, html):
    (OUT / name).write_text(html, encoding="utf-8")
    print("ecrit", name, len(html))

ARROW = icon("arrow")

# ============================================================================
# ACCUEIL
# ============================================================================
JSONLD = f"""
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "name": "Métallerie BDO",
  "alternateName": "Métallerie B.D.O — Damour.Odin",
  "description": "Métallerie, serrurerie d'art et dépannage : fabrication et pose d'ouvrages en acier, aluminium, inox et laiton, en neuf comme en restauration de monuments historiques.",
  "url": "https://www.metallerie-bdo.fr/",
  "telephone": "{PHONE_TEL}",
  "email": "{EMAIL}",
  "vatID": "FR64853435667",
  "foundingDate": "2019",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{ADDR_1}",
    "postalCode": "69380",
    "addressLocality": "Marcilly-d'Azergues",
    "addressRegion": "Auvergne-Rhône-Alpes",
    "addressCountry": "FR"
  }},
  "areaServed": ["Lyon", "Métropole de Lyon", "Villefranche-sur-Saône", "Beaujolais", "Rhône"],
  "sameAs": ["{FB}", "{IG}"]
}}
</script>"""

SERVICES = [
    ("stairs",  "Escaliers et garde-corps", "Escaliers droits, tournants ou hélicoïdaux, rampes et garde-corps conformes aux normes de sécurité.", "ouvrages"),
    ("gate",    "Portails, clôtures et grilles", "Portails battants ou coulissants, clôtures, grilles de défense et barreaudages forgés sur mesure.", "serrurerie"),
    ("window",  "Verrières et châssis acier", "Verrières d'intérieur ou de toiture, châssis vitrés à profilés fins pour l'habitat et les locaux professionnels.", "ouvrages"),
    ("canopy",  "Marquises et balcons", "Auvents de protection et balcons rapportés en acier, aluminium ou inox, adaptés à votre façade.", "ouvrages"),
    ("truss",   "Structures et façades", "Petites charpentes, passerelles, habillages et façades métalliques, en neuf comme en réhabilitation.", "ouvrages"),
    ("column",  "Patrimoine et monuments", "Restauration de ferronneries anciennes et reproduction d'éléments décoratifs dans le respect de l'époque.", "patrimoine"),
    ("frame",   "Agencement sur mesure", "Pare-douches, cloisons vitrées, lanternes et mobilier métallique dessinés pour votre intérieur.", "ouvrages"),
    ("wrench",  "Dépannage et réparation", "Remise en état de portails, grilles, garde-corps et fermetures métalliques endommagés.", "depannage"),
]

def service_card(ic, t, d, anchor):
    return f"""        <a class="service" href="activites.html#{anchor}">
          <span class="icon-tile">{icon(ic)}</span>
          <h3>{t}</h3>
          <p>{d}</p>
          <span class="link-arrow">En savoir plus {ARROW}</span>
        </a>"""

CLIENTS = ["Hospices Civils de Lyon", "Métropole de Lyon", "Ville de Lyon", "Grand Lyon Habitat",
           "Lyon Métropole Habitat", "Rhône Habitat", "SDMIS"]

ZONES = ["Lyon et Métropole", "Villefranche-sur-Saône", "Beaujolais", "Val d'Azergues",
         "Monts d'Or", "Ouest lyonnais", "Val de Saône", "Rhône (69)"]

PROJECTS_HOME = [
    ("lanterne-1", "Lanterne acier et verre bombé", "Création et pose, finition thermolaquée", "Agencement"),
    ("escalier", "Escalier métallique sur mesure", "Secteur Villefranche-sur-Saône", "Escalier"),
    ("verriere", "Verrière en acier", "Fabrication et pose", "Verrière"),
]

def project_card(img, t, sub, tag, cat=None, href="realisations.html"):
    data = f' data-cat="{cat}"' if cat else ""
    if href is None:
        return f"""        <figure class="project"{data}>
          <div class="frame">
            <span class="project__tag">{tag}</span>
            <img data-photo src="assets/img/realisations/{img}.webp" alt="{t}" loading="lazy" width="600" height="450">
          </div>
          <figcaption><h3>{t}</h3><p>{sub}</p></figcaption>
        </figure>"""
    return f"""        <a class="project" href="{href}"{data}>
          <div class="frame">
            <span class="project__tag">{tag}</span>
            <img data-photo src="assets/img/realisations/{img}.webp" alt="{t}" loading="lazy" width="600" height="450">
          </div>
          <h3>{t}</h3>
          <p>{sub}</p>
        </a>"""

index = head(
    "Métallerie BDO — Métallerie et serrurerie d'art près de Lyon (69)",
    "Métallerie BDO, atelier de métallerie et serrurerie d'art à Marcilly-d'Azergues (69). Fabrication et pose d'ouvrages en acier, aluminium, inox et laiton : monuments historiques, marchés publics, particuliers.",
    "index.html", JSONLD) + header("index.html") + f"""
<main id="main">

  <section class="hero">
    <div class="wrap hero__inner">
      <span class="eyebrow">Métallerie · Serrurerie · Dépannage</span>
      <h1>L'ouvrage métallique sur mesure, <span>de l'atelier au chantier</span></h1>
      <p class="hero__lead">
        Depuis notre atelier de Marcilly-d'Azergues, nous concevons, fabriquons et posons
        des ouvrages en acier, aluminium, inox et laiton pour les collectivités,
        les monuments historiques et les particuliers de la région lyonnaise.
      </p>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html">Demander un devis {ARROW}</a>
        <a class="btn btn--outline" href="activites.html">Découvrir nos activités</a>
      </div>
      <ul class="proof">
        <li>{icon("award")} Plus de 30 ans d'expérience</li>
        <li>{icon("column")} Monuments historiques</li>
        <li>{icon("shield")} Marchés publics</li>
      </ul>
    </div>
  </section>

  <section class="clients" aria-label="Références">
    <div class="wrap clients__inner">
      <span class="clients__label">Ils nous font confiance</span>
      <ul class="clients__list">
{chr(10).join(f"        <li>{c}</li>" for c in CLIENTS)}
      </ul>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head section-head--center">
        <span class="eyebrow">Nos savoir-faire</span>
        <h2>Tous vos ouvrages métalliques, conçus et fabriqués par la même équipe</h2>
        <p class="lead">Du relevé sur site à la pose, en passant par la fabrication à l'atelier : un interlocuteur unique pour chaque projet.</p>
      </div>
      <div class="grid grid--4">
{chr(10).join(service_card(*s) for s in SERVICES)}
      </div>
    </div>
  </section>

  <section class="section section--navy">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Domaines d'intervention</span>
        <h2>Trois types de chantiers, une même exigence</h2>
        <p class="lead">Collectivités, propriétaires de bâtiments protégés ou particuliers : chaque maître d'ouvrage a ses contraintes, nous les connaissons.</p>
      </div>
      <div class="grid grid--3">
        <article class="domain">
          <span class="domain__num">01</span>
          <h3>Marchés publics</h3>
          <p>Des ouvrages robustes, conformes aux normes et pensés pour un usage intensif.</p>
          <ul>
            <li>{icon("check")} Passerelles métalliques</li>
            <li>{icon("check")} Garde-corps pour ERP</li>
            <li>{icon("check")} Clôtures et protections de site</li>
          </ul>
        </article>
        <article class="domain">
          <span class="domain__num">02</span>
          <h3>Monuments historiques</h3>
          <p>Restaurer et recréer sans dénaturer : conservation de la matière d'origine, reprise à l'identique.</p>
          <ul>
            <li>{icon("check")} Restauration de ferronneries</li>
            <li>{icon("check")} Éléments décoratifs d'époque</li>
            <li>{icon("check")} Réhabilitation de structures</li>
          </ul>
        </article>
        <article class="domain">
          <span class="domain__num">03</span>
          <h3>Particuliers</h3>
          <p>Des pièces uniques dessinées pour votre maison, avec visite et devis détaillé avant fabrication.</p>
          <ul>
            <li>{icon("check")} Verrières, marquises, balcons</li>
            <li>{icon("check")} Escaliers et garde-corps</li>
            <li>{icon("check")} Portails et agencement</li>
          </ul>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="media">
        <!-- Photo d'atelier a deposer : assets/img/atelier.jpg, puis remplacer ce bloc par une balise <img> -->
        <div class="placeholder">Photo de l'atelier à venir</div>
        <div class="media__badge"><strong>30+</strong><span>ans de<br>savoir-faire</span></div>
      </div>
      <div>
        <span class="eyebrow">L'entreprise</span>
        <h2>Un atelier repris par ceux qui y ont appris le métier</h2>
        <p>
          Métallerie BDO est dirigée par des professionnels du bâtiment qui ont racheté
          l'entreprise de leur premier patron. Cette continuité se retrouve dans la façon
          de travailler : chaque ouvrage est dessiné au cas par cas, fabriqué dans notre
          atelier du Val d'Azergues et posé par nos propres équipes.
        </p>
        <p>
          Nous intervenons aussi bien en construction neuve qu'en rénovation, y compris sur
          des édifices protégés, en associant les techniques de la ferronnerie traditionnelle
          aux exigences actuelles de sécurité et de durabilité.
        </p>
        <div class="stats">
          <div class="stat"><span class="stat__value">30+</span><span class="stat__label">années d'expérience</span></div>
          <div class="stat"><span class="stat__value">4</span><span class="stat__label">métaux travaillés</span></div>
          <div class="stat"><span class="stat__value">100&nbsp;%</span><span class="stat__label">fabrication sur mesure</span></div>
          <div class="stat"><span class="stat__value">7</span><span class="stat__label">donneurs d'ordre publics de référence</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--ice">
    <div class="wrap">
      <div class="section-head section-head--center">
        <span class="eyebrow">Notre méthode</span>
        <h2>Un projet mené de bout en bout</h2>
      </div>
      <ol class="steps">
        <li class="step"><h3>Échange et visite</h3><p>Vous nous décrivez le besoin ; nous venons relever les cotes et vérifier les contraintes de pose.</p></li>
        <li class="step"><h3>Devis et plans</h3><p>Proposition chiffrée détaillée : métal, finition, mode de fixation et délais.</p></li>
        <li class="step"><h3>Fabrication à l'atelier</h3><p>Débit, assemblage, soudure et traitement de surface réalisés par nos équipes.</p></li>
        <li class="step"><h3>Pose et réception</h3><p>Installation sur site, contrôle et réception de l'ouvrage avec vous.</p></li>
      </ol>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Réalisations</span>
        <h2>Quelques ouvrages sortis de notre atelier</h2>
      </div>
      <div class="grid grid--3">
{chr(10).join(project_card(*p) for p in PROJECTS_HOME)}
      </div>
      <div class="btn-row">
        <a class="btn btn--ghost" href="realisations.html">Voir toutes les réalisations {ARROW}</a>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="zone">
        <div class="split split--top">
          <div>
            <span class="eyebrow">Zone d'intervention</span>
            <h2>Lyon, le Rhône et le Beaujolais</h2>
            <p>Notre atelier est installé à Marcilly-d'Azergues, entre Lyon et Villefranche-sur-Saône. Pour un chantier hors de ces secteurs, consultez-nous.</p>
          </div>
          <ul class="zone__list">
{chr(10).join(f"            <li>{icon('pin')}{z}</li>" for z in ZONES)}
          </ul>
        </div>
      </div>
    </div>
  </section>
""" + cta("Un projet de métallerie ou de serrurerie ?",
          "Décrivez-nous votre besoin : nous revenons vers vous avec une proposition chiffrée et, si nécessaire, une visite sur place.") + """
</main>
""" + footer()
write("index.html", index)

# ============================================================================
# ACTIVITES
# ============================================================================
def work(ic, t, d):
    return f"""        <article class="work">
          <div class="work__head"><span class="icon-tile">{icon(ic)}</span><h3>{t}</h3></div>
          <p>{d}</p>
        </article>"""

OUVRAGES = [
    ("stairs", "Escaliers métalliques", "Droits, à quartier tournant ou hélicoïdaux, intérieurs ou extérieurs. Marches en tôle larmée, caillebotis, bois ou verre selon l'usage."),
    ("railing", "Garde-corps et rampes", "Pour balcons, terrasses, mezzanines et escaliers, conformes aux hauteurs et espacements réglementaires."),
    ("window", "Verrières", "Verrières d'intérieur pour cloisonner sans perdre la lumière, verrières de toiture ou de véranda à profilés fins."),
    ("frame", "Châssis et menuiseries acier", "Châssis vitrés, portes et cloisons en acier pour l'habitat comme pour les locaux professionnels."),
    ("canopy", "Marquises", "Auvents au-dessus d'une entrée, couverture vitrée ou pleine, dimensionnés pour la neige et le vent."),
    ("balcony", "Balcons", "Structures rapportées en acier galvanisé ou inox, fixation étudiée selon la nature du mur support."),
    ("facade", "Façades métalliques", "Habillages et bardages en acier, aluminium ou inox, traitement anticorrosion adapté à l'exposition."),
    ("truss", "Petites charpentes", "Ossatures secondaires, renforts, supports techniques, pergolas et abris métalliques."),
    ("lantern", "Lanternes et ouvrages cintrés", "Acier cintré associé au verre bombé, finition thermolaquée : des pièces de grande précision."),
    ("frame", "Pare-douches et agencement", "Pare-douches acier à vitrage clair ou sablé, séparations, étagères et mobilier métallique."),
]

act = head(
    "Nos activités — Métallerie, serrurerie, patrimoine et dépannage | Métallerie BDO",
    "Toutes les prestations de Métallerie BDO : escaliers, garde-corps, verrières, marquises, balcons, façades, portails, grilles, restauration de monuments historiques, marchés publics et dépannage.",
    "activites.html") + header("activites.html") + "\n<main id=\"main\">\n" + page_hero(
    "Nos activités",
    "Métallerie, serrurerie d'art, patrimoine et dépannage",
    "Nous travaillons l'acier, l'aluminium, l'inox et le laiton pour les particuliers, les collectivités et les monuments historiques. Voici le détail de ce que nous fabriquons et posons.",
    "Nos activités") + f"""
  <nav class="subnav" aria-label="Sommaire de la page">
    <div class="wrap">
      <ul>
        <li><a href="#ouvrages">Métallerie</a></li>
        <li><a href="#serrurerie">Serrurerie d'art</a></li>
        <li><a href="#patrimoine">Monuments historiques</a></li>
        <li><a href="#publics">Marchés publics</a></li>
        <li><a href="#depannage">Dépannage</a></li>
        <li><a href="#metaux">Métaux</a></li>
        <li><a href="#methode">Méthode</a></li>
      </ul>
    </div>
  </nav>

  <section class="section" id="ouvrages">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">01 — Métallerie</span>
        <h2>Fabrication et pose d'ouvrages sur mesure</h2>
        <p class="lead">Relevé sur site, plans d'exécution, fabrication à l'atelier, traitement de surface et pose : nous maîtrisons toute la chaîne.</p>
      </div>
      <div class="grid grid--2">
{chr(10).join(work(*w) for w in OUVRAGES)}
      </div>
    </div>
  </section>

  <section class="section section--ice" id="serrurerie">
    <div class="wrap split">
      <div>
        <span class="eyebrow">02 — Serrurerie d'art</span>
        <h2>Le travail du fer pour fermer et protéger</h2>
        <p>La serrurerie d'art prolonge la ferronnerie traditionnelle : chaque pièce est façonnée, assemblée et ajustée à son ouverture, avec une attention particulière aux détails et aux finitions.</p>
        <ul class="checks">
          <li>{icon("check")}<span><strong>Portails et portillons</strong> — battants ou coulissants, pleins ou ajourés.</span></li>
          <li>{icon("check")}<span><strong>Grilles de défense</strong> — protection des fenêtres et soupiraux, barreaudage droit ou ouvragé.</span></li>
          <li>{icon("check")}<span><strong>Garde-corps et rampes</strong> — alliance de sécurité et d'esthétique.</span></li>
          <li>{icon("check")}<span><strong>Clôtures et barreaudages</strong> — dans la continuité du style du bâtiment.</span></li>
          <li>{icon("check")}<span><strong>Grilles décoratives et impostes</strong> — création ou reproduction d'éléments ajourés.</span></li>
        </ul>
      </div>
      <div class="media">
        <!-- Photo de serrurerie a deposer : assets/img/serrurerie.jpg -->
        <div class="placeholder">Photo de serrurerie à venir</div>
      </div>
    </div>
  </section>

  <section class="section section--navy" id="patrimoine">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">03 — Monuments historiques</span>
        <h2>Intervenir sur le patrimoine sans le dénaturer</h2>
        <p class="lead">Relevé précis de l'existant, conservation maximale de la matière d'origine, reprise à l'identique de ce qui doit être remplacé : une méthode propre aux bâtiments protégés.</p>
      </div>
      <div class="grid grid--3">
        <article class="domain">
          <span class="domain__num">A</span>
          <h3>Restauration de ferronneries</h3>
          <p>Dépose, décapage, reprise des assemblages corrodés, remplacement partiel des éléments trop dégradés et remise en peinture.</p>
        </article>
        <article class="domain">
          <span class="domain__num">B</span>
          <h3>Éléments décoratifs</h3>
          <p>Grilles, balustrades et ornements recréés d'après un modèle, une archive ou un relevé, dans le style et les techniques de l'époque.</p>
        </article>
        <article class="domain">
          <span class="domain__num">C</span>
          <h3>Réhabilitation de structures</h3>
          <p>Renforcement et mise en sécurité de structures anciennes, en associant savoir-faire traditionnel et matériaux actuels.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section" id="publics">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">04 — Marchés publics</span>
        <h2>Des ouvrages dimensionnés pour l'usage collectif</h2>
        <p class="lead">Collectivités, bailleurs sociaux, établissements hospitaliers et services de secours nous confient des ouvrages soumis à une forte fréquentation.</p>
      </div>
      <div class="grid grid--3">
{work("bridge", "Passerelles métalliques", "Franchissements et cheminements techniques avec platelage antidérapant et garde-corps conformes, calculés pour les charges d'exploitation.")}
{work("railing", "Garde-corps aux normes", "Hauteurs, remplissages et espacements conformes à la réglementation des établissements recevant du public.")}
{work("fence", "Clôtures et protections", "Délimitation et sécurisation d'emprises, portails de service, protection d'équipements techniques.")}
      </div>
      <div class="recruit mt-lg">
        <div>
          <h3>Ils nous font confiance</h3>
          <p>Hospices Civils de Lyon, Métropole de Lyon, Ville de Lyon, Grand Lyon Habitat, Lyon Métropole Habitat, Rhône Habitat, SDMIS.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--ice" id="depannage">
    <div class="wrap split">
      <div>
        <span class="eyebrow">05 — Dépannage</span>
        <h2>Réparation et remise en état</h2>
        <p>Un portail qui ne ferme plus, une grille arrachée, un garde-corps descellé ? Nous intervenons pour réparer et sécuriser vos ouvrages métalliques existants, qu'ils soient de notre fabrication ou non.</p>
        <ul class="checks">
          <li>{icon("check")}<span>Réparation de portails, portillons et clôtures</span></li>
          <li>{icon("check")}<span>Remise en état de grilles et de garde-corps</span></li>
          <li>{icon("check")}<span>Reprise de soudures, de fixations et de scellements</span></li>
          <li>{icon("check")}<span>Remplacement de pièces et de fermetures métalliques</span></li>
        </ul>
        <div class="btn-row">
          <a class="btn btn--navy" href="tel:{PHONE_TEL}">{icon("phone")} Appeler l'atelier</a>
        </div>
      </div>
      <div class="media">
        <div class="placeholder">Photo d'intervention à venir</div>
      </div>
    </div>
  </section>

  <section class="section" id="metaux">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Matériaux</span>
        <h2>Quatre métaux, chacun pour son usage</h2>
      </div>
      <div class="grid grid--4">
        <article class="work metal"><div class="metal__swatch metal__swatch--acier"></div><h3>Acier</h3><p>Le plus polyvalent et le plus résistant. Protégé par galvanisation, métallisation ou thermolaquage.</p></article>
        <article class="work metal"><div class="metal__swatch metal__swatch--alu"></div><h3>Aluminium</h3><p>Léger et naturellement résistant à la corrosion : idéal pour les grandes pièces et les ouvrages rapportés.</p></article>
        <article class="work metal"><div class="metal__swatch metal__swatch--inox"></div><h3>Inox</h3><p>Tenue durable en milieu humide ou exposé, sans entretien : garde-corps, mains courantes, extérieurs.</p></article>
        <article class="work metal"><div class="metal__swatch metal__swatch--laiton"></div><h3>Laiton</h3><p>Pour les ouvrages décoratifs et les restaurations patrimoniales, pour sa teinte chaude et sa patine.</p></article>
      </div>
    </div>
  </section>

  <section class="section section--ice" id="methode">
    <div class="wrap">
      <div class="section-head section-head--center">
        <span class="eyebrow">Méthode</span>
        <h2>Comment se déroule un chantier</h2>
      </div>
      <ol class="steps">
        <li class="step"><h3>Prise de contact</h3><p>Vous nous décrivez le besoin, le bâtiment et les délais souhaités.</p></li>
        <li class="step"><h3>Visite et relevé</h3><p>Prise de cotes et vérification des contraintes de pose et d'accès.</p></li>
        <li class="step"><h3>Devis et plans</h3><p>Proposition chiffrée détaillée, métal, finition et fixation retenus.</p></li>
        <li class="step"><h3>Fabrication et pose</h3><p>Réalisation à l'atelier, traitement de surface, installation sur site.</p></li>
      </ol>
    </div>
  </section>
""" + cta("Votre ouvrage ne figure pas dans cette liste ?",
          "La métallerie est un métier de pièces uniques. Décrivez-nous votre besoin : si nous savons le faire, nous vous le chiffrons.") + """
</main>
""" + footer()
write("activites.html", act)

# ============================================================================
# REALISATIONS
# ============================================================================
GALLERY = [
    ("verriere", "Verrière en acier", "Fabrication et pose — Villefranche-sur-Saône", "Verrière", "vitrage"),
    ("chassis-acier", "Châssis acier vitrés", "Fabrication et pose — secteur Villefranche", "Châssis", "vitrage"),
    ("escalier", "Escalier métallique sur mesure", "Villefranche-sur-Saône", "Escalier", "escaliers"),
    ("balcon", "Balcon en acier", "Fabrication et pose — Villefranche-sur-Saône", "Balcon", "escaliers"),
    ("facade", "Façade métallique", "Pose — Villefranche-sur-Saône", "Façade", "structures"),
    ("petites-charpentes", "Petite charpente métallique", "Villefranche-sur-Saône", "Charpente", "structures"),
    ("travaux-metallerie", "Pose d'ouvrage métallique", "Chantier — Villefranche-sur-Saône", "Chantier", "structures"),
    ("metallerie", "Ouvrage de métallerie", "Villefranche-sur-Saône", "Métallerie", "structures"),
    ("pare-douche", "Pare-douche acier, vitrage sablé", "Secteur Villefranche-sur-Saône", "Agencement", "agencement"),
    ("ouvrage", "Ouvrage sur mesure", "Secteur Villefranche-sur-Saône", "Sur mesure", "agencement"),
]
FILTERS = [("tout", "Tout"), ("vitrage", "Verrières et châssis"), ("escaliers", "Escaliers et balcons"),
           ("structures", "Structures et façades"), ("agencement", "Agencement")]

real = head(
    "Nos réalisations — Métallerie BDO, Rhône et Beaujolais",
    "Galerie des réalisations de Métallerie BDO : lanterne acier et verre bombé, verrières, châssis acier, escaliers, balcons, façades, petites charpentes et agencement.",
    "realisations.html") + header("realisations.html") + "\n<main id=\"main\">\n" + page_hero(
    "Réalisations",
    "Nos réalisations",
    "Une sélection de chantiers menés dans le Rhône, du Val d'Azergues au Beaujolais et à Villefranche-sur-Saône.",
    "Réalisations") + f"""
  <section class="section">
    <div class="wrap">
      <div class="split split--top">
        <div>
          <span class="eyebrow">Projet à la une</span>
          <h2>Lanterne en acier et verre bombé</h2>
          <p class="lead">Création et pose d'une lanterne en acier avec vitrage bombé et finition thermolaquée.</p>
          <p>Un ouvrage qui réunit le cintrage précis de l'acier, l'ajustage du verre et un traitement de surface durable : le type de pièce unique que seul un atelier de métallerie peut produire.</p>
          <ul class="checks">
            <li>{icon("check")}<span>Structure acier cintrée</span></li>
            <li>{icon("check")}<span>Vitrage bombé</span></li>
            <li>{icon("check")}<span>Peinture thermolaquée</span></li>
          </ul>
        </div>
        <div class="featured">
          <div class="frame"><img data-photo src="assets/img/realisations/lanterne-1.webp" alt="Lanterne acier et verre bombé, vue d'ensemble" loading="lazy" width="900" height="675"></div>
          <div class="frame"><img data-photo src="assets/img/realisations/lanterne-2.webp" alt="Lanterne acier et verre bombé, détail de la structure" loading="lazy" width="450" height="340"></div>
          <div class="frame"><img data-photo src="assets/img/realisations/lanterne-3.webp" alt="Lanterne acier et verre bombé, détail de la finition" loading="lazy" width="450" height="340"></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--ice">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Galerie</span>
        <h2>Ouvrages récents</h2>
      </div>
      <div class="filters" role="group" aria-label="Filtrer les réalisations" data-filters hidden>
{chr(10).join(f'        <button class="filter" type="button" data-filter="{k}" aria-pressed="{"true" if k == "tout" else "false"}">{t}</button>' for k, t in FILTERS)}
      </div>
      <div class="grid grid--3" data-gallery>
{chr(10).join(project_card(i, t, s, tag, cat, href=None) for i, t, s, tag, cat in GALLERY)}
      </div>
      <div class="btn-row">
        <a class="btn btn--ghost" href="{IG}" rel="noopener noreferrer" target="_blank">{icon("instagram")} Plus de photos sur Instagram</a>
      </div>
    </div>
  </section>
""" + cta("Un projet similaire ?",
          "Envoyez-nous une description, des photos de l'existant ou un croquis : nous vous répondons avec une première estimation.") + """
</main>
""" + footer()
write("realisations.html", real)

# ============================================================================
# CONTACT
# ============================================================================
OUVRAGE_OPTS = ["Garde-corps / rampe", "Portail / portillon / clôture", "Grille de défense", "Escalier",
                "Balcon / passerelle", "Marquise", "Verrière / châssis acier", "Façade / bardage",
                "Petite charpente / structure", "Agencement (pare-douche, mobilier)",
                "Restauration de ferronnerie", "Dépannage / réparation", "Autre"]
PROFIL_OPTS = ["Particulier", "Professionnel (entreprise, architecte, maître d'œuvre)",
               "Collectivité ou organisme public", "Bailleur social"]
opts = lambda L: "\n".join(f"                <option>{o}</option>" for o in L)

contact = head(
    "Contact et devis — Métallerie BDO, Marcilly-d'Azergues (69)",
    "Contactez Métallerie BDO pour un devis de métallerie, serrurerie ou dépannage : 243 chemin des Ronzières, 69380 Marcilly-d'Azergues. Tél. 04 78 43 01 16.",
    "contact.html") + header("contact.html") + "\n<main id=\"main\">\n" + page_hero(
    "Contact",
    "Parlons de votre projet",
    "Décrivez-nous l'ouvrage souhaité et le contexte du chantier. Plus la demande est précise (dimensions, photos, délais), plus notre estimation sera fiable.",
    "Contact") + f"""
  <section class="section">
    <div class="wrap split split--top">

      <div class="form-card">
        <h2>Demande de devis</h2>
        <p class="hint">Nous vous répondons dans les plus brefs délais. Les champs marqués * sont obligatoires.</p>
        <div id="form-status" role="status" aria-live="polite"></div>

        <form class="form" id="devis" action="contact.php" method="post" accept-charset="UTF-8">
          <div class="hp" aria-hidden="true">
            <label for="site_web">Ne pas remplir ce champ</label>
            <input type="text" id="site_web" name="site_web" tabindex="-1" autocomplete="off">
          </div>

          <div class="form__row">
            <div class="field">
              <label for="nom">Nom et prénom *</label>
              <input type="text" id="nom" name="nom" required maxlength="100" autocomplete="name">
            </div>
            <div class="field">
              <label for="societe">Société <span class="hint">(facultatif)</span></label>
              <input type="text" id="societe" name="societe" maxlength="120" autocomplete="organization">
            </div>
          </div>

          <div class="form__row">
            <div class="field">
              <label for="email">E-mail *</label>
              <input type="email" id="email" name="email" required maxlength="150" autocomplete="email">
            </div>
            <div class="field">
              <label for="telephone">Téléphone *</label>
              <input type="tel" id="telephone" name="telephone" required maxlength="20" autocomplete="tel" pattern="[0-9 +().\\-]{{10,20}}">
            </div>
          </div>

          <div class="form__row">
            <div class="field">
              <label for="profil">Vous êtes *</label>
              <select id="profil" name="profil" required>
                <option value="">— Choisir —</option>
{opts(PROFIL_OPTS)}
              </select>
            </div>
            <div class="field">
              <label for="ouvrage">Type d'ouvrage *</label>
              <select id="ouvrage" name="ouvrage" required>
                <option value="">— Choisir —</option>
{opts(OUVRAGE_OPTS)}
              </select>
            </div>
          </div>

          <div class="field">
            <label for="commune">Commune du chantier *</label>
            <input type="text" id="commune" name="commune" required maxlength="100" autocomplete="address-level2">
          </div>

          <div class="field">
            <label for="message">Description du projet * <span class="hint">— dimensions, matériau, délai…</span></label>
            <textarea id="message" name="message" required minlength="20" maxlength="5000"></textarea>
          </div>

          <div class="field field--check">
            <input type="checkbox" id="rgpd" name="rgpd" value="1" required>
            <label for="rgpd">J'accepte que mes informations soient utilisées par Métallerie BDO pour traiter ma demande. Elles sont conservées 2 ans après notre dernier échange et ne sont jamais transmises à des tiers. <a href="mentions-legales.html#donnees">En savoir plus</a>. *</label>
          </div>

          <div><button class="btn btn--primary" type="submit">Envoyer ma demande {ARROW}</button></div>
        </form>
      </div>

      <aside>
        <div class="info-card">
          <h3>Métallerie BDO</h3>
          <ul class="info-list">
            <li><span class="icon-tile">{icon("pin")}</span><div><span class="k">Atelier</span><address class="v">{ADDR_1}<br>{ADDR_2}</address></div></li>
            <li><span class="icon-tile">{icon("phone")}</span><div><span class="k">Téléphone</span><a href="tel:{PHONE_TEL}">{PHONE_TXT}</a></div></li>
            <li><span class="icon-tile">{icon("mail")}</span><div><span class="k">E-mail</span><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
            <li><span class="icon-tile">{icon("ruler")}</span><div><span class="k">Secteur</span><span class="v">Lyon, Métropole, Rhône, Beaujolais et Val de Saône</span></div></li>
          </ul>
          <div class="btn-row">
            <a class="btn btn--light" href="https://www.google.com/maps/search/?api=1&amp;query=243+Chemin+des+Ronzi%C3%A8res+69380+Marcilly-d%27Azergues" rel="noopener noreferrer" target="_blank">{icon("pin")} Itinéraire</a>
            <a class="btn btn--outline" href="tel:{PHONE_TEL}">{icon("phone")} Appeler</a>
          </div>
        </div>

        <div class="recruit mt-md">
          <div>
            <h3>Rejoindre l'atelier</h3>
            <p>Métallier, serrurier, soudeur ? Envoyez-nous votre candidature spontanée.</p>
          </div>
          <a class="btn btn--navy" href="mailto:{EMAIL}?subject=Candidature%20spontan%C3%A9e">Postuler</a>
        </div>
      </aside>

    </div>
  </section>
</main>
""" + footer()
write("contact.html", contact)

# ============================================================================
# MENTIONS LEGALES
# ============================================================================
legal = head(
    "Mentions légales et données personnelles — Métallerie BDO",
    "Mentions légales, éditeur, hébergeur, médiation de la consommation et politique de protection des données du site Métallerie BDO.",
    "mentions-legales.html") + header("") + "\n<main id=\"main\">\n" + page_hero(
    "Informations légales", "Mentions légales et données personnelles",
    "Informations relatives à l'éditeur du site, à son hébergement et au traitement de vos données.",
    "Mentions légales") + f"""
  <section class="section">
    <div class="wrap prose">

      <h2>1. Éditeur du site</h2>
      <dl>
        <dt>Raison sociale</dt><dd>METALLERIE BDO</dd>
        <dt>Forme juridique</dt><dd>Société par actions simplifiée (SAS)</dd>
        <dt>Capital social</dt><dd>52 500 €</dd>
        <dt>Siège social</dt><dd>{ADDR_1}, {ADDR_2}, France</dd>
        <dt>Immatriculation</dt><dd>RCS Lyon 853 435 667 — SIRET 853 435 667 00011</dd>
        <dt>Code APE</dt><dd>43.32B — Travaux de menuiserie métallique et serrurerie</dd>
        <dt>TVA intracommunautaire</dt><dd>FR64853435667</dd>
        <dt>Téléphone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE_TXT}</a></dd>
        <dt>E-mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
        <dt>Directeur de la publication</dt><dd>Guy Odin, directeur général</dd>
      </dl>

      <h2>2. Hébergeur</h2>
      <!-- A METTRE A JOUR selon l'hebergeur retenu -->
      <dl>
        <dt>Société</dt><dd>OVH SAS</dd>
        <dt>Adresse</dt><dd>2 rue Kellermann, 59100 Roubaix, France</dd>
        <dt>Téléphone</dt><dd>09 72 10 10 07</dd>
      </dl>

      <h2>3. Médiation de la consommation</h2>
      <!-- OBLIGATOIRE (art. L612-1 Code de la consommation) : a completer avec le mediateur de l'entreprise -->
      <p>Conformément aux articles L612-1 et suivants du Code de la consommation, tout consommateur peut recourir gratuitement à un médiateur de la consommation en vue de la résolution amiable d'un litige.</p>
      <dl>
        <dt>Médiateur</dt><dd><span class="todo">À compléter</span></dd>
        <dt>Coordonnées</dt><dd><span class="todo">À compléter</span></dd>
      </dl>

      <h2>4. Propriété intellectuelle</h2>
      <p>L'ensemble des contenus de ce site (textes, photographies, logo, mise en page) est la propriété exclusive de METALLERIE BDO, sauf mention contraire. Toute reproduction ou adaptation, totale ou partielle, sans autorisation écrite préalable est interdite. Les noms des partenaires cités appartiennent à leurs titulaires respectifs. Les photographies sont non contractuelles.</p>
      <p>Police de caractères : Montserrat, distribuée sous licence SIL Open Font License 1.1.</p>

      <h2>5. Responsabilité</h2>
      <p>METALLERIE BDO s'efforce de fournir des informations exactes et à jour, sans pouvoir garantir l'absence d'erreur ou d'omission. Les liens vers des sites tiers sont fournis à titre d'information ; METALLERIE BDO n'exerce aucun contrôle sur leur contenu.</p>

      <h2 id="donnees">6. Protection des données personnelles</h2>
      <h3>Responsable du traitement</h3>
      <p>METALLERIE BDO, {ADDR_1}, {ADDR_2} — <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      <h3>Données collectées et finalité</h3>
      <p>Le formulaire de contact recueille : nom et prénom, société (facultatif), e-mail, téléphone, profil, type d'ouvrage, commune du chantier et description du projet. Ces données servent uniquement à répondre à votre demande et, le cas échéant, à établir un devis.</p>
      <h3>Base légale</h3>
      <p>Votre consentement, exprimé en cochant la case prévue, et les mesures précontractuelles prises à votre demande (article 6.1.a et 6.1.b du RGPD).</p>
      <h3>Destinataires et durée de conservation</h3>
      <p>Les données sont destinées exclusivement à METALLERIE BDO et ne sont ni vendues, ni cédées, ni transmises à des tiers. Elles sont conservées deux ans à compter du dernier contact. Si un devis est accepté, les données nécessaires à la relation commerciale sont conservées pendant la durée légale applicable aux documents comptables.</p>
      <h3>Vos droits</h3>
      <p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité, ainsi que du droit de retirer votre consentement à tout moment, en écrivant à <a href="mailto:{EMAIL}">{EMAIL}</a> ou à l'adresse du siège. Réponse sous un mois. Vous pouvez également saisir la CNIL : <a href="https://www.cnil.fr/fr/plaintes" rel="noopener noreferrer">www.cnil.fr/fr/plaintes</a>.</p>

      <h2>7. Cookies et traceurs</h2>
      <p>Ce site ne dépose aucun cookie publicitaire ni de mesure d'audience et n'intègre aucun service tiers chargé automatiquement (police, carte, vidéo, réseau social). Seul un cookie technique de session est créé lors de l'envoi du formulaire, afin de limiter les envois abusifs ; strictement nécessaire, il est exempté de consentement (article 82 de la loi Informatique et Libertés). C'est pourquoi aucun bandeau de consentement n'est affiché.</p>

      <h2>8. Droit applicable</h2>
      <p>Les présentes mentions sont régies par le droit français. À défaut de résolution amiable, les tribunaux français sont seuls compétents.</p>

      <p class="hint">Dernière mise à jour : octobre 2026.</p>
    </div>
  </section>
</main>
""" + footer()
write("mentions-legales.html", legal)

# ============================================================================
# 404 (chemins relatifs a la racine du domaine, servie a n'importe quelle profondeur)
# ============================================================================
p404 = (head("Page introuvable — Métallerie BDO", "Cette page n'existe pas ou a été déplacée.", "404.html", robots="noindex")
        .replace('href="assets/', 'href="/assets/'))
p404 += f"""
<main id="main">
  <section class="page-hero">
    <div class="wrap page-hero__inner">
      <span class="eyebrow">Erreur 404</span>
      <h1>Cette page n'existe pas ou a été déplacée</h1>
      <p>Le site a été entièrement refait : l'adresse suivie correspond peut-être à l'ancienne version.</p>
      <div class="btn-row">
        <a class="btn btn--light" href="/">Retour à l'accueil</a>
        <a class="btn btn--outline" href="/contact.html">Nous contacter</a>
      </div>
    </div>
  </section>
</main>
</body>
</html>
"""
write("404.html", p404)
