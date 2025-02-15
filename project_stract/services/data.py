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


# O endpoint "/geral" deve trazer todos os anúncios de todas as plataformas. 
# Nesse relatório devem ser adicionadas colunas para identificar por nome a 
# plataforma na qual o anúncio está sendo veiculado, além do nome conta que 
# esta veiculando o anúncio. Devem haver colunas para todos os campos existentes 
# na API. Campos de diferentes plataformas que possuam o mesmo nome podem ser 
# apresentados na mesma coluna, isto é, uma mesma coluna pode (mas não necessariamente 
# deve) ser aproveitada pelas mesmas plataformas. O campo pode ficar vazio nas linhas 
# das plataformas nas quais ele não exista. Uma exceção é o campo "Cost per Click", 
# que não está disponível para esta API no Google Analytics, porém pode ser calculado 
# dividindo-se o valor de "spend" pelo valor de "clicks".
def generate_all_platform_insights():
    platforms = get_platforms()
    list_all_platforms = []

    # Coletar todos os insights
    for platform in platforms['platforms']:
        for key_platform, value_platform in platform.items():
            if key_platform == 'value':
                list_platforms = generate_platform_insights(value_platform)
                list_all_platforms.extend(list_platforms)


    all_keys = set()
    for insight in list_all_platforms:
        all_keys.update(insight.keys())


    for insight in list_all_platforms:
        for key in all_keys:
            if key not in insight:
                insight[key] = "" 


        if insight["cost_per_click"] == "":
            if insight["spend"] and insight["clicks"]:
                cpc_sum = insight["spend"] / insight["clicks"]
                insight["cost_per_click"] = f"{cpc_sum:.2f}"
            else:
                insight["cost_per_click"] = 0
                

    return list_all_platforms

# O endpoint "/geral/resumo" deve trazer uma tabela similar, mas colapsando em uma única linha 
# todas as linhas que forem da mesma plataforma. Caso as colunas seja numéricas, os dados devem 
# ser somados. Caso sejam texto, a coluna pode ficar vazia na linha em questão (exceto nome da 
# plataforma, que é o mesmo para todas as linhas agregadas da plataforma em questão).
def generate_all_platform_insights_summary():
    list_all_platforms = generate_all_platform_insights()

    summary_insights_dict = {}
    all_keys = []


    for insight in list_all_platforms:
        for key in insight.keys():
            if key not in all_keys:
                all_keys.append(key)

    for insight in list_all_platforms:
        platform = insight.get("platform")

        if platform not in summary_insights_dict:
            summary_insights_dict[platform] = {"platform": platform}

        summary_insights = summary_insights_dict[platform]

        for key in all_keys:
            value = insight.get(key, None)

            if key == "platform":
                continue  

            elif isinstance(value, (int, float)):
                summary_insights[key] = summary_insights.get(key, 0) + value

            elif value is None:
                summary_insights[key] = "" 

            else:
                summary_insights[key] = ""

    return list(summary_insights_dict.values())



if __name__ == "__main__":

    valores = generate_all_platform_insights()
    print(valores)