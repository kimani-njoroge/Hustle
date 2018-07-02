from wtforms import StringField,PasswordField,BooleanField,SubmitField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import Required, Email


#Login class
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')