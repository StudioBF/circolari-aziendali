# 📝 SPECIFICA TECNICA PER LO SVILUPPO DI UN SITO DI CIRCOLARI AZIENDALI

## OBIETTIVO DEL PROGETTO

Creare una base di sito statico utilizzando GitHub Pages per ospitare le circolari ufficiali dell'azienda. L'obiettivo è fornire un link pulito e stabile per la diffusione tramite WhatsApp e Telegram.

**STRUMENTI:** HTML5, Tailwind CSS (per la semplicità e la responsività), JavaScript (minimalista per interazioni di base).

## 1\. ISTRUZIONI CHIAVE PER L'AGENTE IA

L'agente IA deve generare una struttura di repository centralizzata contenente i seguenti file, **utilizzando Tailwind CSS v3** per lo styling.

### Regole per lo Sviluppo:

1.  **Linguaggio:** Tutto il testo visibile (interfaccia utente e contenuti) deve essere in italiano.
2.  **Responsività:** Il layout deve essere ottimizzato per la visualizzazione su dispositivi mobili (mobile-first).
3.  **Estetica:** Deve essere pulito, moderno e istituzionale (usando colori neutri, blu scuro/bianco/grigio).
4.  **Tailwind Setup:** Caricare Tailwind tramite CDN in tutti i file HTML.

## 2\. STRUTTURA DEL REPOSITORY

Il repository deve essere chiamato circolari-aziendali e deve contenere la seguente struttura di directory:

circolari-aziendali/  
├── index.html <-- Pagina principale / Indice delle circolari  
└── circolari/  
├── formazione-81-08.html <-- Il file della prima circolare da caricare  
└── template.html <-- Template HTML per le future circolari  

## 3\. CONTENUTI DEI FILE DA GENERARE

L'agente deve generare il codice per i seguenti tre file.

### 3.1. index.html (Pagina Indice/Bacheca)

Questa pagina deve servire da archivio delle news.

**Contenuto:**

*   Titolo: "Archivio Circolari Ufficiali"
*   Una sezione in alto con un logo placeholder e il nome dell'azienda ("Nome Azienda S.R.L.").
*   Un elenco ben strutturato e responsive (a schede o elenco) che mostri la prima circolare.

### 3.2. circolari/formazione-81-08.html (La Circolare Completa)

Questo file contiene la circolare fornita dall'utente.

**Contenuto:**

*   Riproduzione esatta del testo fornito.
*   Deve includere un pulsante "Torna all'Archivio" in fondo.
*   Lo stile deve essere pulito e istituzionale, facile da leggere.

### 3.3. circolari/template.html (Template per Nuove Circolari)

Un file da usare come base per le future news, con gli stili già applicati.

**Contenuto:**

*   Struttura HTML/Tailwind completa.
*   Sezioni vuote o con testo placeholder: Titolo, Data, Corpo del Testo.
*   Inclusione del pulsante "Torna all'Archivio".

## 4\. ISTRUZIONI PER LA PUBBLICAZIONE SU GITHUB PAGES

Dopo aver generato i file e creato il repository (ad esempio, con nome utente MioUtente), l'agente deve spiegare i seguenti passaggi per l'attivazione di GitHub Pages:

1.  **Commit & Push:** Caricare tutti i file sul repository remoto.
2.  **Attivazione di GitHub Pages:** Navigare su Settings > Pages del repository.
3.  **Source:** Selezionare Deploy from a branch e impostare il branch main (o master) e la cartella / (root) come sorgente.
4.  **URL Finale:** Fornire un esempio dell'URL finale, ad esempio: https://MioUtente.github.io/circolari-aziendali/.

**NOTA BENE:** L'agente deve generare il codice completo per index.html, circolari/formazione-81-08.html e circolari/template.html.