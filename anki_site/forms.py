from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, email_validator, ValidationError
from flask_wtf.file import FileField, FileAllowed
from anki_site.database import User

ALLOWED_FILE_EXTENSIONS = ['pdf']

class UploadForm(FlaskForm):
    file = FileField('Upload File', validators=[
        FileAllowed(ALLOWED_FILE_EXTENSIONS, 'Filetype not allowed.')
    ])
    raw_string = StringField('Input Text',
                            render_kw={'style': 'width: 300px; height: 200px;\
                                       font-size: 16px;'})
    submit = SubmitField('Submit')


    def validate(self, extra_validators=None):
        if not super(UploadForm, self).validate(extra_validators=extra_validators):
            return False

        # Count the number of filled fields
        filled_fields = sum(
            1 for field in [self.file, self.raw_string] if field.data
        )
        
        # At least one field must be filled
        if filled_fields != 1:
            self.errors['field'] = ['Exactly one field must be filled']
            return False

        return True
    
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