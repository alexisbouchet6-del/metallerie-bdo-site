/**
 * Métallerie BDO - script principal.
 *
 * Amelioration progressive : le site reste entierement consultable sans
 * JavaScript. Ce fichier ajoute uniquement du confort d'usage.
 */
(function () {
  "use strict";

  /* ---------------------------------------------------------------------
     1. Menu mobile
     --------------------------------------------------------------------- */
  var burger = document.querySelector("[data-burger]");
  var nav = document.querySelector("[data-nav]");

  function setMenu(open) {
    burger.setAttribute("aria-expanded", String(open));
    burger.setAttribute("aria-label", open ? "Fermer le menu" : "Ouvrir le menu");
    nav.setAttribute("data-open", String(open));
  }

  if (burger && nav) {
    burger.addEventListener("click", function () {
      setMenu(burger.getAttribute("aria-expanded") !== "true");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) { setMenu(false); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.getAttribute("data-open") === "true") {
        setMenu(false);
        burger.focus();
      }
    });
  }

  /* ---------------------------------------------------------------------
     2. Ombre de l'en-tete au defilement
     requestAnimationFrame : un seul calcul par image, pas a chaque evenement
     --------------------------------------------------------------------- */
  var header = document.querySelector("[data-header]");
  if (header) {
    var ticking = false;
    var update = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
      ticking = false;
    };
    window.addEventListener("scroll", function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ---------------------------------------------------------------------
     3. Annee du pied de page
     --------------------------------------------------------------------- */
  var year = String(new Date().getFullYear());
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = year; });

  /* ---------------------------------------------------------------------
     4. Photos absentes : on retire l'image cassee, le cadre affiche
        "Photo a venir" (classe .frame--empty)
     --------------------------------------------------------------------- */
  function dropBroken(img) {
    var frame = img.closest(".frame");
    if (frame) { frame.classList.add("frame--empty"); }
    img.remove();
  }
  document.querySelectorAll("img[data-photo]").forEach(function (img) {
    if (img.complete && img.naturalWidth === 0) {
      dropBroken(img);
    } else {
      img.addEventListener("error", function () { dropBroken(img); });
    }
  });

  /* ---------------------------------------------------------------------
     5. Filtres de la galerie (page Realisations)
     Les boutons sont masques par defaut (attribut hidden) et n'apparaissent
     que si le script tourne : sans JS, toute la galerie reste visible.
     --------------------------------------------------------------------- */
  var filters = document.querySelector("[data-filters]");
  var gallery = document.querySelector("[data-gallery]");
  if (filters && gallery) {
    filters.hidden = false;
    var buttons = filters.querySelectorAll("[data-filter]");
    var items = gallery.querySelectorAll("[data-cat]");
    filters.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-filter]");
      if (!btn) { return; }
      var cat = btn.getAttribute("data-filter");
      buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      items.forEach(function (it) {
        it.hidden = cat !== "tout" && it.getAttribute("data-cat") !== cat;
      });
    });
  }

  /* ---------------------------------------------------------------------
     6. Retour du formulaire (contact.php -> contact.html?envoi=<code>)
     textContent : aucune injection HTML possible depuis l'URL
     --------------------------------------------------------------------- */
  var statusBox = document.getElementById("form-status");
  if (statusBox && window.URLSearchParams) {
    var code = new URLSearchParams(window.location.search).get("envoi");
    var messages = {
      ok:       ["ok",  "Merci, votre demande a bien été envoyée. Nous vous recontactons rapidement."],
      invalide: ["err", "Certains champs sont incomplets ou invalides. Merci de vérifier le formulaire."],
      attente:  ["err", "Une demande vient d'être envoyée. Merci de patienter une minute avant de réessayer."],
      erreur:   ["err", "L'envoi a échoué pour une raison technique. Appelez-nous au 04 78 43 01 16 ou écrivez à contact@metallerie-bdo.fr."]
    };
    if (code && messages[code]) {
      var p = document.createElement("p");
      p.className = "alert alert--" + messages[code][0];
      p.textContent = messages[code][1];
      statusBox.appendChild(p);
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, "", window.location.pathname + "#devis");
      }
    }
  }
})();
