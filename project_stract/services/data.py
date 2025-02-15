from api_stract import get_platforms, get_accounts, get_fields, get_insights

# O endpoint "/{{plataforma}}" deve retornar uma 
# tabela em que cada linha represente um anúncio 
# veiculado na plataforma indicada. As colunas 
# devem trazer todos os campos de insights daquele 
# anúncio, bem como o nome da conta que o está veiculando. 
# Em nenhuma das tabelas precisam ser retornados IDs, 
# mas é importante observar que o nome não é um identificador único
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

        #print(account_name, account_id, account_token)
        insights = get_insights(plataforma, account_id, account_token, fields)
        insights.setdefault("account_name", account_name)
        insights.setdefault("platform", plataforma)

        all_insights.append(insights)
    
    return all_insights




dados = generate_platform_insights(plataforma1)
print(dados)
# generate_platform_insights(plataforma1)