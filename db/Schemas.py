import string
import datetime
import sqlalchemy as sqa
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from db.AlchemBase import Sqldeclarative


class Basics(Sqldeclarative):
    __tablename__ = 'basic'
    id = sqa.Column(sqa.Integer, autoincrement=True, primary_key=True)
    created = sqa.Column(sqa.DateTime(timezone=True), default=datetime.datetime.utcnow, index=True)
    modidate = sqa.Column(sqa.DateTime(timezone=True), onupdate=func.now())
    name = sqa.Column(sqa.String)
    emailId = sqa.Column(sqa.String, index=True, nullable=True, unique=True)
    password = sqa.Column(sqa.String, index=True, nullable=True)


class Order(Sqldeclarative):
    __tablename__ = 'orders'
    orderid = sqa.Column(sqa.Integer, autoincrement=True, primary_key=True)
    created = sqa.Column(sqa.DateTime(timezone=True), default=datetime.datetime.utcnow)
    modidate = sqa.Column(sqa.DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.now())
    productname = sqa.Column(sqa.String)
    emailId = sqa.Column(sqa.String)
    username = sqa.Column(sqa.String)


class Orderdetails(Sqldeclarative):
    __tablename__ = 'orderdetails'
    id = sqa.Column(sqa.Integer, autoincrement=True, primary_key=True)
    orderid = sqa.Column(sqa.Integer, sqa.ForeignKey("orders.orderid"))
    sku = sqa.Column(sqa.Integer, nullable=True)
    qty = sqa.Column(sqa.Integer)
    created = sqa.Column(sqa.DateTime(timezone=True), default=datetime.datetime.utcnow)
    modidate = sqa.Column(sqa.DateTime(timezone=True), onupdate=func.now())
    name = sqa.Column(sqa.String)
    emailId = sqa.Column(sqa.String, nullable=True)


ormrelation = relationship("Orderdetails", order_by=Orderdetails.id, back_populates='orders')
relation = relationship('Order')


def __repr__(self):
    return "<struct {}".format(self.__tablename__)
