from app import app
from app import db

# db.drop_all()

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(ssl_context='adhoc', debug=True)
