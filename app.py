from app import app
from app import db, bcrypt
from app.models import User
db.drop_all()

db.create_all()

hashed_password = bcrypt.generate_password_hash('Administrator@1').decode('utf-8')
user = User(username='admin', phone='12345678901', password=hashed_password)
db.session.add(user)
db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
    # with https for tox-travis testing
    # app.run(ssl_context='adhoc', debug=True)
