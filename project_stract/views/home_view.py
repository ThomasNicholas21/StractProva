from flask import Blueprint, jsonify
from project_stract.utils.generate_csv import generator_csv

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def home():
    dados_json = {
        'nome':'Thomas Nicholas Pedrosa Matias',
        'email': 'thomasnicholaas@gmail.com',
        'link': 'https://www.linkedin.com/in/thomaas-nicholas/'
        }

    return generator_csv(dados_json, filename='home_data.csv')
