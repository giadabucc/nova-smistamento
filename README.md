# nova-smistamento

Smista il lotto di richieste che arriva ogni mattina a Nova Assicurazioni: ogni pratica esce con una categoria
(`da_completare`, `da_rivedere`, `ordinaria`) e in fondo si leggono i conteggi. I dati sono sintetici e le
categorie sono convenzioni di laboratorio: non autorizzano rimborsi.

## Requisiti

- [uv](https://docs.astral.sh/uv/) installato. Python 3.12 lo procura uv da sé.

## Come si avvia

Dalla cartella del progetto, quella che contiene `pyproject.toml`:

```bash
uv run python smista.py
```

Il primo avvio crea l'ambiente in `.venv`. L'ultima riga stampata deve essere `Prove sui confini: tutte superate.`:
se una regola cambia, il programma si ferma prima su un `assert` e dice quale.

## Controlli

```bash
uv run ruff check .
uv run ruff format --check .
```

## La regola

| condizione, nell'ordine | categoria |
|---|---|
| importo assente (`None`) | `da_completare` |
| importo di almeno 100000 centesimi, oppure meno di 2 documenti | `da_rivedere` |
| altrimenti | `ordinaria` |

Una pratica è identificata dalla coppia `(tenant, id)`. Se arriva due volte, si conserva la prima occorrenza.
