/**
 * Métallerie BDO - script principal
 *
 * Portee volontairement minimale : le site doit rester entierement
 * consultable sans JavaScript (progressive enhancement). Ce fichier ne gere
 * que le menu mobile et l'annee du pied de page.
 */
(function () {
  "use strict";

  /* ----------------------------------------------------------------------
     Menu mobile
     Le bouton porte aria-expanded, l'etat d'ouverture est stocke dans
     data-open sur le <nav> : le CSS fait le reste (pas de style inline).
     ---------------------------------------------------------------------- */
  var burger = document.querySelector("[data-burger]");
  var nav = document.querySelector("[data-nav]");

  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", String(!open));
      nav.setAttribute("data-open", String(!open));
    });

    // Fermeture du menu apres un clic sur un lien (navigation par ancre)
    nav.addEventListener("click", function (event) {
      if (event.target.closest("a")) {
        burger.setAttribute("aria-expanded", "false");
        nav.setAttribute("data-open", "false");
      }
    });

    // Fermeture au clavier (touche Echap)
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && nav.getAttribute("data-open") === "true") {
        burger.setAttribute("aria-expanded", "false");
        nav.setAttribute("data-open", "false");
        burger.focus();
      }
    });
  }

  /* ----------------------------------------------------------------------
     Annee courante dans le pied de page
     Evite d'avoir a modifier chaque page au 1er janvier.
     ---------------------------------------------------------------------- */
  var yearSlots = document.querySelectorAll("[data-year]");
  var year = String(new Date().getFullYear());
  for (var i = 0; i < yearSlots.length; i++) {
    yearSlots[i].textContent = year;
  }

  /* ----------------------------------------------------------------------
     Images manquantes
     Si une photo de realisation n'est pas encore deposee dans
     assets/img/realisations/, on retire la balise <img> : le cadre parent
     affiche alors son fond neutre au lieu de l'icone "image cassee".
     ---------------------------------------------------------------------- */
  function dropBroken(img) {
    var frame = img.closest(".frame");
    if (frame) { frame.classList.add("frame--empty"); }
    img.remove();
  }
  var photos = document.querySelectorAll("img[data-photo]");
  for (var j = 0; j < photos.length; j++) {
    var img = photos[j];
    // Image deja en echec avant l'execution du script (cache, chargement rapide)
    if (img.complete && img.naturalWidth === 0) {
      dropBroken(img);
    } else {
      img.addEventListener("error", function () { dropBroken(this); });
    }
  }

  /* ----------------------------------------------------------------------
     Retour du formulaire de contact
     contact.php redirige vers contact.html?envoi=<code>. On affiche le
     message correspondant ; textContent evite toute injection HTML.
     ---------------------------------------------------------------------- */
  var statusBox = document.getElementById("form-status");
  if (statusBox && window.URLSearchParams) {
    var code = new URLSearchParams(window.location.search).get("envoi");
    var messages = {
      ok:       ["ok",  "Merci, votre demande a bien été envoyée. Nous vous recontactons rapidement."],
      invalide: ["err", "Certains champs sont incomplets ou invalides. Merci de vérifier le formulaire."],
      attente:  ["err", "Une demande vient déjà d'être envoyée. Merci de patienter une minute avant de réessayer."],
      erreur:   ["err", "L'envoi a échoué pour une raison technique. Appelez-nous au 04 78 43 01 16 ou écrivez à contact@metallerie-bdo.fr."]
    };
    if (code && messages[code]) {
      var alertBox = document.createElement("p");
      alertBox.className = "alert alert--" + messages[code][0];
      alertBox.textContent = messages[code][1];
      statusBox.appendChild(alertBox);
      // Une fois affiche, on nettoie l'URL pour qu'un rechargement ne repete pas le message
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, "", window.location.pathname + "#devis");
      }
    }
  }
})();
