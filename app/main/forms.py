from wtforms import StringField,TextAreaField,SubmitField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import Required


class PostBidForm(FlaskForm):
    '''
    class to create a wtf form for posting bid
    '''
    description = TextAreaField('Bid Description ',validators=[Required()])
    cost = IntegerField('Bid Cost$', validators=[Required()])
    submit = SubmitField('Submit')
