import os

from flask import Flask
import flask_login
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
# from werkzeug.contrib.fixers import ProxyFix

# from celery import Celery


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object("web.config.ProductionConfig")


# Celery
# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

# flask-login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# flask-sqlalchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# flask-marshmallow
ma = Marshmallow(app)

import web.views
# app.wsgi_app = ProxyFix(app.wsgi_app)

# def create_app():
    # app = Flask(__name__)
    # app.config.from_object(os.environ['APP_SETTINGS'])

    # db.init_app(app)
    # with app.test_request_context():
        # db.create_all()

    # import app.firstmodule.controllers as firstmodule

    # app.register_blueprint(firstmodule.module)

    # return app

