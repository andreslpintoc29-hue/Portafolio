@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title MODO DIOS - Mantenimiento Total - Andres Pinto IT
echo ========================================================
echo        SISTEMA DE MANTENIMIENTO TOTAL INSTITUCIONAL
echo                  BY: ANDRES PINTO
echo                 (MODO ADMINISTRADOR)
echo ========================================================
echo.

echo [1/12] VACIANDO ARCHIVOS BASURA Y TEMPORALES...
del /q /f /s %TEMP%\* >nul 2>&1
del /q /f /s C:\Windows\Temp\* >nul 2>&1
echo --- Limpieza Finalizada.

echo.
echo [2/12] REPARANDO COLA DE IMPRESION (SPOOLER)...
net stop spooler >nul 2>&1
del /Q /F /S "%systemroot%\System32\Spool\Printers\*.*" >nul 2>&1
net start spooler >nul 2>&1

echo.
echo [3/12] REINICIANDO SERVICIOS DE ESCANER Y DIGITALIZACION (WIA)...
net stop stisvc >nul 2>&1
net start stisvc >nul 2>&1

echo.
echo [4/12] VACIANDO CACHE DE RED Y RENOVANDO IP (DNS)...
ipconfig /release >nul 2>&1
ipconfig /renew >nul 2>&1
ipconfig /flushdns >nul 2>&1

echo.
echo [5/12] REPARANDO WINDOWS UPDATE...
net stop wuauserv >nul 2>&1
net stop bits >nul 2>&1
rd /s /q C:\Windows\SoftwareDistribution\Download >nul 2>&1
net start wuauserv >nul 2>&1
net start bits >nul 2>&1

echo.
echo [6/12] REINICIANDO EXPLORER...
taskkill /f /im explorer.exe >nul 2>&1
start explorer.exe

echo.
echo [7/12] LIBERANDO RAM Y CERRANDO PROCESOS PESADOS...
taskkill /f /im Teams.exe >nul 2>&1
taskkill /f /im OneDrive.exe >nul 2>&1
taskkill /f /im Widgets.exe >nul 2>&1

echo.
echo [8/12] RESTAURANDO FIREWALL...
netsh advfirewall reset >nul 2>&1

echo.
echo [9/12] REINICIANDO AUDIO...
net stop Audiosrv >nul 2>&1
net stop AudioEndpointBuilder >nul 2>&1
net start AudioEndpointBuilder >nul 2>&1
net start Audiosrv >nul 2>&1

echo.
echo [10/12] REALIZANDO ESCANEO CHKDSK...
echo (Este proceso puede tardar minutos. No lo cierres)
chkdsk C: /F /X

echo.
echo ========================================================
echo MANTENIMIENTO TOTAL "MODO DIOS" FINALIZADO CON EXITO
echo Todos los servicios conflictivos han sido reiniciados a la fuerza.
echo ========================================================
echo.
pause
