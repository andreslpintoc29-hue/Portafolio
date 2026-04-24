@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Diagnostico WiFi Avanzado - Andres Pinto IT
echo =============================================
echo   Generando reporte avanzado de WiFi...
netsh wlan show interfaces
echo.
echo   Redes disponibles detectadas:
netsh wlan show networks mode=bssid
echo.
echo   Exportando reporte HTML a C:\WiFi_Report.html...
netsh wlan show wlanreport >nul 2>&1
echo.
echo   [OK] Diagnostico WiFi completo. Revise C:\WiFi_Report.html
echo =============================================
pause
