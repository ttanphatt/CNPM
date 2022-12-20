

import hashlib

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship, backref
from QuanLiHS import app, db
from enum import Enum as UserEnum
from flask_login import UserMixin




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


class DanhSachLop(BaseModel):
    __tablename__ = 'DanhSachLop'
    TenLop = Column(String(50), nullable=False)
    Siso = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class Student(BaseModel):
    __tablename__ = 'Students'
    name = Column(String(50), nullable=False)
    sex = Column(String(50), nullable=False)
    birthday = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    number = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)



    def __str__(self):
        return self.name


class scores(BaseModel):
    __tablename__ = 'scores'
    id_stu = Column(Integer, ForeignKey(Student.id), nullable=False)
    name = Column(String(50), nullable=False)
    diem15 = Column(String(50), nullable=False)
    diem1t = Column(String(50), nullable=False)
    diemthi = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class Mon(BaseModel):
    __tablename__ = 'Mon'
    Monhoc = Column(String(50), nullable=False)
    HocKy = Column(String(50), nullable=False)
    NamHoc = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class LopHoc(BaseModel):
    __tablename__ = 'Lop Hoc'
    Lop_name = Column(String(50), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        password2 = str(hashlib.md5('2'.encode('utf-8')).hexdigest())
        password3 = str(hashlib.md5('3'.encode('utf-8')).hexdigest())
        admin2 = Admin(name='school-staff', major='school-staff', password=password2)
        admin3 = Admin(name='teacher', major='teacher', password=password3)
        db.session.add(admin2)
        db.session.add(admin3)
        db.session.commit()
