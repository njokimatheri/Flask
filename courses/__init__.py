from flask import Flask,render_template
from  flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///course.db'
app.config['SECRET_KEY']='1767318e2dca11591278857f'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
# for the login required in course page.This must be declared
login_manager.login_view="login_page"
# the messgae to be displayed will be of this colour
login_manager.login_message_category='info'


from courses import routes
