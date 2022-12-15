# from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, Enum, DateTime
# from sqlalchemy.orm import relationship
# from QuanLiHS import db, app
# from enum import Enum as UserEnum
# from flask_login import UserMixin
# class User(BaseModel, UserMixin):


import hashlib
from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship, backref
from QuanLiHS import app, db
from enum import Enum as UserEnum
from flask_login import UserMixin
from datetime import datetime


# class UserRole(UserEnum):
#     USER = 1
#     ADMIN = 2


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Admin(BaseModel):
    __tablename__ = 'Admin'
    name = Column(String(50), nullable=False)
    major = Column(String(50), nullable=False)
    password = Column(String(100))
    # patients = relationship('Patient', backref='admin', lazy=False)

    def __str__(self):
        return self.name


class Students(BaseModel):
    __tablename__ = 'Students'
    # student_id = Column(Integer, ForeignKey(Admin.id))
    stu_name = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    year = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)


    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        password1 = str(hashlib.md5('1'.encode('utf-8')).hexdigest())
        password2 = str(hashlib.md5('2'.encode('utf-8')).hexdigest())
        password3 = str(hashlib.md5('3'.encode('utf-8')).hexdigest())
        admin1 = Admin(name='manager', major='manager', password=password1)
        admin2 = Admin(name='school-staff', major='school-staff', password=password2)
        admin3 = Admin(name='teacher', major='teacher', password=password3)
        db.session.add(admin1)
        db.session.add(admin2)
        db.session.add(admin3)
        db.session.commit()