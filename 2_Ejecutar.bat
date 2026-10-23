@echo off
title English Quest - Servidor Activo
color 0B

echo =======================================================
echo    🎮 INICIANDO ENGLISH QUEST...
echo =======================================================
echo.
echo Iniciando el servidor de Python en segundo plano...

:: Abre el navegador 2 segundos después de iniciar el servidor
start /b cmd /c "timeout /t 2 >nul & start http://localhost:5000"

:: Inicia el servidor Flask (esto mantiene la ventana abierta)
python servidor.py

pause