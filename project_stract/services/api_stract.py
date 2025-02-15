import requests


# referente ao endpoint: /api/platforms
def get_platforms():
    url = "https://sidebar.stract.to/api/platforms"
    headers = {"Authorization": "ProcessoSeletivoStract2025"}
    response = requests.get(url=url, headers=headers)
    return response.json()


# referente ao endpoint: /api/accounts?platform={{platform}}
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


# referente ao endpoint: /api/fields?platform={{platform}}
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


# referente ao endpoint: /api/insights?platform={{platform}}&account={{account}}&token={{token}}&fields={{field1,field2,etc}}
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
