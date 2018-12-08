from app import db,login_manager
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.orm import joinedload
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Business(db.Model):
    __tablename__='businesses'
    id=db.Column(db.Integer,primary_key=True)
    business_name=db.Column(db.String(255))
    description=db.Column(db.Text())
    businesses=db.relationship('Reviews',backref='businesses')
    userid=db.Column(db.Integer,db.ForeignKey('users.id'))

    def all_busn(self):
        db.query.options(joinedload('business_name'))

    def del_busn(self):
        db.session.delete(self)
        db.session.commit()


class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),index=True,unique=True)
    email=db.Column(db.String(255),unique=True,index=True)
    phone_number=db.Column(db.Integer)
    passwd=db.Column(db.String(255))
    reviews=db.relationship('Reviews',backref='users')
    businesses=db.relationship('Business',backref='users')
    @property
    def password(self):
        raise AttributeError('You cannot the password attribute')
    @password.setter
    def password(self,password):
        self.passwd=generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.passwd,password)

class Reviews(db.Model):
    __tablename__='reviews'
    id=db.Column(db.Integer,primary_key=True)
    review=db.Column(db.Text,nullable=False)
    businessesid=db.Column(db.Integer,db.ForeignKey('businesses.id'))
    userid=db.Column(db.Integer,db.ForeignKey('users.id'))
    review_date =db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def add_review(self):
        db.session.add(self)
        db.session.commit()

class Catalogue(db.Model):
    __tablename__='catalogues'
    id=db.Column(db.Integer,primary_key=True)
    picture_path=db.Column(db.String())
