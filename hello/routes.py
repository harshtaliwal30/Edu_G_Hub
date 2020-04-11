import os
from flask import render_template, url_for, redirect, flash
from hello import app, db, bcrypt
from hello.forms import StudentForm, InstructorForm, LoginForm, UploadFileForm
from hello.models import User_student, User_instructor, Instructor_files
from flask_login import login_user, current_user, logout_user, login_required
db.create_all()


@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    form1 = StudentForm()
    form2 = InstructorForm()
    if form1.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form1.password.data).decode('utf-8')
        user1 = User_student(first_name=form1.first_name.data, last_name=form1.last_name.data, email=form1.email.data,
                             password=hashed_password, enrollment_no=form1.enrollment_no.data)
        db.session.add(user1)
        db.session.commit()
        flash(f'Account has been created for {form1.first_name.data} {form1.last_name.data}!', 'success')
        return redirect(url_for('Login_student'))
    if form2.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form2.password.data).decode('utf-8')
        user1 = User_instructor(first_name=form2.first_name.data, last_name=form2.last_name.data,
                                email=form2.email.data, password=hashed_password)
        db.session.add(user1)
        db.session.commit()
        flash(f'Account has been created for {form2.first_name.data} {form2.last_name.data}!', 'success')
        return redirect(url_for('Login_instructor'))
    return render_template('index.html', form1=form1, form2=form2)


@app.route("/Login_student", methods=['GET', 'POST'])
def Login_student():
    if current_user.is_authenticated:
        return redirect(url_for('Collection_student'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User_student.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful as student.', 'success')
            return redirect(url_for('Collection_student'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('Login_student.html', form=form)


@app.route("/Login_instructor", methods=['GET', 'POST'])
def Login_instructor():
    if current_user.is_authenticated:
        return redirect(url_for('Collection_instructor'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User_instructor.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful as instructor.', 'success')
            return redirect(url_for('Collection_instructor'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('Login_instructor.html', form=form)


@app.route("/Applied_chem_student")
# @login_required()
def Applied_chem_student():
    return render_template('Applied_chem_student.html')


@app.route("/Applied_mathematics_student")
# @login_required()
def Applied_mathematics_student():
    return render_template('Applied_mathematics_student.html')


@app.route("/Engineering_thermodynamics_student")
# @login_required()
def Engineering_thermodynamics_student():
    return render_template('Engineering_thermodynamics_student.html')


@app.route("/Electrical_eng_student")
# @login_required()
def Electrical_eng_student():
    return render_template('Electrical_eng_student.html')


@app.route("/Engineering_drawing_student")
# @login_required()
def Engineering_drawing_student():
    return render_template('Engineering_drawing_student.html')


@app.route("/Applied_chem_lab")
# @login_required()
def Applied_chem_lab_student():
    return render_template('Applied_chem_lab_student.html')


def save_file(form_file):
    # random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_file.filename)
    file_fn = f_name + f_ext
    file_path = os.path.join(app.root_path, 'static/' + file_fn)
    form_file.save(file_path)
    return file_fn


@app.route("/Applied_chem_instructor", methods=['GET', 'POST'])
# @login_required
def Applied_chem_instructor():
    form = UploadFileForm()
    if form.validate_on_submit():
        if form.file_upload.data:
            uploaded_file = save_file(form.file_upload.data)
            final_file = Instructor_files(user_file=uploaded_file)
        db.session.add(final_file)
        db.session.commit()
        flash('Your file has been uploaded!', 'success')
        return redirect(url_for('Applied_chem_instructor'))
    # user_file = url_for('static', filename=current_user.user_file)
    all_files = Instructor_files.query.all()
    return render_template('Applied_chem_instructor.html', all_files=all_files, form=form)


@app.route("/Applied_mathematics_instructor")
# @login_required()
def Applied_mathematics_instructor():
    return render_template('Applied_mathematics_instructor.html')


@app.route("/Engineering_thermodynamics_instructor")
# @login_required()
def Engineering_thermodynamics_instructor():
    return render_template('Engineering_thermodynamics_instructor.html')


@app.route("/Electrical_eng_instructor")
# @login_required()
def Electrical_eng_instructor():
    return render_template('Electrical_eng_instructor.html')


@app.route("/Engineering_drawing_instructor")
# @login_required()
def Engineering_drawing_instructor():
    return render_template('Engineering_drawing_instructor.html')


@app.route("/Applied_chem_lab_instructor")
# @login_required()
def Applied_chem_lab_instructor():
    return render_template('Applied_chem_lab_instructor.html')


@app.route("/Collection_student")
# @login_required()
def Collection_student():
    return render_template('Collection_student.html')


@app.route("/Collection_instructor")
# @login_required()
def Collection_instructor():
    return render_template('Collection_instructor.html')


@app.route("/doubt")
@login_required
def doubt():
    import tkinter as tk
    from tkinter import Menu
    from tkinter import ttk

    def _quit():
        win.quit()
        win.destroy()
        exit()

    win = tk.Tk()
    win.title("Edu_G_Hub")

    menu_bar = Menu()
    win.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=_quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About")
    menu_bar.add_cascade(label="Help", menu=help_menu)

    tab_control = ttk.Notebook(win)

    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Tab 1')

    tab_control.pack(expand=1, fill="both")

    Teachers_frame = ttk.Labelframe(tab1, text='TimeTable')
    Teachers_frame.grid(column=0, row=0, padx=8, pady=4)
    Teachers_frame.grid_configure(column=0, row=1, padx=8, pady=4)

    Teachers = ttk.LabelFrame(tab1, text='Latest Observation for ')
    Teachers.grid(column=0, row=0, padx=8, pady=4)

    ttk.Label(Teachers, text="Teacher's Name:  ").grid(column=0, row=0)

    Teach = tk.StringVar()
    TeachSelected = ttk.Combobox(Teachers, width=24, textvariable=Teach)
    TeachSelected['values'] = ('Teacher 1', 'Teacher 2', 'Teacher 3', 'Teacher 4', 'Teacher 5', 'Teacher 6',
                               'Teacher 7', 'Teacher 8', 'Teacher 9')
    TeachSelected.grid(column=1, row=0)
    TeachSelected.current(0)

    max_width = max([len(x) for x in TeachSelected['values']])
    new_width = max_width - 4
    TeachSelected.config(width=new_width)

    ENTRY_WIDTH = max_width + 3
    ttk.Label(Teachers_frame, text="8-8:50:").grid(column=0, row=1, sticky='W')
    Time1 = tk.StringVar()
    Time1Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time1, state='readonly')
    Time1Entry.grid(column=1, row=1, sticky='W')

    ttk.Label(Teachers_frame, text="8:50-9:40:").grid(column=0, row=2, sticky='W')
    Time2 = tk.StringVar()
    Time2Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time2, state='readonly')
    Time2Entry.grid(column=1, row=2, sticky='W')

    ttk.Label(Teachers_frame, text="9:40-10:30:").grid(column=0, row=3, sticky='W')
    Time3 = tk.StringVar()
    Time3Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time3, state='readonly')
    Time3Entry.grid(column=1, row=3, sticky='W')

    ttk.Label(Teachers_frame, text="10:30-11:20:").grid(column=0, row=4, sticky='W')
    Time4 = tk.StringVar()
    Time4Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time4, state='readonly')
    Time4Entry.grid(column=1, row=4, sticky='W')

    ttk.Label(Teachers_frame, text="11:20-12:10:").grid(column=0, row=5, sticky='W')
    Time5 = tk.StringVar()
    Time5Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time5, state='readonly')
    Time5Entry.grid(column=1, row=5, sticky='W')

    ttk.Label(Teachers_frame, text="12:10-1:00:").grid(column=0, row=6, sticky='W')
    Time6 = tk.StringVar()
    Time6Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time6, state='readonly')
    Time6Entry.grid(column=1, row=6, sticky='W')

    ttk.Label(Teachers_frame, text="1:00-2:00:").grid(column=0, row=7, sticky='W')
    Time7 = tk.StringVar()
    Time7Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time7, state='readonly')
    Time7Entry.grid(column=1, row=7, sticky='W')

    ttk.Label(Teachers_frame, text="2:00-4:00:").grid(column=0, row=8, sticky='W')
    Time8 = tk.StringVar()
    Time8Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time8, state='readonly')
    Time8Entry.grid(column=1, row=8, sticky='W')

    ttk.Label(Teachers_frame, text="4:00-5:00:").grid(column=0, row=10, sticky='W')
    Time9 = tk.StringVar()
    Time9Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time9, state='readonly')
    Time9Entry.grid(column=1, row=10, sticky='W')

    for child in Teachers_frame.winfo_children():
        child.grid_configure(padx=6, pady=6)
        child.grid_configure(padx=4, pady=2)

    ttk.Label(Teachers, text="Teacher's Name:  ").grid(column=0, row=0)

    city = tk.StringVar()
    citySelected = ttk.Combobox(Teachers, width=24, textvariable=city)
    citySelected['values'] = ('Teacher 1', 'Teacher 2', 'Teacher 3', 'Teacher 4', 'Teacher 5', 'Teacher 6',
                              'Teacher 7', 'Teacher 8', 'Teacher 9')
    citySelected.grid(column=1, row=0)
    citySelected.current(0)

    Dictionary = {'Teacher 1': {'8:00-8:50': 'Class-A1A', '8:50-9:40': 'Class-A1B', '9:40-10:30': 'Class-A1C',
                                '10:30-11:20': 'Chamber', '11:20-12:10': 'Chamber', '12:10-1:00': 'Class-A1D',
                                '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Chemistry Lab', '4:00-5:00': 'Chamber'},

                  'Teacher 2': {'8:00-8:50': 'NA', '8:50-9:40': 'Chamber', '9:40-10:30': 'Class-A1D',
                                '10:30-11:20': 'Class-A1A', '11:20-12:10': 'Class-A1B', '12:10-1:00': 'Class-A1E',
                                '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Chemistry Lab'},

                  'Teacher 3': {'8:00-8:50': 'Class-A1B', '8:50-9:40': 'Class-A1C', '9:40-10:30': 'Chamber',
                                '10:30-11:20': 'Chamber', '11:20-12:10': 'Chamber', '12:10-1:00': 'Class-A1A',
                                '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Physics Lab'},

                  'Teacher 4': {'8:00-8:50': 'Class-A1C', '8:50-9:40': 'Class-A1D', '9:40-10:30': 'Chamber',
                                '10:30-11:20': 'Chamber', '11:20-12:10': 'Chamber', '12:10-1:00': 'Class-A1B',
                                '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Physics Lab'},

                  'Teacher 5': {'8:00-8:50': 'NA', '8:50-9:40': 'Chamber', '9:40-10:30': 'Class-A1E',
                                '10:30-11:20': 'Chamber', '11:20-12:10': 'Class A1A', '12:10-1:00': 'Class-A1C',
                                '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Computer Lab'},

                  'Teacher 6': {'8:00-8:50': 'Class-A1D', '8:50-9:40': 'Class-A1A', '9:40-10:30': 'Chamber',
                                '10:30-11:20': 'Class-A1E', '11:20-12:10': 'Chamber', '12:10-1:00': 'NA',
                                '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Computer Lab'},

                  'Teacher 7': {'8:00-8:50': 'NA', '8:50-9:40': 'Class-A1E', '9:40-10:30': 'Class-A1A',
                                '10:30-11:20': 'Chamber', '11:20-12:10': 'Chamber', '12:10-1:00': 'Chamber',
                                '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Manufacturing Lab'},

                  'Teacher 8': {'8:00-8:50': 'NA', '8:50-9:40': 'Chamber', '9:40-10:30': 'Class-A1B',
                                '10:30-11:20': 'Class-A1D', '11:20-12:10': 'Class-A1E', '12:10-1:00': 'Chamber',
                                '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Manufacturing Lab'},

                  'Teacher 9': {'8:00-8:50': 'NA', '8:50-9:40': 'Class-A1A', '9:40-10:30': 'Chamber',
                                '10:30-11:20': 'Class-A1C', '11:20-12:10': 'Class-A1D', '12:10-1:00': 'NA',
                                '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Engineering Graphics Lab'},

                  'Teacher 10': {'8:00-8:50': 'Class-A1E', '8:50-9:40': 'Chamber', '9:40-10:30': 'Chamber',
                                 '10:30-11:20': 'Class-A1B', '11:20-12:10': 'Class-A1C', '12:10-1:00': 'Chamber',
                                 '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Engineering Graphics Lab'}}

    Time1.set(Dictionary['Teacher 1']['8:00-8:50'])
    Time2.set(Dictionary['Teacher 1']['8:50-9:40'])
    Time3.set(Dictionary['Teacher 1']['9:40-10:30'])
    Time4.set(Dictionary['Teacher 1']['10:30-11:20'])
    Time5.set(Dictionary['Teacher 1']['11:20-12:10'])
    Time6.set(Dictionary['Teacher 1']['12:10-1:00'])
    Time7.set(Dictionary['Teacher 1']['1:00-2:00'])
    Time8.set(Dictionary['Teacher 1']['2:00-4:00'])
    Time9.set(Dictionary['Teacher 1']['4:00-5:00'])

    win.mainloop()
    return redirect(url_for('index'))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))
