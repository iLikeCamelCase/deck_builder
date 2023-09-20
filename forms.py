from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from flask_wtf.file import FileField, FileAllowed, FileRequired

ALLOWED_FILE_EXTENSIONS = ['pdf']

class UploadForm(FlaskForm):
    file = FileField('Upload your file.', validators=[
        FileAllowed(ALLOWED_FILE_EXTENSIONS, 'Filetype not allowed.')
    ])
    raw_string = StringField('Or input text')
    submit = SubmitField('Submit')


    def validate(self):
        if not super(UploadForm, self).validate():
            return False

        # Count the number of filled fields
        filled_fields = sum(
            1 for field in [self.file, self.raw_string] if field.data
        )

        # At least one field must be filled
        if filled_fields < 1:
            self.field1.errors.append('At least one field must be filled.')
            return False

        return True