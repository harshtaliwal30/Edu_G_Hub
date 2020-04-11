from flask_wtf import FlaskForm
# from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from hello.models import User_student, User_instructor


class StudentForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    enrollment_no = StringField('Enrollment No.', validators=[DataRequired(), Length(min=6, max=6)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    apply = SubmitField('Apply Now')

    def validate_enrollment_no(self, enrollment_no):
        # if enrollment_no.data != current_user.enrollment_no:
        user = User_student.query.filter_by(enrollment_no=enrollment_no.data).first()
        if user:
            raise ValidationError('That enrollment_no is taken. Please choose a different one.')

    def validate_email(self, email):
        # if email.data != current_user.email:
        user = User_student.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class InstructorForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    apply = SubmitField('Apply Now')

    def validate_email(self, email):
        # if email.data != current_user.email:
        user = User_instructor.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    apply = SubmitField('LOGIN')


class UploadFileForm(FlaskForm):
    file_upload = FileField('Choose File', validators=[FileAllowed(['txt', 'pdf', 'doc', 'docx', 'rtf'])])
    upload = SubmitField('Upload')