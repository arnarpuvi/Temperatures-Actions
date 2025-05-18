import requests
import json
from datetime import datetime

# Ciutat: Lleida (canvia-ho si vols una altra)
latitude = 41.6176
longitude = 0.6200

# Demanar dades a Open-Meteo
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
response = requests.get(url)
data = response.json()

# Obtenir les temperatures d'avui
hores = data["hourly"]["time"]
temperatures = data["hourly"]["temperature_2m"]

# Filtrar només les temperatures d'avui
avui = datetime.now().date().isoformat()
temps_avui = [temp for hora, temp in zip(hores, temperatures) if hora.startswith(avui)]

# Calcular màxim, mínim i mitjana
if temps_avui:
    maxim = max(temps_avui)
    minim = min(temps_avui)
    mitjana = sum(temps_avui) / len(temps_avui)
else:
    maxim = minim = mitjana = None

# Crear diccionari de resultats
resultat = {
    "data": avui,
    "temperatura_maxima": maxim,
    "temperatura_minima": minim,
    "temperatura_mitjana": mitjana
}

# Exportar a JSON
nom_fitxer = f"temp_{avui.replace('-', '')}.json"
with open(nom_fitxer, "w") as f:
    json.dump(resultat, f, indent=4)

print(f"Dades guardades a {nom_fitxer}")
