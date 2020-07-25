import json
from random import shuffle

from flask import render_template, request
from forms import BookingForm, RequestForm
from models import Teacher, Booking, Request
from stepik_study import app, db


def read_file(filename):
    opened_file = open(filename, 'r')
    config_content = opened_file.read()
    data = json.loads(config_content)
    opened_file.close()
    return data


weekdays_ru = {"mon": "Понедельник", "tue": "Вторник", "wed": "Среда", "thu": "Четверг", "fri": "Пятница",
               "sat": "Суббота", "sun": "Воскресенье"}


@app.context_processor
def globalvars():
    return dict(weekdays_ru=weekdays_ru)


@app.route("/")
def index():
    goals_names = read_file("goals.json")
    teachers = db.session.query(Teacher).all()
    shuffle(teachers)
    random_teachers = teachers[:6]
    output = render_template('index.html', goals_names=goals_names, random_teachers=random_teachers)
    return output


@app.route("/goals/<goal>")
def goals_page(goal):
    teachers = db.session.query(Teacher).all()
    goals = read_file('goals.json')
    filtered_teachers = []
    for teacher in teachers:
        if goal in teacher.goals:
            filtered_teachers.append(teacher)
    output = render_template('goal.html', goals=goals, goal=goal, teachers=teachers,
                             filtered_teachers=filtered_teachers)
    return output


@app.route("/profiles/<int:teacher_id>/")
def about_teacher(teacher_id):
    goals_names = read_file("goals.json")
    teacher = db.session.query(Teacher).get(teacher_id)
    teacher_free = json.loads(teacher.free)
    profile_goals = []
    for goals_items in goals_names:
        for abbr, goal_name in goals_items.items():
            if abbr in teacher.goals:
                profile_goals.append(goal_name)
    output = render_template('profile.html', teacher_id=teacher_id, teacher=teacher, goals_names=goals_names,
                             teacher_free=teacher_free, profile_goals=profile_goals)
    return output


@app.route("/request/", methods=['GET', 'POST'])
def selection_request():
    form = RequestForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        goal = form.goal.data
        date = form.date.data
        formrequest = Request(name=name, phone=phone, goal=goal, date=date)
        db.session.add(formrequest)
        db.session.commit()
        return render_template("request_done.html", form=form, name=name, phone=phone, goal=goal, date=date)
    else:
        output = render_template("request.html", form=form)
        return output


@app.route("/booking/<int:teacher_id>/<weekday>/<time>/", methods=['GET', 'POST'])
def booking_card(teacher_id, weekday, time):
    teacher = db.session.query(Teacher).get(teacher_id)
    form = BookingForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.client_name.data
        phone = form.client_phone.data
        weekday = form.client_weekday.data
        time = form.client_time.data
        teacher_id = form.client_teacher.data
        booking = Booking(name=name, phone=phone, teacher_id=teacher_id)
        db.session.add(booking)
        db.session.commit()
        return render_template('booking_done.html', form=form, teacher=teacher, weekday=weekday, time=time, name=name,
                               phone=phone)

    return render_template('booking.html', form=form, teacher=teacher, weekday=weekday, time=time)
