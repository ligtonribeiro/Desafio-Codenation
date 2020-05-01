import json 
import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=57b8d8c5faf6f2dd86613eedf7ae8aca34bb290f"
r = requests.get(url)
response_json = r.json()

with open('answer.json', 'w') as json_file:
    json.dump(response_json, json_file, indent=4)
 

with open('answer.json', 'r') as json_deserialize:
    dados = json.load(json_deserialize)

cifrado = dados['cifrado']
numero_casas = dados['numero_casas']
caracteres_validos = 'abcdefghijklmnopqrstuvwxyz'
decifrado = ''

for letra in cifrado:
    if letra in caracteres_validos:
        posicao = caracteres_validos.find(letra)
        posicao = (posicao - numero_casas) % len(caracteres_validos)
        decifrado = decifrado + caracteres_validos[posicao]
    else:
        decifrado = decifrado + letra

print(decifrado)