from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

name = "app"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ede0f7573b2079e2c4ebbe71537ca81b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

db.init_app(app)

from app import db

# moved to app.py - unable to create db file if run from here
# db.create_all()

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes


