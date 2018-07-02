from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,ValidationError
from wtforms.validators import Required




class PostJobForm(FlaskForm):
    '''
    Function to create a wtf form for posting a job
    '''
    title = StringField('title', validators=[Required()])

    description = StringField('description', validators=[Required()])

    duration = StringField('duration', validators=[Required()])

    technologies = StringField('technologies', validators=[Required()])


    submit = SubmitField('Sign Up')
