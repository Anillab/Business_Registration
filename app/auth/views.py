from flask import current_app as app
from  app import db
from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import SignUp,SignIn
from . import auth
from flask_login import login_required,current_user,login_user,logout_user

@auth.route('/register',methods=['GET','POST'])
def register():
    form=SignUp()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        email=form.email.data
        phone_number=form.phone_number.data
        if not User.query.filter(User.username==username).first():
            test_user=User(username=username,password=password,email=email,phone_number=phone_number)
            db.session.add(test_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('registration.html',form=form)

@auth.route('/login',methods=['GET','POST'])
def login():
    form=SignIn()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        if User.query.filter(User.email==email).first():
            test_user=User.query.filter(User.email==email).first()
            if test_user is not None and test_user.verify_password(password):
                login_user(test_user,form.remember.data)
                return redirect(url_for('main.index'))
            else:
                flash('INVALID USERNAME OR PASSWORD!')
    return render_template('login.html',form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out!")
    return redirect(url_for('main.index'))
