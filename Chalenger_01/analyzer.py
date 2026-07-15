import sqlite3
from scapy.all import sniff, IP, TCP, UDP
from collections import Counter
import os

# Configuração do Banco de Dados SQLite
DB_NAME = "packets.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS traffic (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            src_ip TEXT,
            dst_ip TEXT,
            protocol TEXT,
            size INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_packet(src_ip, dst_ip, protocol, size):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO traffic (src_ip, dst_ip, protocol, size)
        VALUES (?, ?, ?, ?)
    ''', (src_ip, dst_ip, protocol, size))
    conn.commit()
    conn.close()

stats = {
    "total": 0,
    "protocols": Counter(),
    "src_ips": Counter(),
    "dst_ips": Counter()
}

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        size = len(packet)
        
        protocol = "OTHER"
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
            
        save_packet(src_ip, dst_ip, protocol, size)
        
        stats["total"] += 1
        stats["protocols"][protocol] += 1
        stats["src_ips"][src_ip] += 1
        stats["dst_ips"][dst_ip] += 1

def display_statistics():
    print("\n" + "="*40)
    print("ESTATÍSTICAS DE TRÁFEGO")
    print("="*40)
    print(f"Total de pacotes capturados: {stats['total']}")
    
    print("\nPacotes por Protocolo:")
    for proto, count in stats["protocols"].items():
        print(f" - {proto}: {count}")
        
    print("\nTop 5 IPs de Origem:")
    for ip, count in stats["src_ips"].most_common(5):
        print(f" - {ip}: {count} pacotes")
        
    print("\nTop 5 IPs de Destino:")
    for ip, count in stats["dst_ips"].most_common(5):
        print(f" - {ip}: {count} pacotes")
    print("="*40 + "\n")

if __name__ == "__main__":
    init_db()
    print("Iniciando captura de pacotes (Pressione Ctrl+C para parar e ver os resultados)...")
    try:
        # Timeout de 60s
        sniff(prn=process_packet, store=False, timeout=60) 
    except KeyboardInterrupt:
        print("\nCaptura interrompida pelo usuário.")
    finally:
        display_statistics()