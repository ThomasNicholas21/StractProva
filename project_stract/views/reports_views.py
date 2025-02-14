from flask import Blueprint

ads_blueprint = Blueprint("ads", __name__)

@ads_blueprint.route('/<string:platforma>', methods=['GET'])
def get_ads_by_platform(platforma):
    return 'teste /plataforma'

@ads_blueprint.route('/<string:platforma>/resumo', methods=['GET'])
def get_platform_summary(platforma):
    return 'teste /plataforma/resumo'

@ads_blueprint.route('/geral', methods=['GET'])
def get_all_ads():
    return 'teste /geral'

@ads_blueprint.route('/geral/resumo', methods=['GET'])
def get_general_summary():
    return 'teste /geral/resumo'

