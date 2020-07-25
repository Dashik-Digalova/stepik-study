from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, validators


class RequestForm(FlaskForm):
    name = StringField('name', [validators.input_required(message="Введите что-нибудь"), validators.length(min=2, message="Поле должно содержать минимум два символа")])
    phone = StringField('phone', [validators.input_required(message="Введите что-нибудь"), validators.length(min=7, message="Слишком короткая строка")])
    goal = RadioField('goal', choices=[("Для путешествий", "Для путешествий"), ("Для учебы", "Для учебы"),
                                       ("Для работы", "Для работы"), ("Для переезда", "Для переезда")],
                      default="Для путешествий")
    date = RadioField('date', choices=[("1-2", "1-2"), ("3-5", "3-5"), ("5-7", "5-7"), ("7-10", "7-10")], default="1-2")


class BookingForm(FlaskForm):
    client_teacher = StringField('client_teacher')
    client_weekday = StringField('client_weekday')
    client_time = StringField('client_time')
    client_name = StringField('client_name', [validators.InputRequired(message="Введите что-нибудь")])
    client_phone = StringField('client_phone', [validators.Length(min=7, message="Слишком короткая строка")])