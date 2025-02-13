import requests
from pathlib import Path

ROOT_DIR = Path(__file__).parent
PATH_TXT = ROOT_DIR / 'prova.txt'

url = "https://sidebar.stract.to/api"
headers = {"Authorization": "ProcessoSeletivoStract2025"}

response = requests.get(url, headers=headers)

with open(PATH_TXT, 'w', encoding='utf-8') as arquivo:
    arquivo.write(response.text)
