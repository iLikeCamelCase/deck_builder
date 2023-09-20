from flask import Flask, render_template, url_for, flash, redirect, request
from flask_bootstrap import Bootstrap
from forms import UploadForm


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

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/deckbuilder')
def deckbuilder():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save('uploads/'+file.filename)
        # run script here
        

    return render_template('deckbuilder.html', form=form)









if __name__ == '__main__':
    app.run(debug=True)