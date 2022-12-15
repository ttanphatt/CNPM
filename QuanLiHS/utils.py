import hashlib
from QuanLiHS import db
from QuanLiHS.model import Students


def add_students(username, gender, year, address):
    user = Students(username=username.strip(),
                   gender=gender.strip(),
                   year=year.strip(),
                   address=address.strip())

    db.session.add(user)
    db.session.commit()

# def check_login(username, password):
#     password =str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#     return User.query.filter
