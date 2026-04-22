#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import json
import re

ROUTER_IP = "http://192.168.80.1"
USERNAME = "ClaroUsuario"
PASSWORD = "ClienteCLARO"

session = requests.Session()

def get_login_page():
    print("[*] Obteniendo pagina de login...")
    try:
        response = session.get(ROUTER_IP, timeout=10)
        print(f"[OK] Status: {response.status_code}")
        
        response2 = session.get(f"{ROUTER_IP}/api/captcha", timeout=10)
        print(f"[INFO] Captcha: {response2.status_code}")
        
        response3 = session.get(f"{ROUTER_IP}/api/session", timeout=10)
        print(f"[INFO] Session: {response3.status_code} - {response3.text[:200]}")
        
        response4 = session.get(f"{ROUTER_IP}/api/csrf", timeout=10)
        print(f"[INFO] CSRF: {response4.status_code} - {response4.text[:200]}")
        
        print(f"[INFO] Cookies despues: {dict(session.cookies)}")
        return response
    except Exception as e:
        print(f"[X] Error: {e}")
        return None

def login():
    print(f"[*] Intentando login como {USERNAME}...")
    
    login_approaches = [
        ({"username": USERNAME, "password": PASSWORD}, "/api/auth/login"),
        ({"username": USERNAME, "password": PASSWORD, "form": "login"}, "/user/auth"),
        ({"username": USERNAME, "password": PASSWORD, "Content-Type": "application/json"}, "/api/user/login"),
        ({"data": {"username": USERNAME, "password": PASSWORD}}, "/api/login"),
    ]
    
    for data, endpoint in login_approaches:
        try:
            response = session.post(f"{ROUTER_IP}{endpoint}", json=data, timeout=10)
            print(f"[INFO] {endpoint}: {response.status_code}")
            if response.status_code == 200:
                try:
                    result = response.json()
                    if result.get("success") or result.get("code") == 0:
                        print("[OK] Conectado al router")
                        return True
                except:
                    pass
                if "success" in response.text.lower() or "token" in response.text.lower():
                    print("[OK] Conectado al router")
                    return True
        except Exception as e:
            print(f"[X] {endpoint}: {e}")
            continue
    
    form_approaches = [
        ("username=" + USERNAME + "&password=" + PASSWORD, "/api/auth/login"),
    ]
    
    for data, endpoint in form_approaches:
        try:
            response = session.post(f"{ROUTER_IP}{endpoint}", data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=10)
            print(f"[INFO] Form {endpoint}: {response.status_code}")
            if response.status_code == 200:
                print("[OK] Conectado al router")
                return True
        except Exception as e:
            print(f"[X] {endpoint}: {e}")
            continue
    
    basic_auth_approaches = [
        "/api/auth/login",
        "/api/session/login",
        "/user/login",
    ]
    
    for endpoint in basic_auth_approaches:
        try:
            response = session.get(f"{ROUTER_IP}{endpoint}", auth=HTTPBasicAuth(USERNAME, PASSWORD), timeout=10)
            print(f"[INFO] Basic {endpoint}: {response.status_code}")
            if response.status_code == 200:
                print("[OK] Conectado al router")
                return True
        except Exception as e:
            print(f"[X] {endpoint}: {e}")
            continue
    
    print("[X] No se pudo conectar")
    return False

def get_status():
    print("[*] Obteniendo estado del router...")
    try:
        endpoints = [
            "/api/status",
            "/status",
            "/cgi-bin/status",
            "/api/device/status",
            "/api/deviceinfo",
            "/api/device/info",
            "/api/gpon/deviceinfo",
        ]
        
        for endpoint in endpoints:
            try:
                response = session.get(f"{ROUTER_IP}{endpoint}", timeout=5)
                if response.status_code == 200:
                    print(f"[OK] Endpoint encontrado: {endpoint}")
                    print(f"[INFO] Respuesta: {response.text[:800]}")
                    return response.text
            except:
                continue
        
        print("[X] No se encontro endpoint de status")
        return None
    except Exception as e:
        print(f"[X] Error: {e}")
        return None

def change_dns():
    print("[*] Cambiando DNS a Cloudflare...")
    try:
        endpoints = [
            "/api/dns/settings",
            "/api/network/dns",
            "/cgi-bin/dns",
            "/api/gpon/dns",
            "/api/wan/dns",
        ]
        
        dns_data = {
            "primary_dns": "1.1.1.1",
            "secondary_dns": "8.8.8.8"
        }
        
        for endpoint in endpoints:
            try:
                response = session.post(f"{ROUTER_IP}{endpoint}", json=dns_data, timeout=5)
                print(f"[INFO] {endpoint}: {response.status_code} - {response.text[:100]}")
                if response.status_code in [200, 201]:
                    print(f"[OK] DNS cambiado: {endpoint}")
                    return True
            except Exception as e:
                print(f"[X] {endpoint}: {e}")
                continue
        
        print("[X] No se pudo cambiar DNS")
        return False
    except Exception as e:
        print(f"[X] Error: {e}")
        return False

def change_wifi_channel():
    print("[*] Cambiando canal WiFi...")
    try:
        endpoints = [
            "/api/wireless/settings",
            "/api/wifi/channel",
            "/cgi-bin/wifi",
        ]
        
        wifi_data = {
            "channel": "11",
            "mode": "auto"
        }
        
        for endpoint in endpoints:
            try:
                response = session.post(f"{ROUTER_IP}{endpoint}", json=wifi_data, timeout=5)
                if response.status_code in [200, 201]:
                    print(f"[OK] Canal WiFi cambiado: {endpoint}")
                    return True
            except:
                continue
        
        print("[X] No se pudo cambiar canal WiFi")
        return False
    except Exception as e:
        print(f"[X] Error: {e}")
        return False

def scan_wifi_networks():
    print("[*] Escaneando redes WiFi...")
    try:
        response = session.get(f"{ROUTER_IP}/api/wireless/scan", timeout=30)
        if response.status_code == 200:
            print("[OK] Redes encontradas")
            try:
                networks = response.json()
                for net in networks.get("networks", [])[:10]:
                    print(f"  - {net.get('ssid')}: Canal {net.get('channel')}, Senal {net.get('signal')}%")
            except:
                print(f"[INFO] {response.text[:300]}")
            return True
    except Exception as e:
        print(f"[X] Error escaneando: {e}")
        return False

def reboot_router():
    print("[*] Solicitando reinicio del router...")
    try:
        response = session.post(f"{ROUTER_IP}/api/system/reboot", timeout=10)
        if response.status_code in [200, 201]:
            print("[OK] Reinicio solicitado")
            return True
    except Exception as e:
        print(f"[X] Error: {e}")
        return False

def get_router_info():
    print("[*] Obteniendo informacion del router...")
    try:
        response = session.get(f"{ROUTER_IP}/api/device/info", timeout=5)
        if response.status_code == 200:
            print(f"[INFO] {response.text[:500]}")
            return True
    except Exception as e:
        print(f"[X] Error: {e}")
        return False
    
    try:
        response = session.get(f"{ROUTER_IP}/cgi-bin/sysinfo", timeout=5)
        if response.status_code == 200:
            print(f"[INFO] {response.text[:500]}")
            return True
    except Exception as e:
        print(f"[X] Error: {e}")
        return False

def main():
    print("="*50)
    print("  OPTIMIZADOR DE ROUTER CLARO")
    print("="*50)
    
    if not get_login_page():
        print("\n[X] No se puede acceder al router")
        print("[INFO] Verifica que estas conectado al router")
        return
    
    if not login():
        print("\n[X] No se pudo login")
        print("[INFO] Las credenciales pueden haber cambiado")
        return
    
    get_router_info()
    
    get_status()
    
    scan_wifi_networks()
    
    change_dns()
    
    change_wifi_channel()
    
    print("\n" + "="*50)
    print("  RESUMEN")
    print("="*50)
    print("[INFO] Si los cambios no se aplicaron automaticamente,")
    print("      tendras que hacerlos manualmente en:")
    print(f"      {ROUTER_IP}")
    print("="*50)

if __name__ == "__main__":
    main()