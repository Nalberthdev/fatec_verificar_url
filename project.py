import requests
import re

# Chave da API do Google Safe Browsing
API_KEY = "sua api" #busque uma API, indico a do google Safe Browsing.
URL_GOOGLE_SAFE = "https://safebrowsing.googleapis.com/v4/threatMatches:find?key=" + API_KEY # URL da API do Google Safe Browsing

url = input("Digite a URL para verificar: ")

# Verifica se a URL é válida usando regex
padrao = re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")
if not re.match(padrao, url):
    print("URL inválida!")
else:
    # Prepara os dados para enviar à API
    dados = {
        "client": {"clientId": "meu_validador", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }

    # Faz a requisição à API do Google Safe Browsing
    resposta = requests.post(URL_GOOGLE_SAFE, json=dados)
    resultado = resposta.json()

    # Verifica o resultado
    if "matches" in resultado:
        print("⚠️ URL MALICIOSA DETECTADA!")
    else:
        print("✅ URL segura!")
