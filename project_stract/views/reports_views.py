from flask import Blueprint

ads_blueprint = Blueprint("ads", __name__)

@ads_blueprint.route('/<string:platform>', methods=['GET'])
def get_ads_by_platform():
    return 'teste'

@ads_blueprint.route('/<string:platform>/resumo', methods=['GET'])
def get_platform_summary():
    return 'teste'

@ads_blueprint.route('/geral', methods=['GET'])
def get_all_ads():
    return 'teste'

@ads_blueprint.route('/geral/resumo', methods=['GET'])
def get_general_summary():
    return 'teste'

