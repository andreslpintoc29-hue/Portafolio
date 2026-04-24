@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Reparar Puertos USB - Andres Pinto IT
echo =============================================
echo   Reiniciando controladores USB del sistema...
powershell -Command "Get-PnpDevice -Class USB | Where-Object {$_.Status -eq 'Error'} | Enable-PnpDevice -Confirm:$false" >nul 2>&1
echo   Forzando reenumeracion de dispositivos...
pnputil /scan-devices
echo.
echo   [OK] Puertos USB reiniciados. Reconecte el dispositivo.
echo =============================================
pause
