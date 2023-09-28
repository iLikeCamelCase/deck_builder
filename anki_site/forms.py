from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, email_validator, ValidationError
from flask_wtf.file import FileField, FileAllowed
from anki_site.database import User

ALLOWED_FILE_EXTENSIONS = ['pdf']

class UploadForm(FlaskForm):
    deckname = StringField('Deckname', validators=[DataRequired()])
    raw_string = StringField('', render_kw={'style': 'width: 300px; height: 200px;\
                            font-size: 16px;'}, validators=[DataRequired()])
    submit = SubmitField('Submit')

    
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username already in use. Please choose a different one.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use. Please choose a different one.')