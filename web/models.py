from datetime import datetime

from .server import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    date_of_born = db.Column(db.Date)
    country = db.Column(db.String(120), nullable=False)
    turned_pro = db.Column(db.String(4))
    time_added = db.Column(db.DateTime, default=datetime.now())
    rank = db.Column(db.Integer)
    time_edited = db.Column(db.DateTime, default=datetime.now())
    
    
class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    started = db.Column(db.String(4))
    country = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    defunct = db.Column(db.Boolean, default=False)
    current_winner = db.Column(db.String(120))
    holding = db.Column(db.Integer)
    time_added = db.Column(db.DateTime, default=datetime.now())
    time_edited = db.Column(db.DateTime, default=datetime.now())
    
    
class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Date, nullable=False)
    title = db.Column(db.Integer, db.ForeignKey("title.id"), nullable=False)
    winner = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    runner_up = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    score = db.Column(db.String)
    time_added = db.Column(db.DateTime, default=datetime.now())
    time_edited = db.Column(db.DateTime, default=datetime.now())

