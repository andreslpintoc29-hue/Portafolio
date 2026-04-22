@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Reparar Windows Update - Andres Pinto IT
echo =============================================
echo   Deteniendo Windows Update y BITS...
net stop wuauserv
net stop bits
echo   Borrando boveda corrupta SoftwareDistribution...
rd /s /q C:\Windows\SoftwareDistribution\Download >nul 2>&1
echo   Reiniciando servicios...
net start wuauserv
net start bits
echo.
echo   [OK] Windows Update reparado.
echo =============================================
pause
