# Prima parte: la copia che non copia.
originale = {"id": "N-001", "documenti": ["preventivo"]}
copia = originale.copy()
copia["documenti"].append("foto")
print("superficiale:", originale)
print("superficiale:", copia)

# Seconda parte: si copia anche la lista, e i due dizionari diventano indipendenti.
originale = {"id": "N-001", "documenti": ["preventivo"]}
copia = originale.copy()
copia["documenti"] = originale["documenti"].copy()
copia["documenti"].append("foto")
print("indipendente:", originale)
print("indipendente:", copia)

# Terza parte: due nomi, un oggetto solo. is risponde alla domanda «è lo stesso oggetto?».
altro_nome = originale
print("stesso oggetto?", altro_nome is originale)
print("stessa lista?", copia["documenti"] is originale["documenti"])
