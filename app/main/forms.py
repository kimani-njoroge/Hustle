from wtforms import StringField, TextAreaField, SubmitField, IntegerField, ValidationError, validators
from flask_wtf import FlaskForm
from wtforms.validators import Required
from flask_wtf.file import FileField, FileAllowed


class PostBidForm(FlaskForm):
    '''
    class to create a wtf form for posting bid
    '''
    description = TextAreaField('Bid Description ',validators=[Required()])
    cost = IntegerField('Bid Cost $', validators=[Required()])
    submit = SubmitField('Submit')


class PostJobForm(FlaskForm):
    '''
    Function to create a wtf form for posting a job
    '''
    title = StringField('title', validators=[Required()])

    description = StringField('description', validators=[Required()])

    duration = StringField('duration', validators=[Required()])

    technologies = StringField('technologies', validators=[Required()])


    submit = SubmitField('Post')

class ReviewsForm(FlaskForm):
    '''
    class to create a wtf form for posting reviews
    '''
    description = TextAreaField('Reviews Description ',validators=[Required()])
    scale = IntegerField('Reviews Scale(1-5)', [validators.NumberRange(message='Range should be between 1 and 5.',
                               min=1, max=5)])
    submit = SubmitField('Submit')

class SetUpAccountForm(FlaskForm):
    bio = TextAreaField('bio', validators=[Required()])

    cows = StringField('Your Conditions of Work', validators=[Required()])


    submit = SubmitField('Set up Account')
