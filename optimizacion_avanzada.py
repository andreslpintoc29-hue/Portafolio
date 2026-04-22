#!/usr/bin/env python3
import subprocess
import os
import re

def run_command(cmd, desc):
    print(f"\n[*] {desc}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] {desc} - Completado")
            return True
        else:
            print(f"[X] {desc} - Error: {result.stderr or result.stdout}")
            return False
    except Exception as e:
        print(f"[X] {desc} - Excepcion: {e}")
        return False

def optimize_dns():
    print("\n" + "="*50)
    print("  OPTIMIZANDO DNS")
    print("="*50)
    
    dns_configs = [
        ("netsh interface ipv4 set dns name=\"Ethernet\" static 1.1.1.1 primary", "Configurar DNS Cloudflare (1.1.1.1)"),
    ]
    
    for cmd, desc in dns_configs:
        run_command(cmd, desc)

def optimize_windows_network():
    print("\n" + "="*50)
    print("  OPTIMIZANDO RED WINDOWS")
    print("="*50)
    
    optimizations = [
        ("netsh interface tcp set global chimney=enabled", "Activar TCP Chimney"),
        ("netsh interface tcp set global dca=enabled", "Activar DCA"),
        ("netsh interface tcp set global netdma=enabled", "Activar NetDMA"),
        ("netsh interface tcp set global customsettings=enable", "Optimizaciones personalizadas"),
        ("netsh interface tcp set global autotuninglevel=experimental", "Auto-tuning experimental"),
        ("netsh winsock set default all", "Restablecer WINSOCK"),
        ("netsh int ip reset c:\\log.txt", "Restablecer TCP/IP"),
    ]
    
    for cmd, desc in optimizations:
        run_command(cmd, desc)

def optimize_mtu():
    print("\n" + "="*50)
    print("  OPTIMIZANDO MTU")
    print("="*50)
    
    run_command("netsh interface ipv4 set subinterface \"Ethernet\" mtu=1492 store=active", "MTU 1492 (Ethernet)")

def optimize_dns_cache():
    print("\n" + "="*50)
    print("  LIMPIANDO CACHE DNS")
    print("="*50)
    
    commands = [
        ("ipconfig /flushdns", "Limpiar cache DNS"),
        ("ipconfig /release", "Liberar DHCP"),
        ("ipconfig /renew", "Renovar DHCP"),
    ]
    
    for cmd, desc in commands:
        run_command(cmd, desc)

def optimize_wifi():
    print("\n" + "="*50)
    print("  OPTIMIZANDO WIINDOWS PARA WIFI")
    print("="*50)
    
    optimizations = [
        ("netsh wlan set profileparameter name=* pmf=required", "PMF requerido"),
        ("netsh wlan set profileparameter name=* fips=140-2", "FIPS 140-2"),
    ]
    
    for cmd, desc in optimizations:
        run_command(cmd, desc)

def check_network_status():
    print("\n" + "="*50)
    print("  ESTADO DE RED ACTUAL")
    print("="*50)
    
    commands = [
        ("ipconfig /all", "Configuracion IP completa"),
    ]
    
    for cmd, desc in commands:
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            output = result.stdout
            
            print(f"\n--- {desc} ---")
            for line in output.split('\n'):
                if any(x in line for x in ['IPv4', 'Subnet', 'Gateway', 'DNS', 'DHCP', 'Physical']):
                    print(line)
        except Exception as e:
            print(f"[X] Error: {e}")

def set_registry_optimizations():
    print("\n" + "="*50)
    print("  OPTIMIZANDO REGISTRY (requiere administrador)")
    print("="*50)
    
    reg_keys = [
        (r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "DefaultTTL", "64"),
        (r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "TcpTimedWaitDelay", "30"),
        (r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "MaxUserPort", "65534"),
    ]
    
    for key, name, value in reg_keys:
        cmd = f'reg add "{key}" /v {name} /t REG_DWORD /d {value} /f'
        run_command(cmd, f"Establecer {name}={value}")

def main():
    print("="*50)
    print("  OPTIMIZADOR AVANZADO DE RED")
    print("  Para Windows")
    print("="*50)
    
    print("\n[!] ADVERTENCIA: Algunos cambios pueden requerir reinicio.")
    print("[!] Ejecuta este script como Administrador.\n")
    
    print("[*] Ejecutando optimizaciones automaticamente...")
    
    check_network_status()
    
    optimize_dns_cache()
    
    optimize_dns()
    
    optimize_mtu()
    
    optimize_windows_network()
    
    optimize_wifi()
    
    set_registry_optimizations()
    
    print("\n" + "="*50)
    print("  OPTIMIZACIONES COMPLETADAS")
    print("="*50)
    
    print("\n[INFO] Recomendaciones finales:")
    print("   1. Reinicia tu computadora para aplicar todos los cambios")
    print("   2. Reinicia el router (apagalo y encendelo)")
    print("   3. Cambia el canal del WiFi en el router a uno libre")
    print("   4. Usa 5GHz si esta disponible")
    print("   5. Actualiza el firmware del router")
    print("\n[CONFIG] Para entrar al router: http://192.168.80.1")
    print("="*50)

if __name__ == "__main__":
    main()