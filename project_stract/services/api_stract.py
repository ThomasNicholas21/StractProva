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
    url = f"https://sidebar.stract.to/api/accounts"
    headers = {"Authorization": "ProcessoSeletivoStract2025"}
    
    all_accounts_infos = []
    page = 1 

    while True:
        params = {"platform": plataforma, "page": page}
        response = requests.get(url=url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Erro ao buscar dados: {response.status_code}")
            break

        data = response.json()

        all_accounts_infos.extend(data.get("accounts", []))

        pagination = data.get("pagination", {})
        current_page = pagination.get("current", 1)
        total_pages = pagination.get("total", 1)

        if current_page >= total_pages:
            break

        page += 1

    return all_accounts_infos

# for plataforma in plataformas['platforms']:
#     # nome descritivo
#     nome = plataforma['text']
#     # valor
#     valor = plataforma['value']
#     contas = get_accounts(valor)

#     print(f'{nome}: {valor}', f'{contas}', sep='\n')

def get_fields(plataforma):
    url = f"https://sidebar.stract.to/api/fields"
    headers = {"Authorization": "ProcessoSeletivoStract2025"}

    all_fields_infos = []
    page = 1 

    while True:
        params = {"platform": plataforma, "page": page}
        response = requests.get(url=url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Erro ao buscar dados: {response.status_code}")
            break

        data = response.json()

        all_fields_infos.extend(data.get("fields", []))

        pagination = data.get("pagination", {})
        current_page = pagination.get("current", 1)
        total_pages = pagination.get("total", 1)

        if current_page >= total_pages:
            break

        page += 1

    return all_fields_infos

# for plataforma in plataformas['platforms']:
#     # nome descritivo
#     nome = plataforma['text']
#     # valor
#     valor = plataforma['value']
#     contas = get_fields(valor)

#     print(f'{nome}: {valor}', f'{contas}', sep='\n')



# print(plataforma, account, fields, sep='\n\n')

def get_insights(plataforma, account_id, token, fields):
    url = "https://sidebar.stract.to/api/insights"
    headers = {"Authorization": "ProcessoSeletivoStract2025"}  
    

    field_value_list = []
    for value in fields:
        field_value_list.append(value['value'])

    params = {
        "platform": plataforma,
        "account": account_id,
        "token": token,  
        "fields": ','.join(field_value_list)
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Erro {response.status_code}: {response.text}")
        return None

    return response.json()

plataforma = plataformas['platforms'][0]['value']
accounts = get_accounts(plataforma)
account_id = accounts[0]['id']
account_token = accounts[0]['token']
fields = get_fields(plataforma)

insights = get_insights(plataforma, account_id, account_token, fields)
print(insights)
