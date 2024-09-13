# ML-Fortigate-EDR-Integration

# APT Detection Project

Bu proje, APT (Advanced Persistent Threat) saldırılarını makine öğrenimi, Fortigate, ve EDR entegrasyonları ile tespit etmeyi amaçlar. Gerçek zamanlı ağ trafiği izlenir, anomaliler tespit edilir ve saldırgan IP'leri engellemek için otomatik işlemler başlatılır.

## Gereksinimler

- Python 3.x
- Fortigate API erişimi
- EDR aracı (örneğin, edr-tool)
- Elasticsearch (SIEM için)

## Kurulum

1. Projeyi klonlayın:
   ```bash
   git clone https://github.com/yourusername/apt-detection-project.git
   cd apt-detection-project


Gerekli Python kütüphanelerini yükleyin:

pip install -r requirements.txt
Fortigate ve EDR API anahtarlarınızı fortigate.py dosyasına ekleyin.
