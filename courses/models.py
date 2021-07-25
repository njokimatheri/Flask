from courses import db, login_manager
from courses import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    items = db.relationship('item', backref='owned_user', lazy=True)

@password.setter
def password(self, plain_text_password):
    self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

def check_password_correction(self, attempted_password):
    return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Course(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    course_name = db.Column(db.String(length=30), nullable=False, unique=True)
    charges = db.Column(db.Integer(), nullable=False)
    duration = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f'course {self.name}'