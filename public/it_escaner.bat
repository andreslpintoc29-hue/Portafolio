@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Reparar Escaner - Andres Pinto IT
echo =============================================
echo   Deteniendo servicios WIA (Escaner)...
net stop stisvc
echo   Reiniciando servicios...
net start stisvc
echo.
echo   [OK] Escaner reestablecido.
echo =============================================
pause
