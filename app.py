from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Настройка базы данных SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'drakon.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель заметки
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(50), default="Аноним")
    recipient = db.Column(db.String(50))  # К какому профилю относится
    likes = db.Column(db.Integer, default=0) # Колонка для лайков
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

# Создаем базу данных
with app.app_context():
    db.create_all()

# Данные профилей
friends_info = {
    "cat": ("Кот", "Просто самый лучший", "cat.jpg", [("Steam", "#")]),
    "ruslan": ("Руслан", "Гей и любит андрея", "ruslan.jpg", [("Steam", "#")]),
    "andrey": ("Андрей", "Опять ест", "andrey.jpg", [("Steam", "#")]),
    "timokha": ("Тимофка", "Жаль что он с нами", "timokha.jpg", [("Steam", "#")]),
    "lesha": ("Лёша", "Низкий не удаленький", "lesha.jpg", [("Steam", "#")]),
    "ibragim": ("Ибрагим", "Почти 12 лет ", "ibragim.jpg", [("Steam", "#")])
}

@app.route('/')
def home():
    friends_list = [(v[0], k) for k, v in friends_info.items()]
    return render_template('index.html', buttons=friends_list, title="DRAKONCHIK V3", is_home=True)

@app.route('/user/<page_name>')
def show_page(page_name):
    data = friends_info.get(page_name)
    if data:
        name, desc, photo, links = data
        notes = Note.query.filter_by