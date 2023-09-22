from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, instance_path=os.path.join(script_dir,'instance'))
bootstrap = Bootstrap(app)
config = {
    'SECRET_KEY' : 'a94fb169151cb216ff7dd85f31742b3a',
    'WTF_CSRF_SECRET_KEY' : '77273898287e4c215e4c4bffcb7f0573',
    'UPLOAD_FOLDER' : 'deck_builder/uploads/',
    'SQLALCHEMY_DATABASE_URI' : 'sqlite:///site.db'
}
app.config.update(config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# routes imports 'app' from here, wait until app is initialized so that routes
# can import it first. then import routes. avoid circular import
from anki_site import routes