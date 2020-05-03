import json

def gerarJSON(nome_json, resposta_api):
    with open(nome_json, 'w') as arquivo_json:
        json.dump(resposta_api, arquivo_json, indent=4)

def deserializeJSON(nome_json):
    dados = {}
    with open('answer.json', 'r') as arquivo_json:
        dados = json.load(arquivo_json)
    return dados
