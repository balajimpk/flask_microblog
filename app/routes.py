# this line imports the app defined in init.py for the current app(can be any name) folder
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'balaji'}
    posts = [{
        'author': {'username':'balaji'},
        'body': 'beautiful soup'
    },
        {
            'author': {'username':'balaji'},
            'body': 'learning flask'
        }]
    # return 'hello, world!' + user['username']
    # return '''
    # <html><head>
    # <title>MICROBLOG</title>
    # </head>
    # <body>
    #     <h1>  hi, ''' + user['username'] + '''
    # </body>
    # </html>'''
    return render_template('index.html', title='home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)