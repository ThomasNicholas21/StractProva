from flask import Flask

def aplication():
    app = Flask(__name__)

    from project_stract.views.home_view import home_bp
    app.register_blueprint(home_bp)

    return app