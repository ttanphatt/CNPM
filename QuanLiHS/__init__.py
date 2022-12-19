
from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin



app = Flask(__name__)
app.secret_key = 'bugdhbcuijnfiurfhdjdfiidhj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/data?charset=utf8mb4' % quote('My021102@')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app=app)

admin = Admin(app=app, name='Quản Trị', template_mode='bootstrap4')






