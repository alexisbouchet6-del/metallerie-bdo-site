<#
.SYNOPSIS
    Telecharge les photos de realisations de l'ancien site Metallerie BDO
    (heberge par Local.fr) vers assets/img/realisations/.

.DESCRIPTION
    Pourquoi heberger les images localement plutot que de les lier :
    les photos actuelles sont stockees sur le compte S3 de Local.fr. A la fin
    du contrat avec ce prestataire, ces URL cesseront de repondre et la
    galerie du nouveau site serait vide.

    Le script est idempotent : un fichier deja present n'est pas retelecharge
    (utiliser -Force pour ecraser).

.EXAMPLE
    PS> cd metallerie-bdo-site
    PS> .\tools\fetch-images.ps1

.EXAMPLE
    PS> .\tools\fetch-images.ps1 -Force
#>
[CmdletBinding()]
param(
    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$base = 'https://local-fr-public.s3.eu-west-3.amazonaws.com/prod/webtool/userfiles/138120'

# Nom local => chemin distant (non encode : Invoke-WebRequest gere l'encodage)
$images = [ordered]@{
    'pare-douche.webp'        = "$base/modif25092024/Réalisation d'un pare douche en acier avec vitrage sablé près de Villefranche-sur-Saône.webp"
    'petites-charpentes.webp' = "$base/NouveauDossier/Travaux Petites charpentes à Villefranche-sur-Saône.webp"
    'metallerie.webp'         = "$base/NouveauDossier/Service Métallerie à Villefranche-sur-Saône.webp"
    'escalier.webp'           = "$base/NouveauDossier/service Escaliers métalliques sur mesure à Villefranche-sur-Saône.webp"
    'verriere.webp'           = "$base/NouveauDossier/Pose Verrières à illefranche-sur-Saône.webp"
    'travaux-metallerie.webp' = "$base/NouveauDossier/Pose Travaux Métallerie à Villefranche-sur-Saône.webp"
    'ouvrage.webp'            = "$base/modif25092024/La galerie photos de Métallerie BDO près de Villefranche-sur-Saône4.webp"
    'facade.webp'             = "$base/NouveauDossier/Pose Façades en métallique à Villefranche-sur-Saône.webp"
    'chassis-acier.webp'      = "$base/modif25092024/Fabrication et pose des châssis aciers près de Villefranche-sur-Saône.webp"
    'balcon.webp'             = "$base/NouveauDossier/Pose balcons en acier à Villefranche-sur-Saône.webp"
    'lanterne-1.webp'         = "$base/modif25092024/La galerie photos de Métallerie BDO près de Villefranche-sur-Saône2.webp"
    'lanterne-2.webp'         = "$base/modif25092024/La galerie photos de Métallerie BDO près de Villefranche-sur-Saône1.webp"
    'lanterne-3.webp'         = "$base/modif25092024/La galerie photos de Métallerie BDO près de Villefranche-sur-Saône3.webp"
}

# Dossier cible calcule depuis l'emplacement du script : fonctionne quel que
# soit le repertoire courant.
$target = Join-Path (Split-Path -Parent $PSScriptRoot) 'assets\img\realisations'
if (-not (Test-Path $target)) {
    New-Item -ItemType Directory -Path $target | Out-Null
}

$ok = 0; $skipped = 0; $failed = 0

foreach ($name in $images.Keys) {
    $dest = Join-Path $target $name

    if ((Test-Path $dest) -and -not $Force) {
        Write-Host "[skip] $name (deja present)" -ForegroundColor DarkGray
        $skipped++
        continue
    }

    # Encodage explicite de l'URL : les noms contiennent accents, espaces
    # et apostrophes. On encode chaque segment apres le domaine.
    $uri = [System.Uri]::new($images[$name])
    $encoded = $uri.AbsoluteUri

    try {
        Invoke-WebRequest -Uri $encoded -OutFile $dest -UseBasicParsing -TimeoutSec 30
        $size = [math]::Round((Get-Item $dest).Length / 1KB)
        Write-Host "[ ok ] $name ($size Ko)" -ForegroundColor Green
        $ok++
    }
    catch {
        Write-Warning "[fail] $name : $($_.Exception.Message)"
        if (Test-Path $dest) { Remove-Item $dest -Force }
        $failed++
    }
}

Write-Host ""
Write-Host "Termine : $ok telecharge(s), $skipped ignore(s), $failed echec(s)."
if ($failed -gt 0) { exit 1 }
