@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Limpieza Profunda - Andres Pinto IT
echo =============================================
echo   [1/4] Vaciando TEMP del perfil de usuario...
del /q /f /s %TEMP%\* >nul 2>&1
echo   [2/4] Limpiando C:\Windows\Temp...
del /q /f /s C:\Windows\Temp\* >nul 2>&1
echo   [3/4] Borrando archivos Prefetch...
del /q /f /s C:\Windows\Prefetch\* >nul 2>&1
echo   [4/4] Vaciando Papelera de reciclaje...
rd /s /q %systemdrive%\$Recycle.bin >nul 2>&1
echo.
echo   [OK] Limpieza completada. PC mas rapido.
echo =============================================
pause
