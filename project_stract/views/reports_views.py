from flask import Blueprint
from project_stract.services.data import generate_platform_insights, generate_platform_insights_summary
from project_stract.services.data import generate_all_platform_insights
from project_stract.utils.generate_csv import generator_csv

ads_blueprint = Blueprint("ads", __name__)

@ads_blueprint.route('/<string:platforma>', methods=['GET'])
def get_ads_by_platform(platforma):

    get_platform_infos = generate_platform_insights(platforma)

    return generator_csv(get_platform_infos, filename=f'{platforma}_infos.csv')

@ads_blueprint.route('/<string:plataforma>/resumo', methods=['GET'])
def get_platform_summary(plataforma):

    get_platform_summary_infos = generate_platform_insights_summary(plataforma)

    return generator_csv(get_platform_summary_infos, filename=f'{plataforma}_resumo.csv')

@ads_blueprint.route('/geral', methods=['GET'])
def get_all_ads():

    list_all_infos = generate_all_platform_insights()

    return generator_csv(list_all_infos, filename='geral_insights.csv')

@ads_blueprint.route('/geral/resumo', methods=['GET'])
def get_general_summary():
    return 'teste /geral/resumo'

