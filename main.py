from data import db_session
from data.users import User
from flask import Flask
import sqlite3
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")

    curs = sqlite3.connect("db/blogs.sqlite")
    info = curs.execute('SELECT * FROM users WHERE surname=?', ("Scott",)).fetchone()
    if len(info) == 0:
        user = User()
        user.surname = "Scott"
        user.name = "Ridley"
        user.age = 21
        user.position = "captain"
        user.speciality = "research engineer"
        user.address = "module_1"
        user.email = "scott_chief@mars.org"
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
    info = curs.execute('SELECT * FROM users WHERE surname=?', ("Случайный",)).fetchone()
    if len(info) == 0:
        user = User()
        user.surname = "Случайный"
        user.name = "Рэнди"
        user.age = 21
        user.position = "рассказчик"
        user.speciality = "рандомайзер"
        user.address = "Модуль_1"
        user.email = "rendi@mars.rimworld"
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
    info = curs.execute('SELECT * FROM users WHERE surname=?', ("Мамут",)).fetchone()
    if len(info) == 0:
        user = User()
        user.surname = "Мамут"
        user.name = "Рахал"
        user.age = 43
        user.position = "Механик"
        user.speciality = "Автомеханик"
        user.address = "Модуль_2"
        user.email = "rahalmamyt@mars.ru"
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
    info = curs.execute('SELECT * FROM users WHERE surname=?', ("Morgan",)).fetchone()
    if len(info) == 0:
        user = User()
        user.surname = "Morgan"
        user.name = "Dexter"
        user.age = 21
        user.position = "Полицейский"
        user.speciality = "Специалист по анализу брызг крови"
        user.address = "modul_Maimi"
        user.email = "dexer149@mars.org"
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
    info = curs.execute('SELECT * FROM jobs WHERE team_leader=?', (1,)).fetchone()
    if info is None:
        job = Jobs()
        job.team_leader = 1
        job.job = "deployment of residential modules 1 and 2"
        job.work_size = 15
        job.collaborators = "2, 3"
        job.start_date = datetime.datetime.now()
        job.is_finished = False
        db_sess = db_session.create_session()
        db_sess.add(job)
        db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()

