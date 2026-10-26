@echo off
title Actualizador de English Quest
color 0E

echo =======================================================
echo    🔄 BUSCANDO ACTUALIZACIONES...
echo =======================================================
echo.

:: Verifica si existe la carpeta .git
if not exist ".git" (
    echo ❌ ERROR: No se encontro la carpeta .git.
    echo Asegurate de haber descargado el proyecto como repositorio (git clone) y no como ZIP.
    pause
    exit
)

echo Conectando con GitHub...
:: El --no-pager evita que se quede atascado en una pantalla de texto
git --no-pager pull origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ ¡Actualizacion completada con exito!
    echo Si se descargaron cambios, cierra y vuelve a abrir el juego.
) else (
    echo.
    echo ⚠️ Hubo un problema al actualizar. 
    echo Posibles causas: No tienes internet, o no has iniciado sesion en Git en esta PC.
)

echo.
echo Presiona cualquier tecla para cerrar esta ventana...
pause >nul