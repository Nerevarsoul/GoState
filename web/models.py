from datetime import datetime

from .server import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    date_of_born = db.Column(db.Date)
    country = db.Column(db.String(120), nullable=False)
    turned_pro = db.Column(db.String(4))
    time_added = db.Column(db.Datetime, default=datetime.now)
    rank = db.Column(db.Integer)
    time_edited = db.Column(db.Datetime, default=datetime.now)
    
    
class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    started = db.Column(db.String(4))
    country = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    defunct = db.Column(db.Boolean, default=False)
    time_added = db.Column(db.Datetime, default=datetime.now)
    time_edited = db.Column(db.Datetime, default=datetime.now)
    
    
class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Date, nullable=False)
    title = db.Column(db.Integer, db.ForeignKey("title.id"), nullable=False)
    winner = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    runner_up = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    score = db.Column(db.String)
    time_added = db.Column(db.Datetime, default=datetime.now)
    time_edited = db.Column(db.Datetime, default=datetime.now)

