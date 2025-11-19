# 📋 Portale Circolari - Studio Commerciale Fiorella Bernardo

Portale web statico per la pubblicazione e consultazione delle circolari ufficiali dello Studio Commerciale Fiorella Bernardo.

## 🌐 Sito Pubblicato

Il sito è pubblicato su **GitHub Pages** e accessibile all'indirizzo:
[https://studiobf.github.io/circolari-aziendali/](https://studiobf.github.io/circolari-aziendali/)

## 🏗️ Struttura del Progetto

```
circolari-aziendali/
├── index.html                          # Homepage principale
├── circolari.json                      # Database circolari (aggiorna qui!)
├── circolari/
│   ├── formazione-settore-impiantistico.html
│   └── template.html                   # Template per nuove circolari
├── assets/
│   └── logo.png                        # Logo dello studio
└── README.md
```

## ✨ Caratteristiche

- **Design Moderno e Responsive**: Interfaccia elegante ottimizzata per desktop e mobile
- **Caricamento Dinamico**: Le circolari vengono caricate automaticamente da `circolari.json`
- **Facile Manutenzione**: Aggiungi nuove circolari senza modificare il codice HTML
- **Integrazione Social**: Collegamenti diretti ai canali Telegram e WhatsApp
- **Mappa Interattiva**: Localizzazione ufficio con Google Maps integrato

## 📝 Come Aggiungere una Nuova Circolare

### 1. Crea il File HTML della Circolare

Usa il template `circolari/template.html` come base:

```bash
cp circolari/template.html circolari/nome-circolare.html
```

Modifica il nuovo file inserendo:
- Titolo della circolare
- Destinatari
- Contenuto completo

### 2. Aggiorna il File `circolari.json`

Aggiungi un nuovo oggetto all'array JSON:

```json
{
    "id": "nome-circolare",
    "title": "Titolo della Circolare",
    "description": "Breve descrizione (max 2 righe)",
    "date": "20 Nov 2025",
    "day": "20",
    "month_year": "Nov 2025",
    "category": "Categoria",
    "file": "circolari/nome-circolare.html"
}
```

Le circolari più recenti dovrebbero essere inserite **all'inizio** dell'array per apparire per prime.

### 3. Pubblica su GitHub

```bash
git add .
git commit -m "Aggiungi nuova circolare: [titolo]"
git push origin main
```

La circolare sarà automaticamente visibile sul sito entro pochi minuti!

## 🧪 Test Locale

Per testare il sito localmente, avvia un server HTTP:

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
- **JavaScript Vanilla** - Caricamento dinamico delle circolari
- **GitHub Pages** - Hosting gratuito

## 📋 Template delle Circolari

Ogni circolare segue una struttura uniforme:
- Header con navigazione coerente alla homepage
- Badge categoria
- Sezioni numerate con stile consistente
- Card colorate per evidenziare informazioni importanti
- Footer con contatti e link "Torna alla Home"

## 🔧 Configurazione GitHub Pages

1. Vai su **Settings** > **Pages** del repository
2. Source: **Deploy from a branch**
3. Branch: **main** / Cartella: **/ (root)**
4. Salva

Il sito sarà disponibile all'URL GitHub Pages del repository.

## 📞 Contatti

**Studio Commerciale Fiorella Bernardo**  
Corso San Benedetto, 170  
87022 Cetraro (CS)

- 📞 Tel: 0982 971430
- 📱 Cel: 393 987 9566
- 📠 Fax: 0982 531061
- ✉️ Email: bernardo.fiorella@gmail.com
- 📧 PEC: bernardo.fiorella@pec.it

---

© 2025 Studio Commerciale Fiorella Bernardo - Tutti i diritti riservati
