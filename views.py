from flask_login import login_user, logout_user, login_required
from Users.User import User

from FlaskTutorial import app, db, lm
from flask import render_template, flash, redirect, request, url_for

from forms import LoginForm, RegisterForm

@app.route('/')
@app.route('/index')
def index():
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
    return render_template("index.html",title='Home', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db.register(form.email.data, form.password.data)
        user_obj = User(form.email.data)
        login_user(user_obj)
        flash("Registered successfully", category='success')
        return redirect(request.args.get("next") or url_for("private"))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        #user = db.users.find_one({"email": form.email.data})
        user = db.getUser(form.email.data)
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['email'])
            login_user(user_obj, remember=form.remember_me.data)
            flash("Logged in successfully", category='success')
            return redirect(request.args.get("next") or url_for("private"))
        flash("Wrong username or password", category='error') #TODO:Wird aus irgendeinem Grund nicht angezeigt...
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


@lm.user_loader
def load_user(email):
    u = db.getUser(email)
    if not u:
        return None
    return User(u['email'])