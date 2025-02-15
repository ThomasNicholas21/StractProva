from project_stract.services.api_stract import get_platforms, get_accounts, get_fields, get_insights
# from api_stract import get_platforms, get_accounts, get_fields, get_insights
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


# O endpoint "/{{plataforma}}/resumo" deve trazer uma tabela similar, 
# mas colapsando em uma única linha todas as linhas que forem da mesma 
# conta, ficando apenas uma linha para cada conta. Os dados devem ser 
# somados nas colunas numéricas e, nas colunas que tem texto, os dados 
# podem ficar vazios (exceto o nome da conta, que é o mesmo para todas 
# as linhas agregadas da conta em questão). 
def generate_platform_insights_summary(plataforma):
    all_insights = generate_platform_insights(plataforma)
    
    # Dicionário para armazenar a soma dos valores
    summary_insights = {}
    summary_insights_list = []

    for insight in all_insights:
        for key, value in insight.items():
            if key == "platform":
                summary_insights["platform"] = value

            elif isinstance(value, (int, float)):
                summary_insights[key] = summary_insights.get(key, 0) + value

            else:
                summary_insights[key] = ""

    summary_insights_list.append(summary_insights)

    return summary_insights_list


if __name__ == "__main__":
    plataformas = get_platforms()
    plataforma3 = plataformas['platforms'][2]['value']

    valores = generate_platform_insights_summary(plataforma3)
    print(valores)