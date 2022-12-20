from QuanLiHS import admin, db
from QuanLiHS.model import Student, Admin, scores,Mon
from flask_admin.contrib.sqla import ModelView


admin.add_view(ModelView(Student, db.session))
admin.add_view(ModelView(scores, db.session))
admin.add_view(ModelView(Mon, db.session))

