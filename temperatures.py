import requests
import json
from datetime import datetime

# Coordenades de Tremp (o qualsevol altra ciutat que vulguis)
lat = 42.167
lon = 0.894

# Obtenir les temperatures horàries d'avui
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&timezone=Europe/Madrid"
resposta = requests.get(url)
dades = resposta.json()

temperatures = dades["hourly"]["temperature_2m"]

# Calcular màxim, mínim i mitjana
max_temp = max(temperatures)
min_temp = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

# Data d'avui
data_avui = datetime.now().strftime("%Y%m%d")
fitxer = f"temp_{data_avui}.json"

# Crear diccionari i guardar-lo
resultat = {
    "data": data_avui,
    "temperatura_maxima": max_temp,
    "temperatura_minima": min_temp,
    "temperatura_mitjana": round(avg_temp, 2)
}

with open(fitxer, "w") as f:
    json.dump(resultat, f, indent=4)
