from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=False, nullable=True)
    phone = db.Column(db.String(16), unique=False, nullable=False)
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # inputs = db.relationship('SpellChecker', backref='author', lazy=True)
    
    def __repr__(self):
        # return f"User('{self.username}', '{self.phone}', '{self.email}', '{self.image_file}')"
        return f"User('{self.username}', '{self.phone}')"
    
# class SpellChecker(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # input_content = db.Column(db.Text, nullable=False)
    # misspelled_content = db.Column(db.Text, nullable=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # def __repr__(self):
        # return f"SpellChecker('{self.title}', '{self.date_posted}')"
