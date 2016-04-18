import os

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../')

app = Flask(__name__)
app.config.from_object('web.config')
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

import web.views
app.wsgi_app = ProxyFix(app.wsgi_app)
