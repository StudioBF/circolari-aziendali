---
description: Scansiona 'nuove_circolari', aggiunge le circolari al DB e propone il push su GitHub.
---

Usa questo workflow quando l'utente scrive `/aggiungi_circolare` o chiede di importare nuove circolari.

### 1. Scansione
Controlla se ci sono file `.md` nella cartella `nuove_circolari/`.
*   Se vuota: Avvisa l'utente.
*   Se presenti: Procedi con l'elaborazione file per file.

### 2. Elaborazione (Loop per ogni file)
Per ogni file `.md` trovato:

1.  **Analisi & Parsing**:
    *   Leggi il file Markdown.
    *   Converti il contenuto in un oggetto JSON valido seguendo rigorosamente lo schema del DB (vedi regole sotto).
    *   Assicurati che `id` sia `lowercase-con-trattini` e univoco.

2.  **Revisione Editoriale e Sintesi**:
    *   **NON** copiare e incollare il contenuto del Markdown.
    *   **Agisci come un Caporedattore**: Leggi il testo, scarta refusi, commenti AI o ricerche superflue.
    *   Estrai solo le notizie rilevanti: Date, Obblighi, Sanzioni, Novità.
    *   Riscrivi il testo in stile "News Aziendale": conciso, professionale, paragrafi brevi.
    *   Tempo di lettura target: < 2 minuti.

3.  **Generazione Script di Inserimento**:
    Crea un file temporaneo `temp_insert_circular.py` con il contenuto JSON *già revisionato e sintetizzato*.

    **Template Script:**
    ```python
    import json
    import os

    # DATI ESTRATTI DAL MARKDOWN (L'Agente li compila qui)
    NEW_DATA = {
        "id": "...", 
        "title": "...",
        # ... altri campi ...
    }

    TARGET_FILE = "e:/circolari-aziendali/circolari.json"

    def run():
        if not os.path.exists(TARGET_FILE):
            print("Errore: DB non trovato")
            exit(1)

        try:
            with open(TARGET_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Check duplicati
            if any(c['id'] == NEW_DATA['id'] for c in data):
                print(f"SKIP: ID {NEW_DATA['id']} già presente.")
                return

            data.insert(0, NEW_DATA)

            with open(TARGET_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print("SUCCESS")
            
        except Exception as e:
            print(f"ERROR: {e}")
            exit(1)

    if __name__ == "__main__":
        run()
    ```

3.  **Esecuzione**:
    *   Esegui: `python temp_insert_circular.py`
    *   Se output è "SUCCESS":
        *   Elimina `temp_insert_circular.py`.
        *   **Chiedi conferma all'utente**: "Ho inserito [Titolo]. Posso cancellare il file [NomeFile.md]?"
        *   Se Sì -> Cancella il file `.md`.
    *   Se errore -> Fermati e segnala il problema.

### 3. Push su GitHub
Dopo aver processato tutti i file:
1.  Chiedi all'utente: "Vuoi pubblicare le modifiche su GitHub ora?"
2.  Se Sì:
    *   `git status` (per verifica)
    *   `git add circolari.json`
    *   `git commit -m "Aggiunta nuove circolari"`
    *   `git push origin main`

---

#### Schema JSON di Riferimento
```json
{
    "id": "slug-univoco",
    "title": "Titolo",
    "subtitle": "Sottotitolo/Intro",
    "ref": "Rif. Normativo",
    "tag": "Es: Normativa/Avviso",
    "target_audience": "Destinatari",
    "description": "Anteprima",
    "date": "dd Mon yyyy",
    "content": [
        { "type": "paragraph", "text": "...", "style": "lead" }, // Solo per il primo
        { "type": "section", "title": "...", "number": "1", "blocks": [] },
        { "type": "list", "items": [{ "highlight": "Key", "text": "Value" }] },
        { "type": "grid", "cards": [{ "title": "...", "text": "...", "color": "orange" }] }
    ]
}
```
