from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

from .extenctions import db


class Login(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    nick = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(80), nullable=True)
    password = db.Column(db.String(100), nullable=True)
    data_rejestracji = db.Column(db.DateTime(timezone=True), default=func.now())
    products = db.relationship("Products")


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    brand = db.Column(db.Integer, db.ForeignKey('brand.id'))
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200), nullable=False, default='default.png')
    id_user = db.Column(db.Integer, db.ForeignKey('login.id'))
    barcode = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime(timezone=True), nullable=True, default=func.now())
    rating = db.Column(db.Float)


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    date = db.Column(db.DateTime, nullable=True)
    products = db.relationship("Products")


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('login.id'))
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    comment = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float)
    date = db.Column(db.DateTime, nullable=True, default=datetime.now())
    user = db.relationship("Login")
