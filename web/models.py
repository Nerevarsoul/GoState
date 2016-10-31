from datetime import datetime

from sqlalchemy_utils import ChoiceType

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

    __table_args__ = (db.UniqueConstraint('first_name', 'last_name', name='_full_name'),)

    def __repr__(self):
        return '<Player object {}>'.format(self.id)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
    
    
class Title(db.Model):

    STATUS = [
        ('int', 'International'),
        ('con', 'Continental'),
        ('nat', 'National')
    ]

    TYPES = [
        ("major", "Major"),
        ("minor", "Minor"),
        ("w", "Women's"),
        ('team', 'Team'),
        ('hayago', 'Hayago'),
        ('leagues', 'Leagues'),
    ]


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    started = db.Column(db.String(4))
    country = db.Column(db.String(120), nullable=False)
    status = db.Column(ChoiceType(STATUS))
    kind = db.Column(ChoiceType(TYPES))
    defunct = db.Column(db.Boolean, default=False)
    current_winner = db.Column(db.Integer, db.ForeignKey("player.id"))
    holding = db.Column(db.Integer)
    time_added = db.Column(db.DateTime, default=datetime.now())
    time_edited = db.Column(db.DateTime, default=datetime.now())

    __table_args__ = (db.UniqueConstraint('name', 'country', name='_country_name'),)

    def __repr__(self):
        return '<Title object {}>'.format(self.id)

    def __str__(self):
        return self.name
    
    
class Tournament(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Date, nullable=False)
    title = db.Column(db.Integer, db.ForeignKey("title.id"), nullable=False)
    winner = db.Column(db.Integer, db.ForeignKey("player.id"))
    runner_up = db.Column(db.Integer, db.ForeignKey("player.id"))
    score = db.Column(db.String)
    time_added = db.Column(db.DateTime, default=datetime.now())
    time_edited = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Tournament object {}>'.format(self.id)

    def __str__(self):
        return '{} - {}'.format(self.title, self.year)

    __table_args__ = (db.UniqueConstraint('title', 'year', name='_year_title'),)

