from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Player, StatsSnapshot

@api.route('/players/')
def get_players():
    players = Player.query.all()
    return jsonify({'players': [player.to_json() for player in players] })

@api.route('/players/<string:id>')
def get_player(id):
    player = Player.query.get_or_404(id)
    return jsonify(player.to_json())

@api.route('/players/<string:id>/statssnapshots/')
def get_player_statssnapshots(id):
    player = Player.query.get_or_404(id)
    player_statssnapshots = player.statssnapshots.order_by(StatsSnapshot.timestamp.desc())
    return jsonify({'statssnapshots': [player_statssnapshot.to_json() for player_statssnapshot in player_statssnapshots] })

