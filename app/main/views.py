from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import Player
from . import main
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        player = Player.query.filter_by(username=form.username.data).first()
        if player is None:
            session['known'] = False
        else:
            session['known'] = True
            session['player_id'] = player.id
        session['username'] = form.username.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, username=session.get('username'),
                           known=session.get('known', False),
                           player_id=session.get('player_id'))
