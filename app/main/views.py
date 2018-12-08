from flask import current_app as app
from app import db
from flask import render_template,redirect,url_for,flash,request
from . import main
from ..models import Business,User,Catalogue,Reviews
from .forms import BusinessRegistrationForm,ReviewForm
from flask_login import login_required,current_user,login_user,logout_user


@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@main.route('/register/businesses',methods=['GET','POST'])
@login_required
def reg_busn():
    form=BusinessRegistrationForm()
    if form.validate_on_submit():
        name=form.name.data
        description=form.description.data
        owner=current_user.id
        test_busn=Business(business_name=name,description=description,userid=owner)
        db.session.add(test_busn)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('biz_registration.html',form=form)

@main.route('/edit/businesses/<string:busn_name>',methods=['GET','POST'])
@login_required
def update_busn(busn_name):
    if request.method == 'POST':
        form=BusinessRegistrationForm()
        newdesc = form.description.data
        test_busn=Business.query.filter_by(business_name=busn_name).first_or_404()
        if test_busn.userid==current_user.id:
            test_busn.description=newdesc
            db.session.commit()
            return render_template('biz_registration.html',form=form)

    else:
        form=BusinessRegistrationForm()
        return render_template('biz_registration.html',form=form)


@main.route('/delete/businesses/<string:busn_name>',methods=['GET','POST'])
def delete_busn(busn_name):
    test_busn=Business.query.filter_by(business_name=busn_name).first_or_404()
    if not test_busn==[]:
        if test_busn.userid==current_user.id:
            db.session.delete(test_busn)
            db.session.commit()
            return ('hey')
        else:
            return ('not yours')
    return ('not found')

@main.route('/businesses/all',methods=['GET','POST'])
def post_all_busn():
    business=Business.query.all()
    businesses=[]
    for business in business:
        businesses.append(business.business_name)
    return render_template('show_all.html',businesses=businesses)

@main.route('/businesses/catalog/all',methods=['GET','POST'])
def get_all_catalog():
    pass

@main.route('/category/<string:cat_name>',methods=['GET','POST'])
def get_categories():
    category=Category.query.filter(name=cat_name).first_or_404()
    businesses=category.businesses.query.all()
    return render_template('catergory.html',category=category,businesses=businesses)


@main.route('/businesses/reviews/<string:busn_name>', methods=['GET','POST'])
def reviews(busn_name):
    form=ReviewForm()
    reviewer=current_user.id
    review=form.review.data
    test_busn=Reviews(review=review)
    db.session.add(test_busn)
    db.session.commit()
    return render_template('reviews.html',form=form)
