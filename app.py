from app import app
from app import db, bcrypt
from app.models import User, UserLoginHistory, UserServiceHistory
from datetime import datetime as dt
import datetime

db.drop_all()

db.create_all()

hashed_password = bcrypt.generate_password_hash('Administrator@1').decode('utf-8')
user = User(username='admin', phone='12345678901', password=hashed_password)
db.session.add(user)

hashed_password = bcrypt.generate_password_hash('1111111111').decode('utf-8')
user = User(username='actester1', phone='1111111111', password=hashed_password)
db.session.add(user)

hashed_password = bcrypt.generate_password_hash('2222222222').decode('utf-8')
user = User(username='actester2', phone='2222222222', password=hashed_password)
db.session.add(user)

hashed_password = bcrypt.generate_password_hash('3333333333').decode('utf-8')
user = User(username='actester3', phone='3333333333', password=hashed_password)
db.session.add(user)

u1_time_now = dt.now()
u2_time_now = u1_time_now + datetime.timedelta(minutes=6)
u3_time_now = u2_time_now + datetime.timedelta(minutes=6)
u4_time_now = u3_time_now + datetime.timedelta(minutes=6)

user_login = UserLoginHistory(user_id=1, time_login=u1_time_now, time_logout=u1_time_now + datetime.timedelta(minutes=5))
db.session.add(user_login)

user_login = UserLoginHistory(user_id=2, time_login=u2_time_now, time_logout=u2_time_now + datetime.timedelta(minutes=5))
db.session.add(user_login)

user_login = UserLoginHistory(user_id=3, time_login=u3_time_now, time_logout=u3_time_now + datetime.timedelta(minutes=5))
db.session.add(user_login)

user_login = UserLoginHistory(user_id=4, time_login=u4_time_now, time_logout=u4_time_now + datetime.timedelta(minutes=5))
db.session.add(user_login)


    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    # input_content = db.Column(db.Text, nullable=False)
    # misspelled_content = db.Column(db.Text, nullable=True)

user_query = UserServiceHistory(user_id=1, date_posted=u1_time_now + datetime.timedelta(minutes=1),
								input_content='admin - query1 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)
user_query = UserServiceHistory(user_id=1, date_posted=u1_time_now + datetime.timedelta(minutes=2),
								input_content='admin - query2 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)
user_query = UserServiceHistory(user_id=1, date_posted=u1_time_now + datetime.timedelta(minutes=3),
								input_content='admin - query3 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)

user_query = UserServiceHistory(user_id=2, date_posted=u2_time_now + datetime.timedelta(minutes=1),
								input_content='actester1 - query1 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)
user_query = UserServiceHistory(user_id=2, date_posted=u2_time_now + datetime.timedelta(minutes=2),
								input_content='actester1 - query2 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)
user_query = UserServiceHistory(user_id=2, date_posted=u2_time_now + datetime.timedelta(minutes=3),
								input_content='actester1 - query3 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)

user_query = UserServiceHistory(user_id=3, date_posted=u3_time_now + datetime.timedelta(minutes=1),
								input_content='actester2 - query1 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)
user_query = UserServiceHistory(user_id=3, date_posted=u3_time_now + datetime.timedelta(minutes=2),
								input_content='actester2 - query2 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)
user_query = UserServiceHistory(user_id=3, date_posted=u3_time_now + datetime.timedelta(minutes=3),
								input_content='actester2 - query3 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)

user_query = UserServiceHistory(user_id=4, date_posted=u4_time_now + datetime.timedelta(minutes=1),
								input_content='actester3 - query1 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)
user_query = UserServiceHistory(user_id=4, date_posted=u4_time_now + datetime.timedelta(minutes=2),
								input_content='actester3 - query2 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)
user_query = UserServiceHistory(user_id=4, date_posted=u4_time_now + datetime.timedelta(minutes=3),
								input_content='actester3 - query3 - spell-checker test - hikory dickory dok ',
								misspelled_content='spell-checker, hikory, dickory, dok')
db.session.add(user_query)

db.session.commit()

if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True)
