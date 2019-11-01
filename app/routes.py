import os
import subprocess
from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, SpellCheckerForm
from app.models import User, UserLoginHistory, UserServiceHistory
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Spell Checker Home')

@app.route("/register", methods=['GET','POST'])
def register():
    result_str = " "
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('register.html', title='Register', form=form, result_str=result_str)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, phone=form.phone.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        result_str = "success"
        flash('success - Your account has been created - please log in!', 'success')
    else:
        result_str = "failure"        
        flash('failure - Acount Registration failed - please try again!', 'danger')
    return render_template('register.html', title='Register', form=form, result_str=result_str)
    
@app.route("/login", methods=['GET','POST'])
def login():
    result_str = " "
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not bcrypt.check_password_hash(user.password, form.password.data):
            result_str = "Incorrect Two-factor failure"
            flash('Two-factor failure - Login Unsuccessfull', 'danger')
        elif user.phone != form.phone.data:
            result_str = "Incorrect Two-factor failure"
            flash('Two-factor failure - Login Unsuccessfull', 'danger')
        else:
            result_str = "success."
            login_user(user, remember=form.remember.data)
            login_record = UserLoginHistory(user_id = user.id, time_login=datetime.now(), time_logout=None)
            db.session.add(login_record)
            db.session.commit()
    return render_template('login.html', title='Login', form=form, result_str=result_str)


@app.route("/logout")
@login_required
def logout():
    if current_user.is_authenticated:
        # db.session.pop('login_record') -- try this approach
        # trying with current_user alias to pull the latest record from UserLoginHistory
        try:
            login_record = UserLoginHistory.query.filter(UserLoginHistory.user_id == current_user.id).\
                                                  filter(UserLoginHistory.time_logout == None).\
                                                  filter(UserLoginHistory.time_login < datetime.now()).first()
            print(login_record)
        except:
            return redirect(url_for('home'))

        login_record.time_logout = datetime.now()
        db.session.commit()

        user = current_user
        user.authenticated = False
        db.session.add(user)
        db.session.commit()
        logout_user()
    return redirect(url_for('home'))

@app.route("/spell_check", methods=['GET','POST'])
@login_required
def spellcheck():
    if (not current_user.is_authenticated):
        return redirect(url_for('login'))
    form = SpellCheckerForm()
    if form.validate_on_submit():
        input_text = form.input_content.data

        if (os.getenv('OS')[:3] == "Win"):
            spellcheck_file_path = os.path.join(app.root_path, 'spell_check\spell_check.exe')
            input_file_path = os.path.join(app.root_path, 'spell_check\input.txt')
            wordlist_file_path = os.path.join(app.root_path, 'spell_check\wordlist.txt')
        else:
            spellcheck_file_path = './a.out'
            input_file_path = os.path.join(app.root_path, 'spell_check/input.txt')
            wordlist_file_path = os.path.join(app.root_path, 'spell_check/wordlist.txt')
        
        with open(input_file_path, 'w') as f:
            f.write(str(input_text))
        if not f:
            flash('Error creating input file for spell checker!', 'danger')
            return redirect(url_for('spellcheck'))

        form.input_content.data = input_text
        form.output_content.data = input_text
        misspelled_words = subprocess.check_output([spellcheck_file_path, input_file_path, wordlist_file_path], stderr=subprocess.STDOUT).decode('utf-8')

        if (os.getenv('OS')[:3] == "Win"):
            form.misspelled_content.data = misspelled_words.replace("\r", ", ").replace("\n", "").strip()[:-1]
        else:
            form.misspelled_content.data = misspelled_words.replace("\n", ", ").strip()[:-1]

        service_record = UserServiceHistory(user_id = current_user.id, input_content = input_text, misspelled_content = form.misspelled_content.data)
        db.session.add(service_record)
        db.session.commit()

    return render_template('spellcheck.html', form=form)