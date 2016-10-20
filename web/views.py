from flask import render_template, jsonify, request

from .server import app
from .models import Title
from .serializers import TitleSchema


@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/titles')
def list_titles():
    titles = Title.query.all()
    data = title_schema.dump(titles)
    return jsonify(titles=data)


@app.route('/titles/<int:title_id>')
def title_view(title_id):
    titles = Title.query.get(id=title_id)
    return jsonify(title=title)

