from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def home():
    dados_json = jsonify(
        {
            'name':'teste',
            'e-mail': 'teste@teste.com',
            'linkedln': 'www.linkedln.com'
        }
    )

    return dados_json
