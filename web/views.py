from flask import render_template, jsonify, request

from .server import app
from .models import Title


@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/titles')
def index_view():
    titles = Title.objects.all()
    return jsonify(titles=titles)
