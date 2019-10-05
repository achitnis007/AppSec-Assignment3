from flask import Flask, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ede0f7573b2079e2c4ebbe71537ca81b'
posts = [
    {
        'author': 'Abhijit Chitnis',
        'title': 'Blog post # 1',
        'content': 'This is my very first blog post - excited!',
        'date_posted': 'May 02, 2019'
    },
    {
        'author': 'Shilpa Chitnis',
        'title': 'Blog post # 2',
        'content': 'This is Shilpa\'s first blog post - very excited!',
        'date_posted': 'Oct 10, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/user/<name>")
def user(name):
    return '<h2>Hello, {0}!</h2>'.format(name)

@app.route("/about")
def about():
    return render_template('about.html', title='About the Blog...')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
    
@app.route("/login")
def login():
    form = loginForm()
    return render_template('login.html', title='Login', form=form)
 
if __name__ == '__main__':
    app.run(debug=True)
