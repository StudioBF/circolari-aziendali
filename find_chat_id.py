import requests
import time
import json

TOKEN = "PLACEHOLDER_TOKEN"
URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

def get_updates():
    print("Cerco messaggi recenti...")
    try:
        response = requests.get(URL)
        data = response.json()
        
        if not data.get('ok'):
            print(f"Errore API: {data}")
            return

        results = data.get('result', [])
        
        if not results:
            print("Nessun messaggio trovato. Assicurati di aver aggiunto il bot al canale e inviato un messaggio (es. 'test').")
            return

        print("\n--- TROVATI I SEGUENTI ID ---")
        found = False
        for update in results:
            # Check for channel post
            if 'channel_post' in update:
                chat = update['channel_post']['chat']
                print(f"CANALE: '{chat.get('title')}' | ID: {chat.get('id')} | Tipo: {chat.get('type')}")
                found = True
            # Check for my_chat_member (when bot is added to channel)
            elif 'my_chat_member' in update:
                chat = update['my_chat_member']['chat']
                print(f"CANALE (Evento Aggiunta): '{chat.get('title')}' | ID: {chat.get('id')}")
                found = True
            # Check for messages
            elif 'message' in update:
                chat = update['message']['chat']
                print(f"CHAT (Privata/Gruppo): '{chat.get('first_name', '')} {chat.get('title', '')}' | ID: {chat.get('id')} | Tipo: {chat.get('type')}")
                found = True
                
        if not found:
            print("Messaggi trovati ma nessun canale identificato chiaramente.")

    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    get_updates()
