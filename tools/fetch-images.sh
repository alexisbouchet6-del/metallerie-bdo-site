#!/usr/bin/env bash
# Telecharge les photos de realisations de l'ancien site (Local.fr)
# vers assets/img/realisations/. Equivalent Linux/macOS de fetch-images.ps1.
#
# Usage : ./tools/fetch-images.sh [--force]
set -euo pipefail

FORCE=0
[[ "${1:-}" == "--force" ]] && FORCE=1

BASE="https://local-fr-public.s3.eu-west-3.amazonaws.com/prod/webtool/userfiles/138120"
TARGET="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/assets/img/realisations"
mkdir -p "$TARGET"

# Format : nom_local|chemin_distant_deja_encode
IMAGES=(
  "pare-douche.webp|modif25092024/R%C3%A9alisation%20d%27un%20pare%20douche%20en%20acier%20avec%20vitrage%20sabl%C3%A9%20pr%C3%A8s%20de%20Villefranche-sur-Sa%C3%B4ne.webp"
  "petites-charpentes.webp|NouveauDossier/Travaux%20Petites%20charpentes%20%C3%A0%20Villefranche-sur-Sa%C3%B4ne.webp"
  "metallerie.webp|NouveauDossier/Service%20M%C3%A9tallerie%20%C3%A0%20Villefranche-sur-Sa%C3%B4ne.webp"
  "escalier.webp|NouveauDossier/service%20Escaliers%20m%C3%A9talliques%20sur%20mesure%20%C3%A0%20Villefranche-sur-Sa%C3%B4ne.webp"
  "verriere.webp|NouveauDossier/Pose%20Verri%C3%A8res%20%C3%A0%20illefranche-sur-Sa%C3%B4ne.webp"
  "travaux-metallerie.webp|NouveauDossier/Pose%20Travaux%20M%C3%A9tallerie%20%C3%A0%20Villefranche-sur-Sa%C3%B4ne.webp"
  "ouvrage.webp|modif25092024/La%20galerie%20photos%20de%20M%C3%A9tallerie%20BDO%20pr%C3%A8s%20de%20Villefranche-sur-Sa%C3%B4ne4.webp"
  "facade.webp|NouveauDossier/Pose%20Fa%C3%A7ades%20en%20m%C3%A9tallique%20%C3%A0%20Villefranche-sur-Sa%C3%B4ne.webp"
  "chassis-acier.webp|modif25092024/Fabrication%20et%20pose%20des%20ch%C3%A2ssis%20aciers%20pr%C3%A8s%20de%20Villefranche-sur-Sa%C3%B4ne.webp"
  "balcon.webp|NouveauDossier/Pose%20balcons%20en%20acier%20%C3%A0%20Villefranche-sur-Sa%C3%B4ne.webp"
  "lanterne-1.webp|modif25092024/La%20galerie%20photos%20de%20M%C3%A9tallerie%20BDO%20pr%C3%A8s%20de%20Villefranche-sur-Sa%C3%B4ne2.webp"
  "lanterne-2.webp|modif25092024/La%20galerie%20photos%20de%20M%C3%A9tallerie%20BDO%20pr%C3%A8s%20de%20Villefranche-sur-Sa%C3%B4ne1.webp"
  "lanterne-3.webp|modif25092024/La%20galerie%20photos%20de%20M%C3%A9tallerie%20BDO%20pr%C3%A8s%20de%20Villefranche-sur-Sa%C3%B4ne3.webp"
)

ok=0; skipped=0; failed=0
for entry in "${IMAGES[@]}"; do
  name="${entry%%|*}"
  path="${entry#*|}"
  dest="$TARGET/$name"

  if [[ -f "$dest" && $FORCE -eq 0 ]]; then
    echo "[skip] $name"; skipped=$((skipped + 1)); continue
  fi

  if curl -fsS --max-time 30 -o "$dest" "$BASE/$path"; then
    echo "[ ok ] $name"; ok=$((ok + 1))
  else
    echo "[fail] $name" >&2; rm -f "$dest"; failed=$((failed + 1))
  fi
done

echo
echo "Termine : $ok telecharge(s), $skipped ignore(s), $failed echec(s)."
[[ $failed -eq 0 ]]
