from hello import db, login_manager1, login_manager2
from flask_login import UserMixin


@login_manager2.user_loader
def load_user_instructor(user_id):
    return User_instructor.query.get(int(user_id))


@login_manager1.user_loader
def load_user_student(user_id):
    return User_student.query.get(int(user_id))


class User_student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    enrollment_no = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.email}')"


class User_instructor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.email}')"


class Instructor_files(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_file = db.Column(db.String(100), nullable=False, default='default.pdf')

    def __repr__(self):
        return f"'{self.user_file}'"