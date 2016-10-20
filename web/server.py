import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.contrib.fixers import ProxyFix


basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../')

app = Flask(__name__)
app.config.from_object("web.config.Config")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://gostate_user:{}@localhost/gostate".format(os.environ['DATABASE_PASS'])
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'


# flask-sqlalchemy
db = SQLAlchemy(app)

# flask-marshmallow
ma = Marshmallow(app)

import web.views
app.wsgi_app = ProxyFix(app.wsgi_app)

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    import app.firstmodule.controllers as firstmodule

    app.register_blueprint(firstmodule.module)

    return app

