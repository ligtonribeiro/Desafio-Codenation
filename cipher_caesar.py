import hashlib
import json
import requests

from decouple import config

# Consumindo a API, salvando reposta em arquivo JSON
url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=" + config('TOKEN')
r = requests.get(url)
response_json = r.json()

with open('answer.json', 'w') as arquivo_json:
    json.dump(response_json, arquivo_json, indent=4)

with open('answer.json', 'r') as json_deserialize:
    dados = json.load(json_deserialize)

# Descriptografando o texto.
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

print("Texto Cifrado: " + cifrado)
print("Texto Decifrado: " + decifrado)

# Atualizando arquivo JSON
dados['decifrado'] = decifrado

with open('answer.json', 'w') as atualizar_cifrado_json:
    json.dump(dados, atualizar_cifrado_json, indent=4)

# SHA1
decifrado = dados['decifrado']
resumo_criptografico = hashlib.sha1(decifrado.encode('utf-8')).hexdigest()
dados['resumo_criptografico'] = resumo_criptografico

with open('answer.json', 'w') as atualizar_resumo_json:
    json.dump(dados, atualizar_resumo_json, indent=4)
