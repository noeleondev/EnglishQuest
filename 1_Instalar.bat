@echo off
title Instalador de English Quest
color 0A

echo =======================================================
echo    🎮 BIENVENIDO A ENGLISH QUEST - INSTALADOR
echo =======================================================
echo.
echo Comprobando si tienes Python instalado...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ❌ ERROR: No tienes Python instalado o no esta en el PATH.
    echo.
    echo Por favor, descarga Python en: https://www.python.org/downloads/
    echo IMPORTANTE: Al instalar, marca la casilla "Add Python to PATH".
    echo.
    pause
    exit
)

echo ✅ Python detectado correctamente.
echo.
echo Instalando librerias necesarias (Flask)...
pip install flask
echo.
echo =======================================================
echo    CREANDO ACCESO DIRECTO EN EL ESCRITORIO...
echo =======================================================

:: Crear un archivo temporal de VBScript para generar el acceso directo
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = oWS.ExpandEnvironmentStrings("%USERPROFILE%\Desktop\English Quest.lnk") >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%~dp02_Ejecutar.bat" >> CreateShortcut.vbs
echo oLink.WorkingDirectory = "%~dp0" >> CreateShortcut.vbs
echo oLink.Description = "Jugar English Quest" >> CreateShortcut.vbs
echo oLink.IconLocation = "shell32.dll, 43" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs

cscript //nologo CreateShortcut.vbs
del CreateShortcut.vbs

echo.
echo ✅ ¡Instalacion completada!
echo ✅ Se ha creado un acceso directo en tu escritorio llamado "English Quest".
echo.
echo Ahora puedes cerrar esta ventana y usar el acceso directo.
pause