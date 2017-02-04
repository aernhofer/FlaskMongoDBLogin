from flask_login import login_user
from Users.User import User

from FlaskTutorial import app, db
from flask import render_template, flash, redirect

from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",title='Home',
                           #user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if db.login(email, password):
            flash('Login requested for email="%s", password="%s", remember_me=%s' %
                  (form.email.data, form.password.data, str(form.remember_me.data)))
            return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)
