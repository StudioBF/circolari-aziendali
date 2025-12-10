@echo off
cd /d "%~dp0"
title FioberBot - Server Telegram
color 0A
cls
echo ========================================================
echo   FIOBER BOT - SERVER DI PUBBLICAZIONE
echo ========================================================
echo.
echo   Il bot e' ora ATTIVO e in ascolto.
echo   Puoi tornare sul sito e cliccare "Pubblica".
echo.
echo   [!] PER SPEGNERE: Chiudi semplicemente questa finestra.
echo.
echo ========================================================
echo.
python telegram_publisher.py
pause
