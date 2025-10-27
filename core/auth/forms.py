from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .models import User

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), 
                                           Length(1, 64), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  need_to_remember = BooleanField('Need to remember')
  submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  repeat_password = PasswordField('Repeat Password', 
                                  validators=[DataRequired(), 
                                              EqualTo('password')])
  is_teacher = BooleanField('Are you a teacher?')
  language = SelectField("select", choices=[('1', '中国'), ('2', 'Deutsch'), ('3', 'English'), ('4', 'Русский')])
  submit = SubmitField('Register')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data)
    if user is not None:
      raise ValidationError('Email already registered.')
  
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data)
    if user is not None:
      raise ValidationError('Username already in use.')