import requests


# verificando platformas
def get_platforma():
    url = "https://sidebar.stract.to/api/platforms"
    headers = {"Authorization": "ProcessoSeletivoStract2025"}
    response = requests.get(url=url, headers=headers)
    return response.json()

plataformas = get_platforma()
print(plataformas)
