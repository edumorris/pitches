from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError, BooleanField, TextAreaField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email Address:', validators=[Required(), Email()])
    username = StringField("Enter a username:", validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("Email already registered. Go to login page")
    
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username not available')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address:', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your comment:', validators=[Required()])
    submit = SubmitField('Comment')

pitch_category = [('Pickup Lines', 'Pickup Lines'), ('Interview Pitch', 'Inteview Pitch'), ('Product Pitch', 'Product Pitch'), ('Promo Pitch', 'Promo Pitch')]

class PitchForm(FlaskForm):
    category = SelectField('Category', choices=pitch_category)
    pitch = TextAreaField('Your pitch:', validators=[Required()])
    submit = SubmitField('Submit Pitch')