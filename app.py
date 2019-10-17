from app import app
from app import db

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager


# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'ede0f7573b2079e2c4ebbe71537ca81b'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


# db = SQLAlchemy(app)

# db.init_app(app)

db.create_all()

# from app import db

# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'

# from app import routes


if __name__ == '__main__':
    app.run(debug=True)
