@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Reparar Audio - Andres Pinto IT
echo =============================================
echo   Deteniendo servicio de audio Windows...
net stop Audiosrv >nul 2>&1
net stop AudioEndpointBuilder >nul 2>&1
echo   Reiniciando servicios de audio...
net start AudioEndpointBuilder
net start Audiosrv
echo.
echo   [OK] Audio de Windows reiniciado correctamente.
echo =============================================
pause
