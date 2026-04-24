@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Diagnostico Disco Duro - Andres Pinto IT
echo =============================================
echo   Ejecutando CHKDSK en unidad C:
echo   Esto detecta sectores danados y errores logicos.
echo =============================================
chkdsk C: /F /R /X
echo.
echo   [OK] Analisis de disco completado.
echo =============================================
pause
