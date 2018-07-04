from flask_login import current_user
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, ValidationError, validators, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import Required, Length, Email
from flask_wtf.file import FileField, FileAllowed

from app.models import User


class PostBidForm(FlaskForm):
    '''
    class to create a wtf form for posting bid
    '''
    description = TextAreaField('Bid Description ', validators=[Required()])
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

    category = SelectField('Category', choices=[('Web_development', "Web development"), ("App_development", "App development"), ("Content_Management_Systems", "Content Management Systems"), ("E_Commerce", "E-Commerce")])

    submit = SubmitField('Post')


class ReviewsForm(FlaskForm):
    '''
    class to create a wtf form for posting reviews
    '''
    description = TextAreaField('Reviews Description ', validators=[Required()])
    scale = IntegerField('Reviews Scale(1-5)', [validators.NumberRange(message='Range should be between 1 and 5.',
                                                                       min=1, max=5)])
    submit = SubmitField('Submit')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=2, max=20)])

    email = StringField('Your Email Address', validators=[Email()])

    picture = FileField('Change Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update information')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class AcceptbidForm(FlaskForm):
    submit = SubmitField('Accept Bid')


class DownloadKeyForm(FlaskForm):
    download_key = IntegerField('Enter your download key')
    submit = SubmitField('Download')

