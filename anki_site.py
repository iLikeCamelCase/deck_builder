from flask import Flask, render_template, url_for, flash, redirect, request
from flask_bootstrap import Bootstrap
from forms import UploadForm
from werkzeug.utils import secure_filename
from backend_script import create_deck_from_file
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
bootstrap = Bootstrap(app)
config = {
    'SECRET_KEY' : 'a94fb169151cb216ff7dd85f31742b3a',
    'WTF_CSRF_SECRET_KEY' : '77273898287e4c215e4c4bffcb7f0573',
    'UPLOAD_FOLDER' : 'deck_builder/uploads/',
    'SQLALCHEMY_DATABASE_URI' : 'sqlite:///site.db'
}
app.config.update(config)

db = SQLAlchemy(app)

# Classes for db ##################################################

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) #max username length 20
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    words = db.Column(db.Text)
    decks = db.relationship('Deck', backref='author', lazy=True)

    def __repr__(self):
        return f"User('self.username', 'self.email')"
    
class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deckname = db.Column(db.String, unique=True, nullable=False)
    source = db.Column(db.String, nullable=False)
    dest = db.Column(db.String, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )

    def __repr__(self):
        return f"Deck('{self.deckname}', '{self.source}', '{self.dest}')"
    

###################################################################


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
            create_deck_from_file('uploads/'+filename,'pdf','fr','en',
                                  'tempdecknamepdf','created/')

        else:
            raw = form.raw_string.data
            with open('uploads/textfile.txt', 'w') as file:
                file.write(raw)
            # already knows it's in upload/ directory
            # let's change that so we need to tell it
            create_deck_from_file('uploads/textfile.txt','txt','fr','en',
                                  'tempdecknametxt','created/')
            # run script based on raw text
        
    else:
        print(form.file.data)
        

    return render_template('deckbuilder.html', form=form)









if __name__ == '__main__':
    app.run(debug=True)