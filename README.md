# 📋 Portale Circolari - Studio Commerciale Fiorella Bernardo

Portale web statico per la pubblicazione e consultazione delle circolari ufficiali dello Studio Commerciale Fiorella Bernardo.

## 🌐 Sito Pubblicato

Il sito è pubblicato su **GitHub Pages** e accessibile all'indirizzo:
[https://studiobf.github.io/circolari-aziendali/](https://studiobf.github.io/circolari-aziendali/)

## 🏗️ Struttura del Progetto

```
circolari-aziendali/
├── index.html                          # Homepage
├── circolari.json                      # Database circolari (aggiorna qui!)
├── circolari/
│   └── index.html                      # Viewer per le singole circolari
├── assets/
│   └── logo vettoriale.svg             # Logo dello studio
└── README.md
```

## ✨ Caratteristiche

- **Design Moderno e Responsive**: Interfaccia elegante ottimizzata per desktop e mobile.
- **Caricamento Dinamico**: Le circolari vengono generate automaticamente leggendo il file `circolari.json`.
- **Ricerca Live**: Filtro istantaneo per titolo e contenuto.
- **Archivio Storico**: Organizzazione automatica per anno.
- **Paginazione**: Navigazione ottimizzata con 5 elementi per pagina.
- **Facile Manutenzione**: Aggiungi nuove circolari modificando solo un file JSON.
- **Integrazione Social**: Collegamenti diretti ai canali Telegram e WhatsApp.
- **Mappa Interattiva**: Localizzazione ufficio con Google Maps integrato.

## 📝 Come Aggiungere una Nuova Circolare

Il sistema è interamente guidato dai dati. Non è necessario creare file HTML.

### 1. Modifica il File `circolari.json`

Aggiungi un nuovo oggetto all'inizio dell'array nel file `circolari.json`.

Ecco la struttura di base:

```json
{
    "id": "titolo-univoco-url",
    "title": "Titolo della Circolare",
    "subtitle": "Sottotitolo esplicativo",
    "ref": "Rif. Normativo",
    "tag": "Tipo Documento",
    "target_audience": "Pubblico di riferimento",
    "description": "Breve descrizione per l'anteprima",
    "date": "25 Nov 2025",
    "day": "25",
    "month_year": "Nov 2025",
    "category": "Fiscale",
    "content": [
        {
            "type": "paragraph",
            "text": "Testo introduttivo...",
            "style": "lead"
        },
        {
            "type": "separator"
        },
        {
            "type": "section",
            "title": "Titolo Sezione",
            "number": "1",
            "blocks": [
                {
                    "type": "paragraph",
                    "text": "Testo del paragrafo."
                },
                {
                    "type": "list",
                    "items": [
                        { "highlight": "Punto 1", "text": "Dettaglio punto 1" },
                        { "highlight": "Punto 2", "text": "Dettaglio punto 2" }
                    ]
                }
            ]
        }
    ]
}
```

### Tipi di Blocchi Supportati

- **paragraph**: Paragrafo di testo semplice. Opzionale `style: "lead"` per il testo introduttivo.
- **separator**: Linea divisoria orizzontale.
- **section**: Una sezione numerata che può contenere altri blocchi (`blocks`).
- **list**: Lista puntata. Ogni item ha `highlight` (grassetto) e `text`.
- **grid**: Griglia di card colorate (utile per evidenziare rischi o punti chiave).

### 2. Pubblica su GitHub

```bash
git add circolari.json
git commit -m "Aggiungi nuova circolare: [titolo]"
git push origin main
```

La circolare sarà automaticamente visibile sul sito entro pochi minuti!

## 🧪 Test Locale

Per testare il sito localmente, avvia un server HTTP (necessario per caricare il JSON):

```bash
# Con Python 3
python -m http.server 8000

# Oppure con Node.js (se installato)
npx http-server -p 8000
```

Apri il browser su `http://localhost:8000`

> **Nota**: Non aprire direttamente `index.html` dal file system, altrimenti le circolari non verranno caricate (errore CORS).

## 🎨 Tecnologie Utilizzate

- **HTML5** - Struttura semantica
- **Tailwind CSS** (via CDN) - Styling moderno e responsive
- **Alpine.js** (via CDN) - Gestione stato e reattività
- **GitHub Pages** - Hosting gratuito

## 🔧 Configurazione GitHub Pages

1. Vai su **Settings** > **Pages** del repository
2. Source: **Deploy from a branch**
3. Branch: **main** / Cartella: **/ (root)**
4. Salva

## 📞 Contatti

**Studio Commerciale Fiorella Bernardo**  
Corso San Benedetto, 170  
87022 Cetraro (CS)

- 📞 Tel: 0982 971430
- 📱 Cel: 393 987 9566
- 📠 Fax: 0982 531061
- ✉️ Email: bernardo.fiorella@gmail.com
- 📧 PEC: bernardo.fiorella@pec.it

## 🛡️ Funzionalità Admin & Bot Telegram

Il sito include una modalità amministratore nascosta per facilitare la pubblicazione delle circolari sul canale Telegram ufficiale.

### Modalità Admin
- **Attivazione**: Clicca 5 volte rapidamente sul logo dello studio nella homepage.
- **Indicatore**: Un'icona a forma di scudo verde apparirà nella barra di navigazione quando la modalità è attiva.
- **Funzioni**: Nelle pagine delle singole circolari apparirà il pulsante **"Pubblica"**.

### Bot Telegram (FioberBot)
Il sistema include uno script Python (`telegram_publisher.py`) per inviare le circolari ai canali Telegram.

**Avvio e Automazione:**

1.  **Avvio Manuale (Debug)**: Usa `Avvia Bot.bat`. Apre una finestra nera dove puoi vedere i log e verificare che tutto funzioni. Utile per testare.
2.  **Avvio Silente (Background)**: Usa `FioberBot_Background.vbs`.
    *   Avvia il bot senza finestre visibili.
    *   Per farlo partire all'accensione del PC:
        1.  Premi `Windows + R`, scrivi `shell:startup` e invio.
        2.  Copia il file `FioberBot_Background.vbs` in questa cartella.

**Requisiti:**
- Python installato.
- File `config_secrets.json` configurato con Token e ID dei canali.

---

© 2025 Studio Commerciale Fiorella Bernardo - Tutti i diritti riservati
