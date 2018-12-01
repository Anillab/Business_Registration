from app import db

def save_object(object):
    db.session.add(object)
    db.session.commit()

class Business(db.Model):
    __tablename__='businesses'
    id=db.Column(db.Integer,primary_key=True)
    Business_Name=db.Column(db.String(255))

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    phone_number=db.Column(db.Integer)
    password=db.Column(db.String(255))
