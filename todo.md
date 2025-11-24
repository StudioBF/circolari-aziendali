Agisci come un Senior Frontend Developer. Sto lavorando su un sito web statico per uno studio commerciale e ho bisogno di rendere dinamica la sezione delle comunicazioni ("Circolari").

I file principali su cui lavorare sono:
1. [index.html](cci:7://file:///e:/circolari-aziendali/index.html:0:0-0:0) (Homepage)
2. [circolari/index.html](cci:7://file:///e:/circolari-aziendali/circolari/index.html:0:0-0:0) (Pagina di visualizzazione singola circolare)
3. [circolari.json](cci:7://file:///e:/circolari-aziendali/circolari.json:0:0-0:0) (File dati contenente le circolari)

Il tuo compito è implementare le seguenti funzionalità, procedendo con estrema attenzione per non rompere il layout esistente:

### 1. Rinnovamento Sezione Circolari in Homepage ([index.html](cci:7://file:///e:/circolari-aziendali/index.html:0:0-0:0))
La sezione "Bacheca Circolari" deve diventare un'applicazione dinamica (Single Page Application logic) che carica i dati da [circolari.json](cci:7://file:///e:/circolari-aziendali/circolari.json:0:0-0:0).
- **Archivio Dinamico**:
  - Implementa un selettore di anno (es. "Archivio 2025").
  - All'avvio, deve rilevare automaticamente l'anno più recente dai dati e mostrare quelle circolari.
  - L'utente deve poter cambiare anno per vedere lo storico.
- **Paginazione a "Carosello"**:
  - Non mostrare tutte le circolari in una lista infinita.
  - Mostra massimo 5 circolari per pagina.
  - Aggiungi controlli di navigazione (es. Avanti/Indietro o numeri) per scorrere le circolari senza ricaricare la pagina.
- **Ricerca Live**:
  - Inserisci una barra di ricerca nella testata della sezione.
  - Implementa un filtro in tempo reale (mentre si digita) che cerca in: Titolo, Sottotitolo, Descrizione e Target.
  - Il filtro deve aggiornare la vista immediatamente.

### 2. Fix Header Visualizzatore ([circolari/index.html](cci:7://file:///e:/circolari-aziendali/circolari/index.html:0:0-0:0))
- Modifica la barra di navigazione (`<nav>`) esistente.
- Rendi l'intero blocco che contiene il **Logo** e il **Nome dello Studio** un unico link cliccabile che riporta alla homepage (`../index.html`).
- Elimina il link testuale separato "Torna alla Home" che risulta ridondante.
- **ATTENZIONE**: Assicurati di preservare la struttura HTML corretta (non cancellare `<body>` o `<nav>`) e le classi Tailwind esistenti.

### Vincoli Tecnici
- Usa JavaScript puro (Vanilla JS) per la massima compatibilità e leggerezza, oppure suggerisci una micro-libreria solo se strettamente necessario per la reattività.
- Il codice deve essere pulito, modulare e non deve richiedere un build system complesso.
- Procedi passo dopo passo verificando che ogni modifica mantenga l'integrità della pagina.