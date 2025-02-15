from flask import Blueprint
from project_stract.services.data import generate_platform_insights
from project_stract.utils.generate_csv import generator_csv

ads_blueprint = Blueprint("ads", __name__)

@ads_blueprint.route('/<string:platforma>', methods=['GET'])
def get_ads_by_platform(platforma):

    get_platform_infos = generate_platform_insights(platforma)

    return generator_csv(get_platform_infos, filename=f'{platforma}_infos.csv')

@ads_blueprint.route('/<string:platforma>/resumo', methods=['GET'])
def get_platform_summary(platforma):
    return 'teste /plataforma/resumo'

@ads_blueprint.route('/geral', methods=['GET'])
def get_all_ads():
    return 'teste /geral'

@ads_blueprint.route('/geral/resumo', methods=['GET'])
def get_general_summary():
    return 'teste /geral/resumo'

