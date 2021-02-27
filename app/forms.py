from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    image = FileField('Images', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])