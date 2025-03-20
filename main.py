from data import db_session
from data.users import User
from flask import Flask
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    db_sess = db_session.create_session()

    users_data = [
        {"surname": "Scott", "name": "Ridley", "age": 21, "position": "captain",
         "speciality": "research engineer", "address": "module_1", "email": "scott_chief@mars.org"},
        {"surname": "Случайный", "name": "Рэнди", "age": 21, "position": "рассказчик",
         "speciality": "рандомайзер", "address": "Модуль_1", "email": "rendi@mars.rimworld"},
        {"surname": "Мамут", "name": "Рахал", "age": 43, "position": "Механик",
         "speciality": "Автомеханик", "address": "Модуль_2", "email": "rahalmamyt@mars.ru"},
        {"surname": "Morgan", "name": "Dexter", "age": 21, "position": "Полицейский",
         "speciality": "Специалист по анализу брызг крови", "address": "modul_Maimi", "email": "dexer149@mars.org"}
    ]

    for user_data in users_data:
        if not db_sess.query(User).filter(User.email == user_data["email"]).first():
            user = User(**user_data)
            db_sess.add(user)
            db_sess.commit()

    job_data = {
        "team_leader": 1,
        "job": "deployment of residential modules 1 and 2",
        "work_size": 15,
        "collaborators": "2, 3",
        "start_date": datetime.datetime.now(),
        "is_finished": False
    }

    if not db_sess.query(Jobs).filter(Jobs.job == job_data["job"]).first():
        job = Jobs(**job_data)
        db_sess.add(job)
        db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()