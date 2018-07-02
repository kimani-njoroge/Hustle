from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User




class RegistrationForm(FlaskForm):
    '''
    Function to create a wtf form for registering
    '''
    email = StringField('Your Email Address', validators=[Required(),Email()])
    username = StringField('Enter your username', validators=[Required()])
    role = SelectField('Role', choices = [('client', 'Client'), ('freelancer', 'Freelancer')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message="Passwords must match")])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
