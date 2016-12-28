from datetime import date, datetime

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
    
    titles = db.relationship('Title')

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
    winner = db.relationship('Player')
    holding = db.Column(db.Integer, nullable=False)
    time_added = db.Column(db.DateTime, default=datetime.now())
    time_edited = db.Column(db.DateTime, default=datetime.now())
    igo_url = db.Column(db.String, unique=True, index=True)

    tournaments = db.relationship('Tournament')

    __table_args__ = (db.UniqueConstraint('name', 'country', name='_country_name'),)

    def __repr__(self):
        return '<Title object {}>'.format(self.id)

    def __str__(self):
        return self.name
    
    
class Tournament(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Date)
    holding = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Integer, db.ForeignKey("title.id"), nullable=False)
    winner = db.Column(db.Integer, db.ForeignKey("player.id"))
    runner_up = db.Column(db.Integer, db.ForeignKey("player.id"))
    score = db.Column(db.String)
    time_added = db.Column(db.DateTime, default=datetime.now())
    time_edited = db.Column(db.DateTime, default=datetime.now())

    games = db.relationship('Game')

    def __repr__(self):
        return '<Tournament object {}>'.format(self.id)

    def __str__(self):
        return '{} - {}'.format(self.title, self.year)

    __table_args__ = (db.UniqueConstraint('title', 'year', name='_year_title'),)
    
    
class Game(db.Model):

    RESULT = [
        ('w', 'White'),
        ('b', 'Black'),
        ('j', 'Jigo')
    ]

    STAGE = [
        ('f', 'Final'),
        ('p', 'Preliminary'),
        ('l', 'League')
    ]
        
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today())
    white_player = db.Column(db.Integer, db.ForeignKey("player.id"))
    black_player = db.Column(db.Integer, db.ForeignKey("player.id"))
    winner = db.Column(ChoiceType(RESULT))
    result = db.Column(db.String)
    filename = db.Column(db.String)
    igo_url = db.Column(db.String, unique=True, index=True)
    tournament = db.Column(db.Integer, db.ForeignKey("tournament.id"))
    stage = db.Column(ChoiceType(STAGE))
    event = db.Column(db.String)
        
    def __repr__(self):
        return '<Game object {}>'.format(self.id)

    def __str__(self):
        return '{} - {}: '.format(self.white_player, self.black_player, self.result)
