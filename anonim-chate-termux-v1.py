import socket
import threading
import json
import os
import sys
from datetime import datetime

# --- AYARLAR ---
SERVER_IP = "fi5.bot-hosting.net"
PORT = 22027
CONFIG_FILE = "settings.json"

# --- RENKLER (Termux Uyumlu) ---
GRI = "\033[90m"
SARI = "\033[93m"
BEYAZ = "\033[97m"
CYAN = "\033[96m"
YESIL = "\033[92m"
KIRMIZI = "\033[91m"
SIFIRLA = "\033[0m"

def ayarları_yukle():
    """JSON dosyasından kullanıcı adını çeker."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f).get("user_name")
        except: return None
    return None

def ayarları_kaydet(name):
    """Kullanıcı adını JSON dosyasına kaydeder."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"user_name": name}, f, ensure_ascii=False, indent=4)

def receive_messages(client_socket):
    """Sunucudan gelen mesajları dinleyen thread."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"\n{KIRMIZI}[!] Sunucu bağlantısı kesildi.{SIFIRLA}")
                break
            
            # Gelen mesajı bastırırken mevcut input satırını temizle
            sys.stdout.write("\r\033[K" + message + "\n")
            sys.stdout.flush()
        except:
            break

def start_client():
    # 1. Kullanıcı Adı Kontrolü
    user_name = ayarları_yukle()
    if not user_name:
        os.system('clear')
        user_name = input(f"{SARI}[?] Kullanıcı adınız ne olsun? {SIFIRLA}").strip()
        user_name = user_name or "Anonim"
        ayarları_kaydet(user_name)

    # 2. Sunucuya Bağlanma
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_IP, PORT))
        # Sunucuya ismi bildir
        client.send(f"config-name:{user_name}".encode('utf-8'))
        
        os.system('clear')
        print(f"{YESIL}┌────────────────────────────────────────────────┐")
        print(f"│      TERMUX SOHBET BAĞLANDI - HOŞ GELDİN!      │")
        print(f"└────────────────────────────────────────────────┘{SIFIRLA}")
        print(f"{GRI}Komutlar: create-room:limit | join ID | close-room | exit{SIFIRLA}\n")
    except Exception as e:
        print(f"{KIRMIZI}[!] Bağlantı Hatası: {e}{SIFIRLA}")
        return

    # 3. Mesaj Dinleme Thread'ini Başlat
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    # 4. Mesaj Gönderme Döngüsü
    while True:
        try:
            msg = input(f"{SIFIRLA}")
            
            if not msg.strip():
                sys.stdout.write("\033[F\033[K") # Boş satırı sil
                continue
            
            if msg.lower() == "exit":
                break
            
            # İsim değiştirme komutuysa yerel ayarı da güncelle
            if msg.startswith("config-name:"):
                try:
                    new_name = msg.split(":")[1]
                    ayarları_kaydet(new_name)
                    user_name = new_name
                except: pass

            # Mesajı sunucuya gönder (Hata yakalamalı)
            try:
                client.send(msg.encode('utf-8'))
            except (BrokenPipeError, ConnectionResetError):
                print(f"{KIRMIZI}[!] HATA: Mesaj gönderilemedi, bağlantı koptu.{SIFIRLA}")
                break

            # Kendi ekranında şık format: Saat | İsim: Mesaj *
            sys.stdout.write("\033[F\033[K") # Yazdığın input satırını sil
            saat_ayrac = f"{GRI}{datetime.now().strftime('%H:%M %d/%m')}{SARI} |{SIFIRLA}"
            print(f"{saat_ayrac} {CYAN}{user_name}:{SIFIRLA} {BEYAZ}{msg} {YESIL}*{SIFIRLA}")
            
        except KeyboardInterrupt:
            break

    client.close()
    print(f"\n{KIRMIZI}Çıkış yapıldı.{SIFIRLA}")

if __name__ == "__main__":
    start_client()
