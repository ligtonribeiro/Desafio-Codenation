import hashlib
import json
import requests
from decouple import config
from functions import *

# Consumindo a API
token = config('TOKEN')
url_get = f"https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={token}"
url_post = f"https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={token}"
r = requests.get(url_get)
response_json = r.json()

# Salvando resposta da API em um arquivo JSON / Realizando deserialização
gerarJSON('answer.json', response_json)
dados = deserializeJSON('answer.json')

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

# Atualizando arquivo JSON
dados['decifrado'] = decifrado
gerarJSON('answer.json', dados)

# SHA1
decifrado = dados['decifrado']
resumo_criptografico = hashlib.sha1(decifrado.encode('utf-8')).hexdigest()
dados['resumo_criptografico'] = resumo_criptografico
gerarJSON('answer.json', dados)

# Enviando arquivo JSON
files = [('answer', open('answer.json', 'rb'))]
headers = {}
response = requests.post(url_post, headers=headers, files=files)
nota = response.text

print("Texto Cifrado: ", cifrado)
print("Texto Decifrado: ", decifrado)
print("Pontução do desafio: ", nota)