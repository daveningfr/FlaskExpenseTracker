from flask import Flask
from app.config import Config
# TODO: import flask_sqlalchemy
# TODO: import flask_login
from flask_wtf.csrf import CSRFProtect
from os import path
from flask_sqlalchemy import SQLAlchemy



# TODO: declare sqlalchemy db here
db = SQLAlchemy()
csrf = CSRFProtect()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    
    from .models import Users

    with app.app_context():
        # TODO: initialise sqlalchemy db here
        db.init_app(app)
        
        # TODO: create sqlalchemy db file
        if not path.exists(app.config['DATABASE_NAME']):
            db.create_all()
            print('Created Database!')

        
        csrf.init_app(app)


        # TODO: initialise loginmanager


        from app.auth import auth
        from app.views import views

        app.register_blueprint(auth)
        app.register_blueprint(views)

    return app
