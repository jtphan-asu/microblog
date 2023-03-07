from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

#decorators modifies the function that follows it
#Flask will invoke this function which associate the URLS / and /index
@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('index')
    return render_template('login.html', title='Sign In', form=form)

def index():
    user = {'username': 'Jonathan'}
    
    posts = [
        {
            'author' : { 'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    
    
    #Flask framework function render_template
    return render_template('index.html', title='Home', user=user, posts=posts)
