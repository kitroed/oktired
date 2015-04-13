from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    username = StringField('Please enter the player screen name you wish to verify:', validators=[Required()])
    submit = SubmitField('Submit')
