from flask import Blueprint, jsonify
from project_stract.services.data import generate_platform_insights, generate_platform_insights_summary
from project_stract.services.data import generate_all_platform_insights, generate_all_platform_insights_summary
from project_stract.utils.generate_csv import generator_csv

ads_blueprint = Blueprint("ads", __name__)

VALID_PARAMS_PLATFORM = ['meta_ads', 'ga4', 'tiktok_insights']

@ads_blueprint.route('/<string:plataforma>', methods=['GET'])
def get_ads_by_platform(plataforma):
    if plataforma not in VALID_PARAMS_PLATFORM:
        return jsonify({"error": "Plataforma invalida"}), 400

    get_platform_infos = generate_platform_insights(plataforma)

    return generator_csv(get_platform_infos, filename=f'{plataforma}_infos.csv')

@ads_blueprint.route('/<string:plataforma>/resumo', methods=['GET'])
def get_platform_summary(plataforma):
    if plataforma not in VALID_PARAMS_PLATFORM:
        return jsonify({"error": "Plataforma invalida"}), 400

    get_platform_summary_infos = generate_platform_insights_summary(plataforma)

    return generator_csv(get_platform_summary_infos, filename=f'{plataforma}_resumo.csv')

@ads_blueprint.route('/geral', methods=['GET'])
def get_all_ads():

    list_all_infos = generate_all_platform_insights()

    return generator_csv(list_all_infos, filename='geral_insights.csv')

@ads_blueprint.route('/geral/resumo', methods=['GET'])
def get_general_summary():

    list_all_infos_summary = generate_all_platform_insights_summary()

    return generator_csv(list_all_infos_summary, filename='geral_resumo.csv')
