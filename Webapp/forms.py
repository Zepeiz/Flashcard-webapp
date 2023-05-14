#Creating forms for users to fill out
from os import set_inheritable
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from Webapp.models import User



class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check): #flask will check for validate_(variable name) from User in models.py
        user = User.query.filter_by(username = username_to_check.data).first() #returns an object, use first() to get the first value
        if user: #If two usernames are the same, raise error
            raise ValidationError('Username already exists! Please try a different username.')
    
    def validate_email(self, email_address_to_check):
        email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email_address:
            raise ValidationError('This email address in already in use! Please try a different email address.')

    username = StringField(label='Username', validators=[Length(min=2, max=20), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register') #Names of buttons are set here

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign In') #Names of buttons are set here

class CardForm(FlaskForm):
    key_phrase = StringField(label='Key Phrase', validators=[DataRequired()])
    definition = StringField(label='Definition', validators=[DataRequired()])
    submit = SubmitField(label='Save')

class CreateCardForm(FlaskForm):
    submit = SubmitField(label='Create Card')