from flask import Flask, render_template, url_for, flash, redirect, request
from flask_bootstrap import Bootstrap
from forms import UploadForm
from werkzeug.utils import secure_filename


app = Flask(__name__)
bootstrap = Bootstrap(app)

config = {
    'SECRET_KEY' : 'a94fb169151cb216ff7dd85f31742b3a',
    'WTF_CSRF_SECRET_KEY' : '77273898287e4c215e4c4bffcb7f0573'
}
app.config.update(config)


UPLOAD_FOLDER = 'deck_builder/uploads/'
ALLOWED_EXTENSIONS = {'pdf'} # ADD MORE
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/deckbuilder', methods=['GET','POST'])
def deckbuilder():
    form = UploadForm()
    if form.validate_on_submit():
        
        file = form.file.data
        if file:
            filename = secure_filename(file.filename)
            file.save('uploads/'+filename)
            # run script based on pdf insertion
        else:
            raw = form.raw_string.data
            # run script based on raw text
        
    else:
        print(form.file.data)
        

    return render_template('deckbuilder.html', form=form)









if __name__ == '__main__':
    app.run(debug=True)