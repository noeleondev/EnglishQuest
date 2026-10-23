@echo off
title Actualizador de English Quest
color 0E

echo =======================================================
echo    🔄 BUSCANDO ACTUALIZACIONES...
echo =======================================================
echo.

:: Verifica si existe la carpeta .git
if not exist ".git" (
    echo ❌ ERROR: No se encontro el repositorio de Git.
    echo Asegurate de haber descargado el proyecto correctamente.
    pause
    exit
)

echo Descargando cambios desde GitHub...
git pull origin main

echo.
if %errorlevel% equ 0 (
    echo ✅ Actualizacion completada con exito.
    echo (Si se descargaron archivos, cierra y vuelve a abrir el juego).
) else (
    echo ⚠️ Hubo un problema al actualizar. Revisa tu conexion a internet.
)
echo.
pause