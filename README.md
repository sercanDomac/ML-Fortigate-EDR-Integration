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

Dosya Yapısı
main.py: Projeyi çalıştıran ana Python scripti.

fortigate.py: Fortigate ile IP engelleme işlemlerini yöneten script.

edr.py: EDR sistemine uç nokta analizlerini başlatan script.

ml_model.py: Makine öğrenimi ile anomali tespiti yapan script.

log_si.py: Loglama ve SIEM entegrasyonunu yapan script.

requirements.txt: Gerekli Python kütüphanelerini belirten dosya.

Katkıda Bulunma
Her türlü geri bildirim, hata raporu veya katkıda bulunma tekliflerinizi memnuniyetle karşılıyorum. Lütfen GitHub Issues bölümünden sorunlarınızı bildirin veya katkıda bulunmak için bir pull request oluşturun.

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.

İletişim
Sorularınız veya işbirliği teklifleriniz için benimle iletişime geçebilirsiniz:

E-posta
sercandomac@gmail.com
