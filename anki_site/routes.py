from flask import render_template, url_for, flash, redirect, request, send_file, session
from anki_site.forms import UploadForm, RegistrationForm, LoginForm
from werkzeug.utils import secure_filename
from anki_site.backend_script import create_deck_from_file
from anki_site.database import User, Deck
from anki_site import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import os

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()


        flash(f'Account created! You are now able to login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html', title ='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
           flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', title ='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route('/decks')
@login_required
def decks():
    return render_template('decks.html', title='Decks')



@app.route('/download/<deckname>')
def download(deckname: str):

    return send_file('instance/files/created/'+current_user.username+'/'+deckname+'apkg', as_attachment=True)



@app.route('/deckbuilder', methods=['GET','POST'])
def deckbuilder():
    UPLOAD_FOLDER = "anki_site/instance/files/uploads/"
    DOWNLOAD_FOLDER = "anki_site/instance/files/created/"
    form = UploadForm()
    if form.validate_on_submit():
        
        deckname = form.deckname.data
        raw = form.raw_string.data
        with open(UPLOAD_FOLDER+'textfile.txt', 'w') as file:
            file.write(raw)
        # run script based on raw text
        create_deck_from_file(UPLOAD_FOLDER+'textfile.txt','txt','fr','en',
                            deckname,DOWNLOAD_FOLDER+current_user.username+"/")
        session['filename'] = deckname
        if os.path.exists(UPLOAD_FOLDER+'textfile.txt'):
            os.remove(UPLOAD_FOLDER+'textfile.txt')

        return redirect(url_for('download', deckname=deckname))

    else:
        pass

    # not deleting return file for some reason
    if os.path.exists(DOWNLOAD_FOLDER+'tempdeckname.apkg'):
        os.remove(DOWNLOAD_FOLDER+'tempdeckname.apkg')
        
    return render_template('deckbuilder.html',title='App', form=form)
