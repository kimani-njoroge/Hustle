from wtforms import StringField,TextAreaField,SubmitField, IntegerField,ValidationError, validators
from flask_wtf import FlaskForm
from wtforms.validators import Required


class PostBidForm(FlaskForm):
    '''
    class to create a wtf form for posting bid
    '''
    description = TextAreaField('Bid Description ',validators=[Required()])
    cost = IntegerField('Bid Cost$', validators=[Required()])
    submit = SubmitField('Submit')


class PostJobForm(FlaskForm):
    '''
    Function to create a wtf form for posting a job
    '''
    title = StringField('title', validators=[Required()])

    description = StringField('description', validators=[Required()])

    duration = StringField('duration', validators=[Required()])

    technologies = StringField('technologies', validators=[Required()])


    submit = SubmitField('Sign Up')

class ReviewsForm(FlaskForm):
    '''
    class to create a wtf form for posting reviews
    '''
    description = TextAreaField('Reviews Description ',validators=[Required()])
    scale = IntegerField('Reviews Scale', [validators.Length(min=1, max=5)])
    submit = SubmitField('Submit')
