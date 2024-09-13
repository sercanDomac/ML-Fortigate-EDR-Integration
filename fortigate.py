# fortigate.py
import requests

FORTIGATE_URL = "https://your-fortigate-ip/api/v2"
API_KEY = "your-api-key"

def block_ip_with_fortigate(ip_address):
    url = f"{FORTIGATE_URL}/monitor/firewall/policy"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "action": "deny",
        "srcaddr": [{"name": ip_address}],
        "dstaddr": [{"name": "all"}],
        "service": [{"name": "ALL"}],
        "schedule": "always"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"IP adresi {ip_address} Fortigate tarafından engellendi.")
    else:
        print(f"Fortigate IP engelleme başarısız: {response.text}")
