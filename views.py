from flask_login import login_user, logout_user, login_required, current_user
from Users.User import User
from FlaskTutorial import app, db, lm
from flask import render_template, flash, redirect, request, url_for
from forms import LoginForm, RegisterForm
from datetime import datetime

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['posttext'])
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'Erni'},
            'body': 'Ich mag Zuege!'
        }
    ]
    return render_template("index.html", title='Home', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if(db.getUser(form.email.data)==None): #Makes sure emails are unique
            db.register(vname=form.vname.data, nname=form.nname.data,
                        email=form.email.data, passwd=form.password.data)
            user_obj = db.getUser(form.email.data)
            login_user(user_obj)
            flash("Registered successfully", category='success')
            return redirect(request.args.get("next") or url_for("private"))
        else:
            form.email.errors.append('This email is already in use. \
                                      Please goto Login or choose another one.')
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        #user = db.users.find_one({"email": form.email.data})
        user = db.getUserJson(form.email.data)
        if user and User.validate_login(user['password'], form.password.data):
            db.updateLastLogin(form.email.data)
            user_obj = db.getUser(form.email.data)
            login_user(user_obj, remember=form.remember_me.data)
            flash("Logged in successfully", category='success')
            return redirect(request.args.get("next") or url_for("private"))
        flash("Wrong username or password", category='error')
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("Successfully logged out", category='success')
    return redirect(url_for('login'))


@app.route('/private')
@login_required
def private():
    return render_template('private.html', title='Private')


@app.route('/user/<email>')
@login_required
def user(email):
    user = db.getUser(email)
    if user == None:
        flash('User %s not found.' % email, category='error')
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)


@lm.user_loader
def load_user(email):
    return db.getUser(email)
