from flask import Flask

def aplication():
    app = Flask(__name__)

    from project_stract.views.home_view import home_bp
    from project_stract.views.reports_views import ads_blueprint
    app.register_blueprint(home_bp)
    app.register_blueprint(ads_blueprint)

    return app