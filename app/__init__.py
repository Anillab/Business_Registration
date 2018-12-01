from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config_options

bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager=LoginManager()

def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument
    Args:
        config_name:name of the configuartion to be used
    '''
    # initialize the application
    app=Flask(__name__)

    # app configurations
    app.config.from_object(config_options[config_name])

    # initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    return app
