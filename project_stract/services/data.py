from api_stract import get_platforms, get_accounts, get_fields, get_insights

# O endpoint "/{{plataforma}}" deve retornar uma 
# tabela em que cada linha represente um anúncio 
# veiculado na plataforma indicada. As colunas 
# devem trazer todos os campos de insights daquele 
# anúncio, bem como o nome da conta que o está veiculando. 
# Em nenhuma das tabelas precisam ser retornados IDs, 
# mas é importante observar que o nome não é um identificador único
# plataformas = get_platforms()
# plataforma1 = plataformas['platforms'][0]['value']
# accounts = get_accounts(plataforma1)
# fields = get_fields(plataforma1)
# insights1 = get_insights(plataforma1, accounts[0]['id'], accounts[0]['token'], fields)

    

# dict_insights = {'platform': plataformas['platforms'][0]['text'], 'account_name': accounts[0]['name']}

# def test(dict_insight: dict):
#     for iterable in insights1['insights']:
#         for chave, valor in iterable.items():
#             dict_insight.setdefault(chave, valor)
    
#     return dict_insight

# lista = test(dict_insights)
# print(lista)

plataformas = get_platforms()
plataforma1 = plataformas['platforms'][0]['value']
# plataforma2 = plataformas['platforms'][1]['value']
# plataforma3 = plataformas['platforms'][2]['value']
# print(plataforma1, plataforma2, plataforma3, sep='\n')

# gera dados de insight para plataforma
def generate_platform_insights(plataforma):
    accounts = get_accounts(plataforma)
    fields = get_fields(plataforma)

    all_insights = []

    for account in accounts:
        account_name = account['name']
        account_id = account['id']
        account_token = account['token']
        dict_default = {'platform': plataforma, 'account_name': account_name}

        insights_format = get_insights(plataforma, account_id, account_token, fields)

        if insights_format:
            for iterable in insights_format['insights']:
                for key, value in iterable.items():
                    dict_default.setdefault(key, value)

                all_insights.append(dict_default)

    
    return all_insights

teste = generate_platform_insights(plataforma1)
print(teste)


# dados = generate_platform_insights(plataforma1)
# print(dados)
# generate_platform_insights(plataforma1)