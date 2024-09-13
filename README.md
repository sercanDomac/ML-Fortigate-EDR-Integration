APT Detection Solution
Proje Açıklaması
APT Detection Solution, gelişmiş sürekli tehditleri (APT'ler) tespit etmek ve savunmak için makine öğrenimi, Fortigate güvenlik duvarı entegrasyonu ve EDR (Endpoint Detection and Response) sistemlerini bir araya getiren kapsamlı bir güvenlik çözümüdür. Bu proje, gerçek zamanlı ağ trafiğini izleyerek anormal davranışları tespit eder, şüpheli IP adreslerini otomatik olarak engeller ve uç nokta güvenliğini sağlar.

Özellikler
Makine Öğrenimi ile Anomali Tespiti: Autoencoder tabanlı bir model kullanarak ağ trafiğindeki anomalleri tespit eder.
Fortigate Entegrasyonu: Tespit edilen şüpheli IP adreslerini Fortigate güvenlik duvarı aracılığıyla engeller.
EDR Analizi: EDR sistemi ile uç noktalarda şüpheli işlemleri analiz eder ve izole eder.
SIEM Loglama: Olayları loglar ve SIEM sistemine gönderir, böylece detaylı analiz ve raporlama yapılır.
Kurulum ve Kullanım
Gereksinimler
Python 3.x
Fortigate API erişimi
EDR aracı (örneğin, edr-tool)
Elasticsearch (SIEM için)

---------
git clone https://github.com/sercanDomac/ML-Fortigate-EDR-Integration
cd apt-detection-solution
---------

pip install -r requirements.txt
----------
