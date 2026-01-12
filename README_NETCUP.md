# Guida al Deploy: FioberBot + Circolari Web

Questa guida ti aiuta a mettere online lo stack "Fiober", composto da due entità distinte:
1.  **FioberBot**: Il bot Telegram multiuso (attualmente gestisce le circolari).
2.  **Circolari Web**: Il sito statico per la consultazione delle circolari.

I due servizi sono configurati per girare insieme integrandosi con l'infrastruttura esistente (Traefik).

## 1. Configurazione Cloudflare (DNS)
1.  Accedi al pannello **Cloudflare**.
2.  Vai sulla gestione DNS del dominio `fiorellabernardo.eu`.
3.  Aggiungi un nuovo record:
    *   **Tipo**: `A`
    *   **Nome**: `circolari` (che diventerà `circolari.fiorellabernardo.eu`)
    *   **Indirizzo IP**: Inserisci l'IP del tuo server Netcup.
    *   **Proxy Status**: Imposta su **DNS Only** (Nuvola Grigia) inizialmente per permettere il rilascio del certificato SSL.

## 2. Preparazione Cartella sul Server
Isoliamo tutto in una directory dedicata a Fiober.

1.  Crea la cartella:
    ```bash
    mkdir -p /opt/fiober
    ```
    *(Nota: Ho rinominato la cartella da 'circolari' a 'fiober' dato che il progetto è più ampio)*

2.  Entra nella cartella:
    ```bash
    cd /opt/fiober
    ```

## 3. Caricamento File
Copia questi file in `/opt/fiober`:

*   `docker-compose.yml` (Nuova versione con FioberBot)
*   `Dockerfile.fiober_bot`
*   `Dockerfile.circolari_web`
*   `telegram_publisher.py`
*   `config_secrets.json`
*   `circolari.json`
*   Cartelle `imprese` e `circolari` (contenuto statico)

## 4. Avvio Stack
```bash
docker compose up -d
```

### Gestione dei Servizi Separati

Essendo servizi distinti nel file compose, puoi gestirli singolarmente:

*   **Riavviare solo il Bot** (es. dopo modifica codice Python):
    ```bash
    docker compose restart fiober-bot
    ```
    *oppure per ricostruire:* `docker compose up -d --build fiober-bot`

*   **Riavviare solo il Sito** (es. dopo modifiche HTML/Nginx):
    ```bash
    docker compose restart circolari-web
    ```

*   **Vedere i log del Bot**:
    ```bash
    docker compose logs -f fiober-bot
    ```

## Anatomia del Sistema
*   **fiober-bot**: È il cervello. Legge `circolari.json` (montato come volume) per conoscere i dati e usa l'API di Telegram. Non espone porte web, vive in background.
*   **circolari-web**: È il volto. Un server Nginx leggero che serve le pagine HTML. Espone la porta interna 80 a Traefik, che la rende sicura su `circolari.fiorellabernardo.eu`.

## FAQ
**Posso aggiungere altre funzioni al Bot?**
Sì. Modifica `telegram_publisher.py` (magari rinominandolo in futuro se cresce troppo). Poiché il bot è un container a sé stante, le modifiche non impattano il sito web.
