# IMPORTS
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
PENDING_CIRCULAR = None  # Stores the circular object awaiting confirmation

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"❌ ERRORE CRITICO: File {CONFIG_FILE} non trovato!")
        print("Crea il file con TOKEN, OFFICIAL_CHANNEL_ID e AUTHORIZED_USERS.")
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
OFFICIAL_CHANNEL_ID = config.get("OFFICIAL_CHANNEL_ID") or config.get("CHANNEL_ID")
TEST_CHANNEL_ID = config.get("TEST_CHANNEL_ID")
AUTHORIZED_USERS = config.get("AUTHORIZED_USERS", [])

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def make_request(method, params=None):
    url = f"{BASE_URL}/{method}"
    if params:
        # JSON Encoding for complex objects like reply_markup
        req = urllib.request.Request(url, method="POST")
        req.add_header('Content-Type', 'application/json')
        data = json.dumps(params).encode('utf-8')
    else:
        req = urllib.request.Request(url)
        data = None
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        with urllib.request.urlopen(req, data=data, context=ctx) as response:
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

def format_message_body(c):
    # Formats the message text WITHOUT the link (since we use a button)
    msg = f"📢 *Nuova Circolare - Studio Bernardo*\n\n"
    msg += f"📄 *{c['title']}*\n"
    if c.get('subtitle'):
        msg += f"_{c['subtitle']}_\n"
    msg += f"\n{c.get('description', '')}\n\n"
    
    tag = c.get('tag', 'News').replace(" ", "")
    msg += f"#StudioBernardo #Aggiornamento #{tag}"
    return msg

def get_circular_link(c):
    return f"{BASE_SITE_URL}/circolari/index.html?id={c['id']}"

def send_message(target_chat_id, text, reply_markup=None):
    params = {
        "chat_id": target_chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": "true" 
    }
    if reply_markup:
        params["reply_markup"] = reply_markup

    result = make_request("sendMessage", params)
    
    # Fallback if Markdown fails
    if not result or not result.get("ok"):
        print("Errore Markdown. Riprovo senza formattazione...")
        del params["parse_mode"]
        make_request("sendMessage", params)
    return result

def answer_callback(callback_id, text=""):
    make_request("answerCallbackQuery", {"callback_query_id": callback_id, "text": text})

def delete_message(chat_id, message_id):
    make_request("deleteMessage", {"chat_id": chat_id, "message_id": message_id})

def publish_to_channel(channel_id, circular):
    link = get_circular_link(circular)
    channel_markup = {
        "inline_keyboard": [[
            {"text": "🔗 Leggi l'approfondimento", "url": link}
        ]]
    }
    body = format_message_body(circular)
    send_message(channel_id, body, channel_markup)

def main():
    global PENDING_CIRCULAR

    print(f"--- FIOBER BOT AVVIATO (Dual Channel Mode) ---")
    print(f"Canale Ufficiale: {OFFICIAL_CHANNEL_ID}")
    print(f"Canale Test: {TEST_CHANNEL_ID}")
    print(f"In attesa di comandi...")

    offset = 0
    
    while True:
        try:
            updates = make_request("getUpdates", {"offset": offset, "timeout": 30})
            
            if updates and updates.get("ok"):
                for update in updates.get("result", []):
                    offset = update["update_id"] + 1
                    
                    # 1. HANDLE CALLBACK QUERIES (Buttons)
                    if "callback_query" in update:
                        cb = update["callback_query"]
                        cb_id = cb["id"]
                        data = cb["data"]
                        user_id = cb["from"]["id"]
                        chat_id = cb["message"]["chat"]["id"]
                        msg_id = cb["message"]["message_id"]

                        if AUTHORIZED_USERS and user_id not in AUTHORIZED_USERS:
                            answer_callback(cb_id, "⛔ Non autorizzato")
                            continue

                        # PUBLISH OFFICIAL
                        if data == "publish_official":
                            if PENDING_CIRCULAR and OFFICIAL_CHANNEL_ID:
                                publish_to_channel(OFFICIAL_CHANNEL_ID, PENDING_CIRCULAR)
                                answer_callback(cb_id, "Pubblicato Ufficiale!")
                                send_message(chat_id, "✅ *Pubblicato su Canale UFFICIALE*")
                                delete_message(chat_id, msg_id)
                                PENDING_CIRCULAR = None
                            else:
                                answer_callback(cb_id, "Errore: Canale non configurato o sessione scaduta")

                        # PUBLISH TEST
                        elif data == "publish_test":
                            if PENDING_CIRCULAR and TEST_CHANNEL_ID:
                                publish_to_channel(TEST_CHANNEL_ID, PENDING_CIRCULAR)
                                answer_callback(cb_id, "Pubblicato Test!")
                                send_message(chat_id, "✅ *Pubblicato su Canale TEST*")
                                delete_message(chat_id, msg_id)
                                PENDING_CIRCULAR = None
                            else:
                                answer_callback(cb_id, "Errore: Canale Test non configurato")
                        
                        # CANCEL
                        elif data == "cancel_publish":
                            PENDING_CIRCULAR = None
                            answer_callback(cb_id, "Annullato")
                            delete_message(chat_id, msg_id)
                            send_message(chat_id, "❌ Operazione annullata.")

                        continue

                    # 2. HANDLE TEXT MESSAGES
                    if "message" in update:
                        msg = update["message"]
                        user_id = msg["from"]["id"]
                        text = msg.get("text", "")
                        
                        if not text:
                            continue

                        # AUTH CHECK
                        if AUTHORIZED_USERS and user_id not in AUTHORIZED_USERS:
                            print(f"⛔ UTENTE NON AUTORIZZATO: {user_id}")
                            continue
                        
                        # PUBLISH REQUEST
                        if text.startswith("/start publish_"):
                            circular_id = text.replace("/start publish_", "").strip()
                            print(f"Richiesta ID: {circular_id}")
                            
                            circular = load_circular_by_id(circular_id)
                            if circular:
                                PENDING_CIRCULAR = circular
                                
                                body = format_message_body(circular)
                                
                                # Admin Buttons with DUAL CHANNEL choice
                                buttons = []
                                if OFFICIAL_CHANNEL_ID:
                                    buttons.append([{"text": "📢 Pubblica Ufficiale", "callback_data": "publish_official"}])
                                if TEST_CHANNEL_ID:
                                    buttons.append([{"text": "🧪 Pubblica Test", "callback_data": "publish_test"}])
                                buttons.append([{"text": "❌ Annulla", "callback_data": "cancel_publish"}])

                                admin_markup = {"inline_keyboard": buttons}
                                
                                send_message(user_id, body, admin_markup)
                            else:
                                send_message(user_id, f"❌ Errore: Circolare '{circular_id}' non trovata.")
                            continue

            time.sleep(1)

        except KeyboardInterrupt:
            print("\nBot fermato.")
            sys.exit(0)
        except Exception as e:
            print(f"Errore loop: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
