@echo off
setlocal

:choisir_fichier
set "filepath=D:\NSI\2Methylbutan2ol-Serpentes\main.py"

if not exist "%filepath%" (
    echo Erreur : Le fichier n'existe pas. Veuillez reessayer.
    goto choisir_fichier
)

echo Execution de %filepath%...
python "%filepath%"

pause
