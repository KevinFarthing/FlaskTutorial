from flask import render_template, flash, redirect, url_for
# url_for('login') - uses endpoint name as argument - which is the name of the function and therefore internal
from app import app
from app.forms import LoginForm
# import all relevant flask modules AND ALSO all python pages what you wrote

@app.route('/')
@app.route('/index')
def index(): #because the base page of websites is conventionally index.html? No! it's the '/'
    user = {'username':'Kevin'}
    # posts list is a total hack to test site.
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # return render_template('index.html',user=user)
    return render_template('index.html', title='Home',user=user, posts=posts)
    # render_template function part of flask? 'index.html' references file in templates folder. Sweet.
    #yep, flask function. remember to import it.

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # extra bits to retrieve login data!
    if form.validate_on_submit(): #returns false when the browser sends a get request
        # flash is a way to show a message to the user, lets them know whatever worked. DOES NOT SHOW AUTOMATICALLY, THE HTML MUST BE ABLE TO USE IT
        flash('Login requested for user {}, remember_me{}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
        # end retrieve login data bits
    # title='Sign In' using title as an arbitrarily named variable, or is it a flask keyword?
    return render_template('login.html',title='Sign In', form=form)