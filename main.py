# main.py
from ml_model import train_autoencoder, detect_anomalies_with_autoencoder
from fortigate import block_ip_with_fortigate
from edr import analyze_endpoint_with_edr
from log_si import log_anomaly, send_log_to_si

# Eğitim ve anomali tespiti için veriler
new_packet_features = [0.5, 0.3, 1.0, 0.6, 0.4, 0.8]
X_train = np.random.rand(100, 6)  # Örnek eğitim verisi

# Model eğitimi
model = train_autoencoder(X_train)

# Anomali tespiti
anomaly_score = detect_anomalies_with_autoencoder(model, new_packet_features)

# Süreci başlatma
if anomaly_score > 0.1:
    src_ip = "192.168.1.10"
    block_ip_with_fortigate(src_ip)
    analyze_endpoint_with_edr(src_ip)
    log_anomaly(new_packet_features, anomaly_score)
    send_log_to_si(f"APT saldırısı tespit edildi: IP {src_ip}, Skor: {anomaly_score}")
else:
    print("Normal trafik.")
