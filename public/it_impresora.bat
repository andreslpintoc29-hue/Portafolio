@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Reparar Impresora - Andres Pinto IT
echo =============================================
echo   Deteniendo servicio Spooler...
net stop spooler
echo   Borrando documentos fantasma atascados...
del /Q /F /S "%systemroot%\System32\Spool\Printers\*.*" >nul 2>&1
echo   Reiniciando servicio Spooler...
net start spooler
echo.
echo   [OK] Impresora desbloqueada.
echo =============================================
pause
