from QuanLiHS import admin, db
from QuanLiHS.model import Student, Admin
from flask_admin.contrib.sqla import ModelView


admin.add_view(ModelView(Student, db.session))

