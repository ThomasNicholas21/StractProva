from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def home():
    dados_json = jsonify(
        {
            'nome':'Thomas Nicholas Pedrosa Matias',
            'email': 'thomasnicholaas@gmail.com',
            'link': 'https://www.linkedin.com/in/thomaas-nicholas/'
        }
    )

    return dados_json
