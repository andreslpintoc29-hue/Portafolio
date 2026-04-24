@echo off
color 0A
title Liberar Memoria RAM - Andres Pinto IT
echo =============================================
echo   Cerrando procesos en segundo plano pesados...
taskkill /f /im SearchUI.exe >nul 2>&1
taskkill /f /im SearchApp.exe >nul 2>&1
taskkill /f /im OneDrive.exe >nul 2>&1
taskkill /f /im SkypeApp.exe >nul 2>&1
taskkill /f /im Teams.exe >nul 2>&1
taskkill /f /im Widgets.exe >nul 2>&1
taskkill /f /im GameBar.exe >nul 2>&1
echo   Vaciando cache de memoria del sistema...
powershell -Command "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"
echo.
echo   [OK] RAM liberada. Procesos innecesarios eliminados.
echo =============================================
pause
