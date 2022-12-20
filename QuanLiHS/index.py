import hashlib
from flask import render_template,  url_for, redirect
from QuanLiHS import app, utils
from flask import request
from QuanLiHS.model import Admin
from QuanLiHS.admin import *
import utils

@app.route("/")
def home():
    return render_template("index.html")

# @app.route('/user-login', methods=['get', 'post'])
# def user_signin():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]


@app.route("/login", methods=['get', 'post'])
def login():
    err_msg = ''
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        password = request.form.get('password')
        admins = Admin.query.all()
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        for ad in admins:
            if ad.name == name and ad.password == password:
                if ad.name == "school-staff":
                    return render_template('school-staff.html')
                if ad.name == "teacher":
                    student = utils.load_student()
                    return render_template('teacher.html', Student=student)
            else:
                err_msg = 'User hoac mat khau khong chinh xac'

    return render_template('index.html', err_msg=err_msg)

@app.route("/XuatDiem")
def XuatDiem():
    diem =utils.out_scores()
    return render_template('XuatDiem.html', scores=diem)

@app.route("/Student")
def Student_list():
    student = utils.load_student()
    return render_template('teacher.html',
                           Student=student)


@app.route('/school_staff', methods=['get', 'post'])
def get_list():
    err_msg = ""
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        sex = request.form.get('sex')
        birthday = request.form.get('birthday')
        address = request.form.get('address')
        number = request.form.get('number')
        email = request.form.get('email')

        try:
            utils.add_students(name=name, sex=sex,  birthday=birthday, address=address, number=number, email=email)

        except Exception as ex:
            err_msg = "Co loi" + str(ex)
    return render_template('index.html', err_msg=err_msg)


@app.route('/teacher',  methods=['get', 'post'])
def get_scores():
    err_msg1 = ""
    if request.method.__eq__('POST'):
        diem15 = request.form.get('diem15')
        diem1t = request.form.get('diem1t')
        diemthi = request.form.get('diemthi')

        try:
            utils.add_scores(diem15=diem15, diem1t=diem1t, diemthi=diemthi)

        except Exception as ex:
            err_msg = "Co loi" + str(ex)
    return render_template('index.html', err_msg=err_msg1)


if __name__ == '__main__':
    app.run(debug=True)

