@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Reparar Red - Andres Pinto IT
echo =============================================
echo   Liberando IP actual...
ipconfig /release
echo   Solicitando nueva IP...
ipconfig /renew
echo   Purgando cache DNS...
ipconfig /flushdns
echo   Reiniciando stack Winsock...
netsh winsock reset
echo.
echo   [OK] Red reparada. Reinicie el equipo.
echo =============================================
pause
