from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class BusinessRegistrationForm(FlaskForm):
    name=StringField('Business Name',validators=[DataRequired(),Length(min=5,max=50)])
    description=StringField('Business Description',validators=[DataRequired()])
    owner=StringField('Owner',validators=[DataRequired()])
    submit=SubmitField('Register')


class ReviewForm(FlaskForm):
    reviewer_name=StringField('Reviewer Name',validators=[DataRequired(),Length(min=5,max=50)])
    business_name=StringField('Business Name',validators=[DataRequired(),Length(min=5,max=50)])
    review=StringField('Business Review',validators=[DataRequired(),Length(min=5,max=500)])
