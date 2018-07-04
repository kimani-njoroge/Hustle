<<<<<<< HEAD
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, ValidationError, validators
=======
from flask_login import current_user
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, ValidationError, validators, SelectField
>>>>>>> a4d7ff321f0a724bd9b481f174839e2b8dda38bf
from flask_wtf import FlaskForm
from wtforms.validators import Required, Length, Email
from flask_wtf.file import FileField, FileAllowed


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

<<<<<<< HEAD
=======
    category = SelectField('Category', choices=[('Web_development', "Web development"), ("App_development", "App development"), ("Content_Management_Systems", "Content Management Systems"), ("E_Commerce", "E-Commerce")])
>>>>>>> a4d7ff321f0a724bd9b481f174839e2b8dda38bf

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

class SetUpAccountForm(FlaskForm):
    bio = TextAreaField('bio', validators=[Required()])

    cows = StringField('Your Conditions of Work', validators=[Required()])


    submit = SubmitField('Set up Account')


class AcceptbidForm(FlaskForm):
    submit = SubmitField('Accept Bid')


class DownloadKeyForm(FlaskForm):
<<<<<<< HEAD
    download_key = IntegerField('Your download key')
    submit = SubmitField('Submit')

class AddCategoriesForm(FlaskForm):
    name= StringField('Category', validators=[Required()])
=======
    download_key = IntegerField('Enter your download key')
    submit = SubmitField('Download')


class AddCategoriesForm(FlaskForm):
    name = StringField('Category', validators=[Required()])
>>>>>>> a4d7ff321f0a724bd9b481f174839e2b8dda38bf
    submit = SubmitField('Add Category')
