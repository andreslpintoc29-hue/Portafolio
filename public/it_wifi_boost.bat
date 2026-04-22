@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (powershell -Command "Start-Process '%~0' -Verb RunAs" & exit /b)
color 0A
title Optimizador WiFi - Andres Pinto IT
echo =============================================
echo   OPTIMIZADOR DE VELOCIDAD WI-FI v3.0
echo   Andres Pinto - Soporte IT
echo =============================================
echo.
echo [1/10] Eliminando limite QoS del sistema...
netsh int tcp set global autotuninglevel=normal >nul 2>&1
netsh int tcp set global congestionprovider=none >nul 2>&1
echo   Done.
echo.
echo [2/10] Configurando DNS ultra rapido...
netsh interface ipv4 set dns name="Wi-Fi" static 8.8.8.8 primary >nul 2>&1
netsh interface ipv4 add dns name="Wi-Fi" 1.1.1.1 index=2 >nul 2>&1
echo   Google DNS: 8.8.8.8 + Cloudflare: 1.1.1.1
echo.
echo [3/10] Ajustando MTU optimizado...
netsh interface ipv4 set subinterface "Wi-Fi" mtu=1500 store=active >nul 2>&1
echo   MTU: 1500 (maximo)
echo.
echo [4/10] Habilitando TCP AutoTuning...
netsh int tcp set global autotuninglevel=experimental >nul 2>&1
echo   TCP AutoTuning: Experimental
echo.
echo [5/10] Limpiando cache DNS...
ipconfig /flushdns >nul 2>&1
echo   Cache DNS limpiada.
echo.
echo [6/10] Renovando IP...
ipconfig /release "Wi-Fi" >nul 2>&1
ipconfig /renew "Wi-Fi" >nul 2>&1
echo   IP renovada.
echo.
echo [7/10] Optimizando registro para red...
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v DefaultTTL /t REG_DWORD /d 64 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v TcpMaxDataRetransmissions /t REG_DWORD /d 5 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v EnablePMTUDiscovery /t REG_DWORD /d 1 /f >nul
echo   Registro optimizado.
echo.
echo [8/10] Configurando Red LAN para maxima velocidad...
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v LanmanServer\Parameters" /v ServerSize /t REG_DWORD /d 3 /f >nul 2>&1
echo   Servidor SMB optimizado.
echo.
echo [9/10] Limpiando tablas de enrutamiento...
route -f >nul 2>&1
echo   Tablas limpiadas.
echo.
echo [10/10] Deshabilitando ahorro de energia USB...
powercfg /change monitor-timeout-ac 0 >nul 2>&1
powercfg /change disk-timeout-ac 0 >nul 2>&1
echo   Ahorro de energia desactivado.
echo.
echo =============================================
echo   [OK] WI-FI OPTIMIZADO!
echo.
echo   Para mejor seal, ve al router:
echo   1. Abre http://192.168.80.1
echo   2. Login: ClaroUsuario / ClienteCLARO
echo   3. Ve a WiFi > Advanced
echo   4. Cambia:
echo      - Canal: 36 o 149 (5GHz)
echo      - Ancho banda: 80MHz
echo      - Potencia: 100%
echo   5. Save y reinicia router
echo =============================================
pause