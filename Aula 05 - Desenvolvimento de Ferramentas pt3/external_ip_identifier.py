import json
from urllib.request import urlopen

url = "https://ipinfo.io/json"

response = urlopen(url)

data = json.load(response)

print("Campos Disponíveis: " + ", ".join(data.keys()))

# Altere no print() abaixo os campos que você quer ver
print("Região: " + data["region"])