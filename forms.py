from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from flask_wtf.file import FileField, FileAllowed, FileRequired

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