import hashlib
from flask import render_template
from QuanLiHS import app, utils
from flask import request
from QuanLiHS.model import Admin


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
                if ad.name == "manager":
                    return render_template('manager.html')
                if ad.name == "school-staff":
                    return render_template('school-staff.html')
                if ad.name == "teacher":
                    return render_template('teacher.html')
            else:
                err_msg = 'User hoac mat khau khong chinh xac'

    return render_template('index.html', err_msg=err_msg)


if __name__ == '__main__':
    app.run(debug=True)

