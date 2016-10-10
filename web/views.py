from flask import render_template, jsonify, request

from .server import app
from .models import Title


@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/titles')
def list_titles():
    titles = Title.objects.all()
    return jsonify(titles=titles)


@app.route('/titles/<int:title_id>')
def title_view(title_id):
    titles = Title.objects.get(id=title_id)
    return jsonify(title=title)
