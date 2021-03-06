from flask import render_template, jsonify, request

from .server import app, db
from .models import Title, Player, Tournament, Game
from .serializers import title_schema, titles_schema


@app.route('/', methods=['GET'])
def index_view():
    return render_template('index.html')


# list object view
@app.route('/titles/<string:country>', methods=['GET'])
def list_titles(country):
    query = db.session.query(Title).outerjoin(Player, Player.id == Title.current_winner)
    if country and country != 'all':
        query = query.filter_by(country=country)
    titles = query.all()
    return render_template('titles.html', titles=titles)


@app.route('/players/<string:country>', methods=['GET'])
def list_players(country=None):
    query = db.session.query(Player).options(db.subqueryload(Player.titles))
    if country and country != 'all':
        query = query.filter_by(country=country)
    players = query.all()
    return render_template('players.html', players=players)


@app.route('/tournaments/<string:country>', methods=['GET'])
def list_tournaments(country=None):
    pass


@app.route('/games/<string:country>', methods=['GET'])
def list_games(country=None):
    pass


# Single object view
@app.route('/titles/<int:title_id>', methods=['GET'])
def title_view(title_id):
    title = Title.query.get(title_id)
    return render_template('title_view.html', title=title)


@app.route('/players/<int:player_id>', methods=['GET'])
def player_view(player_id):
    player = Player.query.get(player_id)
    return render_template('player_view.html', player=player)


@app.route('/tournaments/<int:tournament_id>', methods=['GET'])
def tournament_view(title_id):
    pass


@app.route('/games/<int:game_id>', methods=['GET'])
def game_view(player_id):
    pass


#API
@app.route('/api/titles', methods=['GET'])
def api_list_titles():
    titles = Title.query.all()
    # print(len(titles))
    data = titles_schema.dump(titles)
    return jsonify(data.data)


@app.route('/api/titles/<int:title_id>', methods=['GET'])
def api_title(title_id):
    title = Title.query.get(title_id)
    data = title_schema.dump(title)
    return jsonify(data.data)


# Errors
# @app.errorhandler(400)
# def internal_error(exception):
    # app.logger.error(exception)
    # return render_template('400.html'), 400


@app.errorhandler(403)
def internal_error(exception):
    app.logger.error(exception)
    return render_template('403.html'), 403


# @app.errorhandler(404)
# def internal_error(exception):
    # app.logger.error(exception)
    # return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(exception):
    app.logger.error(exception)
    return render_template('500.html'), 500
