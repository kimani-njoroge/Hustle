from wtforms import StringField,TextAreaField,SubmitField, IntegerField,ValidationError
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


    submit = SubmitField('Sign Up')


class SetUpAccountForm(FlaskForm):
    bio = TextAreaField('bio', validators=[Required()])

    cows = StringField('Your Conditions of Work', validators=[Required()])


    submit = SubmitField('Update information')
