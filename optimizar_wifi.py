#!/usr/bin/env python3
import subprocess
import time
import re
import socket
import requests
import json

def get_wifi_networks():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'networks', 'mode=bssid'], 
                              capture_output=True, text=True, encoding='utf-8', errors='ignore')
        networks = {}
        current_ssid = None
        
        for line in result.stdout.split('\n'):
            if 'SSID' in line and 'BSSID' not in line:
                current_ssid = line.split(':')[1].strip()
                if current_ssid not in networks:
                    networks[current_ssid] = {'signal': 0, 'canal': None, 'auth': None}
            elif 'Signal' in line and current_ssid:
                signal = line.split(':')[1].strip().replace('%', '')
                networks[current_ssid]['signal'] = int(signal)
            elif 'Channel' in line and current_ssid:
                canal = line.split(':')[1].strip()
                networks[current_ssid]['canal'] = canal
            elif 'Authentication' in line and current_ssid:
                auth = line.split(':')[1].strip()
                networks[current_ssid]['auth'] = auth
                
        return networks
    except Exception as e:
        print(f"Error al escanear redes: {e}")
        return {}

def analyze_channels(networks):
    channel_usage = {}
    for ssid, data in networks.items():
        if data['canal']:
            canal = int(data['canal'])
            if canal not in channel_usage:
                channel_usage[canal] = 0
            channel_usage[canal] += 1
    return channel_usage

def get_current_wifi_info():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], 
                              capture_output=True, text=True, encoding='utf-8', errors='ignore')
        
        info = {}
        for line in result.stdout.split('\n'):
            if 'SSID' in line and 'BSSID' not in line:
                info['ssid'] = line.split(':')[1].strip()
            elif 'Signal' in line:
                info['signal'] = line.split(':')[1].strip()
            elif 'Channel' in line:
                info['channel'] = line.split(':')[1].strip()
            elif 'Authentication' in line:
                info['auth'] = line.split(':')[1].strip()
            elif 'Transmit rate' in line:
                info['tx_rate'] = line.split(':')[1].strip()
            elif 'Receive rate' in line:
                info['rx_rate'] = line.split(':')[1].strip()
            elif 'Radio type' in line:
                info['radio_type'] = line.split(':')[1].strip()
        return info
    except Exception as e:
        print(f"Error al obtener información WiFi: {e}")
        return {}

def test_latency(host='8.8.8.8', count=5):
    try:
        result = subprocess.run(['ping', '-n', str(count), host], 
                              capture_output=True, text=True, encoding='utf-8', errors='ignore')
        
        for line in result.stdout.split('\n'):
            if 'Average' in line or 'promedio' in line:
                match = re.search(r'(\d+)ms', line)
                if match:
                    return int(match.group(1))
        return None
    except Exception as e:
        print(f"Error en test de latencia: {e}")
        return None

def test_internet_speed():
    print("\n--- Test de Velocidad ---")
    print("Para un test completo, visita: https://speedtest.net")
    print("o instala Speedtest CLI: pip install speedtest-cli")
    print("Luego ejecuta: speedtest")
    return None

def optimize_windows_network():
    print("\n=== OPTIMIZANDO CONFIGURACIÓN DE RED WINDOWS ===\n")
    
    optimizations = [
        ("netsh interface tcp set global autotuninglevel=disabled", "Desactivar auto-tuning"),
        ("netsh interface tcp set global rss=disabled", "Desactivar RSS"),
        ("netsh wlan set profileparameter name=* radio=any", "Habilitar todas las bandas"),
    ]
    
    for cmd, desc in optimizations:
        try:
            subprocess.run(cmd.split(), capture_output=True, timeout=10)
            print(f"[OK] {desc}")
        except:
            print(f"[X] {desc} (no disponible)")

def print_recommendations(current_info, networks, channel_usage):
    print("\n" + "="*50)
    print("       RECOMENDACIONES DE OPTIMIZACIÓN")
    print("="*50)
    
    print("\n[STATUS] ESTADO ACTUAL:")
    if current_info:
        print(f"   Red WiFi: {current_info.get('ssid', 'N/A')}")
        print(f"   Señal: {current_info.get('signal', 'N/A')}")
        print(f"   Canal: {current_info.get('channel', 'N/A')}")
        print(f"   Velocidad TX: {current_info.get('tx_rate', 'N/A')}")
        print(f"   Tipo: {current_info.get('radio_type', 'N/A')}")
    
    print("\n[CHANNELS] CANALES MAS CONGESTIONADOS:")
    if channel_usage:
        sorted_channels = sorted(channel_usage.items(), key=lambda x: x[1], reverse=True)
        for canal, count in sorted_channels[:5]:
            print(f"   Canal {canal}: {count} redes")
    
    print("\n[RECOMENDACIONES]:")
    print("   1. Cambia el canal a uno menos congestionado (1, 6, 11 son comunes)")
    print("   2. Si tu router supporta 5GHz, úsalo (menos interferencias)")
    print("   3. Ubica el router en un lugar central, elevado, sin obstáculos")
    print("   4. Aleja el router de microondas, teléfonos inalámbricos")
    print("   5. Considera un repetidor WiFi o mesh si la señal es débil")
    
    print("\n[CONFIG] PARA MEJORAR EN EL ROUTER (192.168.80.1):")
    print("   - Busca 'Wireless' o 'WiFi' > 'Channel' > Selecciona canal menos usado")
    print("   - Activa 'Band Steering' si está disponible")
    print("   - Configura 'Transmit Power' al máximo")
    print("   - Usa WiFi 5GHz si está disponible")

def main():
    print("="*50)
    print("   OPTIMIZADOR DE SEÑAL WIFI - CLARO")
    print("="*50)
    
    print("\n[+] Escaneando redes WiFi cercanas...")
    networks = get_wifi_networks()
    
    print(f"   {len(networks)} redes encontradas")
    
    print("\n[*] Analizando canales...")
    channel_usage = analyze_channels(networks)
    
    print("\n[*] Obteniendo informacion de tu conexion...")
    current_info = get_current_wifi_info()
    
    print("\n[*] Testeando latencia...")
    latency = test_latency()
    
    print("\n--- Resultado de Latencia ---")
    if latency:
        print(f"Latencia promedio: {latencia}ms")
        if latency < 50:
            print("[OK] Excelente latencia")
        elif latency < 100:
            print("[OK] Buena latencia")
        else:
            print("⚠ Latencia alta - considera optimizar")
    
    test_internet_speed()
    
    optimize_windows_network()
    
    print_recommendations(current_info, networks, channel_usage)
    
    print("\n" + "="*50)
    print("FINALIZADO. Para cambios en el router, accede a:")
    print("   http://192.168.80.1")
    print("="*50)

if __name__ == "__main__":
    main()
