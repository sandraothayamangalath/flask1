from flask import Flask, render_template,flash,redirect,url_for,session,logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from flask import request
app= Flask(__name__)
Articles =Articles()
@app.route('/')
def index():
    # return 'render_template'
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',articles=Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html',id=id)

class RegisterForm(form.Form):
    name=StringField('name',[validators.length(min=1,max=50)])
    username=StringField('username',[validators.length(min=4,max=24)])
    Email=StringField('Email',[validators.length(min=6,max=50)])
    password=PasswordField('password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='password do not match')
    ])
    confirm=PasswordField('confirm password ')

@app.route('/register', methods=['GET','POST'])
def register():
    form=RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        print(".............................................................if")
        return render_template('register.html')
    return render_template('register.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)