from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class SignUp(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=10)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Passsword',validators=[DataRequired()])
    password2=PasswordField('Confirm Passsword',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

class SignIn(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Passsword',validators=[DataRequired()])
    submit=SubmitField('Login')
