# log_si.py
import logging
from elasticsearch import Elasticsearch

logging.basicConfig(filename='security_logs.log', level=logging.INFO, format='%(asctime)s %(message)s')

def log_anomaly(packet_features, anomaly_score):
    log_message = f"Anomali tespit edildi! Kaynak: {packet_features[0]}, Hedef: {packet_features[1]}, Skor: {anomaly_score}"
    logging.info(log_message)

def send_log_to_si(system_log):
    es = Elasticsearch(['http://localhost:9200'])
    es.index(index='security_logs', body={'log_entry': system_log})
