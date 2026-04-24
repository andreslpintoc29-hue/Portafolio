@echo off
title Resucitar Pantalla - Andres Pinto IT
color 0A
echo =============================================
echo   Matando proceso Explorer.exe...
taskkill /f /im explorer.exe >nul 2>&1
echo   Reiniciando interfaz de Windows...
start explorer.exe
echo.
echo   [OK] Shell de Windows reiniciado.
echo =============================================
pause
