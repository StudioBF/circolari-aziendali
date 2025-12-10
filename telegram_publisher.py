import urllib.request
import urllib.parse
import json
import time
import ssl
import sys
import os

# CONFIGURAZIONE INIZIALE
CONFIG_FILE = "config_secrets.json"
BASE_SITE_URL = "https://studiobf.github.io/circolari-aziendali" 

# GLOBALS
PENDING_CIRCULAR = None  # To store the circular waiting for confirmation

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"❌ ERRORE CRITICO: File {CONFIG_FILE} non trovato!")
        print("Crea il file con TOKEN, CHANNEL_ID e AUTHORIZED_USERS.")
        sys.exit(1)
    
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Errore caricamento {CONFIG_FILE}: {e}")
        sys.exit(1)

# CARICO LA CONFIGURAZIONE
config = load_config()
TOKEN = config.get("TOKEN")
CHANNEL_ID = config.get("CHANNEL_ID")
AUTHORIZED_USERS = config.get("AUTHORIZED_USERS", [])

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def make_request(method, params=None):
    url = f"{BASE_URL}/{method}"
    if params:
        data = urllib.parse.urlencode(params).encode('utf-8')
        req = urllib.request.Request(url, data=data)
    else:
        req = urllib.request.Request(url)
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Errore richiesta {method}: {e}")
        return None

def load_circular_by_id(target_id):
    try:
        with open('circolari.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for circular in data:
                if circular.get('id') == target_id:
                    return circular
    except Exception as e:
        print(f"Errore lettura circolari.json: {e}")
    return None

def format_message(c):
    link = f"{BASE_SITE_URL}/circolari/index.html?id={c['id']}"
    msg = f"📢 *Nuova Circolare - Studio Bernardo*\n\n"
    msg += f"📄 *{c['title']}*\n"
    if c.get('subtitle'):
        msg += f"_{c['subtitle']}_\n"
    msg += f"\n{c.get('description', '')}\n\n"
    msg += f"👇 *Leggi l'approfondimento:*\n{link}\n\n"
    tag = c.get('tag', 'News').replace(" ", "")
    msg += f"#StudioBernardo #Aggiornamento #{tag}"
    return msg

def send_message(target_chat_id, text):
    params = {
        "chat_id": target_chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": "false"
    }
    result = make_request("sendMessage", params)
    if not result or not result.get("ok"):
        print("Errore Markdown. Riprovo senza formattazione...")
        del params["parse_mode"]
        make_request("sendMessage", params)
    return result

def main():
    global PENDING_CIRCULAR

    print(f"--- FIOBER BOT AVVIATO (Secure Mode) ---")
    print(f"Canale: {CHANNEL_ID}")
    print(f"Utenti Admin: {AUTHORIZED_USERS}")
    print(f"In attesa di comandi...")

    offset = 0
    
    while True:
        try:
            updates = make_request("getUpdates", {"offset": offset, "timeout": 30})
            
            if updates and updates.get("ok"):
                for update in updates.get("result", []):
                    offset = update["update_id"] + 1
                    
                    if "message" in update:
                        msg = update["message"]
                        user_id = msg["from"]["id"]
                        text = msg.get("text", "")
                        
                        if not text:
                            continue

                        # AUTH CHECK
                        if AUTHORIZED_USERS and user_id not in AUTHORIZED_USERS:
                            print(f"⛔ UTENTE NON AUTORIZZATO: {user_id}")
                            send_message(user_id, f"⛔ Non autorizzato. ID: `{user_id}`")
                            continue
                        
                        # 1. INIT PUBLISH
                        if text.startswith("/start publish_"):
                            circular_id = text.replace("/start publish_", "").strip()
                            print(f"Richiesta Anteprima ID: {circular_id}")
                            
                            circular = load_circular_by_id(circular_id)
                            if circular:
                                formatted_msg = format_message(circular)
                                PENDING_CIRCULAR = formatted_msg
                                
                                # Send PREVIEW to user
                                send_message(user_id, 
                                             f"⚠️ *ANTEPRIMA DI STAMPA*\n\n{formatted_msg}")
                                send_message(user_id, 
                                             "Digita */confirm* per pubblicare sul Canale.\nDigita */cancel* per annullare.")
                            else:
                                send_message(user_id, f"❌ Errore: Circolare '{circular_id}' non trovata.")
                            continue

                        # 2. CONFIRM
                        if text == "/confirm":
                            if PENDING_CIRCULAR:
                                print("Pubblicazione in corso...")
                                send_message(CHANNEL_ID, PENDING_CIRCULAR)
                                send_message(user_id, "✅ *Circolare Pubblicata con Successo!*")
                                PENDING_CIRCULAR = None
                            else:
                                send_message(user_id, "⚠️ Nessuna circolare in attesa. Invia prima una richiesta dal sito.")
                            continue

                        # 3. CANCEL
                        if text == "/cancel":
                            if PENDING_CIRCULAR:
                                PENDING_CIRCULAR = None
                                send_message(user_id, "❌ Operazione annullata.")
                            else:
                                send_message(user_id, "Nessuna operazione da annullare.")
                            continue

                        # Default
                        if text == "/start":
                            send_message(user_id, "Ciao Admin! Usa il sito per inviare comandi.")

            time.sleep(1)

        except KeyboardInterrupt:
            print("\nBot fermato.")
            sys.exit(0)
        except Exception as e:
            print(f"Errore loop: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
