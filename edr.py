# edr.py
import subprocess

def analyze_endpoint_with_edr(ip_address):
    try:
        subprocess.run(['edr-tool', '--analyze', ip_address])
        print(f"{ip_address} adresinde EDR analizi başlatıldı.")
    except Exception as e:
        print(f"EDR analizi başarısız oldu: {e}")
