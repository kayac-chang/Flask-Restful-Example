from flask import Flask, jsonify, request
from extensions import db
from product import views
import os

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    """An application factory"""
    app = Flask(__name__)

    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True

    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(views.blueprint)

# Run Server
if __name__ == '__main__':
    create_app().run()
