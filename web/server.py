import logging
import os

from flask import Flask
import flask_login
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
# from werkzeug.contrib.fixers import ProxyFix

from .core import db


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object("web.config.ProductionConfig")

# Configure logging
handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
handler.setLevel(app.config['LOGGING_LEVEL'])
formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
handler.setFormatter(formatter)
app.logger.addHandler(handler)

app.debug = True
toolbar = DebugToolbarExtension(app)

# flask-login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# flask-sqlalchemy
# db = SQLAlchemy(app)
db.init_app(app)
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

