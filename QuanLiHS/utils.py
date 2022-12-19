import hashlib
from QuanLiHS import db, app
from QuanLiHS.model import Student
import json, os




def add_students(username, gender, birthday, address, number_phone, mail):
    user = Student(username=username.strip(),
                   gender=gender.strip(),
                   birthday=birthday.strip(),
                   address=address.strip(),
                   number_phone=number_phone.strip(),
                   mail=mail.strip())
    db.session.add(user)
    db.session.commit()


def read_json(path):
    with open(path, "r") as f:
        return json.load(f)


def load_student():
    student = Student.query.all()
    return student

# def add_list(name, sex, date, address, number, email):


# def check_login(username, password):
#     password =str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#     return User.query.filter
