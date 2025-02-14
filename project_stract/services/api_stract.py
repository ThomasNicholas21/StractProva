import requests


# verificando platformas
def get_platforms():
    url = "https://sidebar.stract.to/api/platforms"
    headers = {"Authorization": "ProcessoSeletivoStract2025"}
    response = requests.get(url=url, headers=headers)
    return response.json()

plataformas = get_platforms()
# print(plataformas)

def get_accounts(plataforma):
    url = f"https://sidebar.stract.to/api/accounts?platform={plataforma}"
    headers = {"Authorization": "ProcessoSeletivoStract2025"}
    response = requests.get(url=url, headers=headers)
    return response.json()

for plataforma in plataformas['platforms']:
    # nome descritivo
    nome = plataforma['text']
    # valor
    valor = plataforma['value']
    contas = get_accounts(valor)

    print(f'{nome}: {valor}', f'{contas}', sep='\n')
    