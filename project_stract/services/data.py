from project_stract.services.api_stract import get_platforms, get_accounts, get_fields, get_insights

# O endpoint "/{{plataforma}}" deve retornar uma 
# tabela em que cada linha represente um anúncio 
# veiculado na plataforma indicada. As colunas 
# devem trazer todos os campos de insights daquele 
# anúncio, bem como o nome da conta que o está veiculando. 
# Em nenhuma das tabelas precisam ser retornados IDs, 
# mas é importante observar que o nome não é um identificador único

# gera dados de insight para plataforma
def generate_platform_insights(plataforma):
    accounts = get_accounts(plataforma)
    fields = get_fields(plataforma)
    text_platforma = ''

    all_insights = []

    plataformas = get_platforms()
    for value_i in plataformas['platforms']:
        if value_i['value'] == plataforma:
            text_platforma = value_i['text']

    for account in accounts:
        account_name = account['name']
        account_id = account['id']
        account_token = account['token']
        dict_default = {'platform': text_platforma, 'account_name': account_name}

        insights_format = get_insights(plataforma, account_id, account_token, fields)

        if insights_format:
            for iterable in insights_format['insights']:
                for key, value in iterable.items():
                    dict_default.setdefault(key, value)

            all_insights.append(dict_default)

    
    return all_insights

if __name__ == "__main__":
    plataformas = get_platforms()
    plataforma1 = plataformas['platforms'][0]['value']
    teste = generate_platform_insights(plataforma1)

    for i in teste:
        print(i)
