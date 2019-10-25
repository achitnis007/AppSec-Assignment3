from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_talisman import Talisman

name = "app"

app = Flask(__name__)

SELF = "'self'"

Talisman(
    app,
    content_security_policy={
        'default-src': SELF,
        'script-src': [
            SELF,
            'code.jquery.com',
            'cdnjs.cloudflare.com',
            'stackpath.bootstrapcdn.com' 
        ],
        'style-src': [
            SELF,
            'code.jquery.com',
            'cdnjs.cloudflare.com',
            'stackpath.bootstrapcdn.com'          
        ],
        'Strict-Transport-Security': 'max-age=0; includeSubDomains'
    },
    content_security_policy_nonce_in=['script-src']
)


# <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
# <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
# <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>


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


