from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Player, StatsSnapshot

@api.route('/statssnapshots/')
def get_statssnapshots():
    statssnapshots = StatsSnapshot.query.all()
    return jsonify({'statssnapshots': [statssnapshot.to_json() for statssnapshot in statssnapshots] })

@api.route('/statssnapshots/<int:id>')
def get_statssnapshot(id):
    statssnapshot = StatsSnapshot.query.get_or_404(id)
    return jsonify(statssnapshot.to_json())
