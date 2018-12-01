from flask import current_app as app
from flask import render_template,redirect,url_for
from ..models import User,save_object
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
        if not User.query.filter(User.username==user).first():
            test_user=User(username=username,password=password,email=email)
            save_object(test_user)
            login_user(test_user)
            return redirect(url_for('#'))
    return render_template('registration.html',form=form)

@auth.route('/login',methods=['GET','POST'])
def login():
    form=SignIn()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        if User.query.filter(User.username==username).first():
            test_user=User.query.filter(User.username==user).first()
