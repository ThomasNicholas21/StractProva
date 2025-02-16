<h1 align="center">
   Desafio Stract
</h1>


## :rocket: Sobre o projeto

Este projeto, desenvolvido com Python e o framework Flask, foi criado com o objetivo de trabalhar com requisições e APIs, retornando informações de plataformas como Facebook Ads, Google Analytics e TikTok. Esses dados fornecem insights valiosos para análise e otimização de estratégias, auxiliando na tomada de decisões com fins lucrativos.

A aplicação foi estruturada de forma modular, garantindo melhor organização, manutenção e escalabilidade, facilitando futuras implementações e aprimoramentos.

## :mag: Tecnologias usadas:

- `Python`
- `Flask`

## :computer: Endpoints:

- `/`
- `/{{plataforma}}`
- `/{{plataforma}}/resumo`
- `/geral`
- `/geral/resumo`

## :wrench: Iniciando o projeto
1. Clone este repositório usando: `https://github.com/ThomasNicholas21/StractProva.git`;
2. Entre no diretório;
3. Rode o comando `pip install -r requirements.txt` para instalar todas as dependências;
4. Rode o comando `python manage.py` para iniciar a aplicação.
5. Nos endpoints utilize valores válidos para o parâmetro plataforma:
- `meta_ads`
- `ga4`
- `tiktok_insights`
