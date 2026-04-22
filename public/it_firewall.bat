@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Reparar Firewall - Andres Pinto IT
echo =============================================
echo   Reseteando reglas del Firewall de Windows...
netsh advfirewall reset
echo   Reactivando Firewall en todos los perfiles...
netsh advfirewall set allprofiles state on
echo.
echo   [OK] Firewall restaurado a configuracion predeterminada.
echo =============================================
pause
