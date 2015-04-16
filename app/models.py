from datetime import datetime
from flask import current_app, request, url_for
from app.exceptions import ValidationError
import json
from . import db


class Player(db.Model):
    __tablename__ = 'players'
    # intending to use the uuid from minecraft as the player id (stored as a 36 character string)
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(64), unique=True)
    statssnapshots = db.relationship('StatsSnapshot', backref='players', lazy='dynamic')

    def to_json(self):
        json_player = {
            'url': url_for('api.get_player', id=self.id, _external=True),
            'id': self.id,
            'username': self.username,
            'statssnapshot_count': self.statssnapshots.count()
        }
        #__table_args__ = (Uniqueconstraint('username', unique=True))
        return json_player

    def __repr__(self):
        return '<Player %r>' % self.username

class StatsSnapshot(db.Model):
    __tablename__ = 'statssnapshots'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    stats = db.Column(db.Text)
    player_id = db.Column(db.String(36), db.ForeignKey('players.id'))
    # I'd like to enforce avoiding duplicate stats snapshots with something like:
    # Index('ux_player_stats', "player_id", "timestamp")

    def to_json(self):
        json_statssnapshot = {
            'url': url_for('api.get_statssnapshot', id=self.id, _external=True),
            'player_id': self.player_id,
            'timestamp': self.timestamp,
            'stats': json.loads(self.stats)
        }
        return json_statssnapshot

    def __repr__(self):
        return '<Stats Snapshot %n>' % self.id
