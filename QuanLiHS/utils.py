import hashlib
from QuanLiHS import db, app
from QuanLiHS.model import Student, scores
import json


def add_students(name, sex, birthday, address, number, email, id_stu):
    user = Student(name=name.strip(),
                   id_stu=id_stu.strip(),
                   sex=sex.strip(),
                   birthday=birthday.strip(),
                   address=address.strip(),
                   number=number.strip(),
                   email=email.strip())
    db.session.add(user)
    db.session.commit()

def add_scores(name, diem15, diem1t, diemthi):
    diem = scores(name=name.strip(),
                  diem15=diem15.strip(),
                  diem1t=diem1t.strip(),
                  diemthi=diemthi.strip())
    db.session.add(diem)
    db.session.commit()

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)


def load_student():
    student = Student.query.all()
    return student

# def add_list(name, sex, date, address, number, email,**kwargs):
#     HS = Student(name=name.strip(),
#                  sex=sex.strip(),
#                  date=date.strip(),
#                  address=address.strip(),
#                  number=number.strip(),
#                  email=kwargs.get('email'))
#     db.session.add(HS)
#     db.session.commit()

# def check_login(username, password):
#     password =str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#     return User.query.filter
