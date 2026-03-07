from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Настройка базы данных SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'notes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель заметки
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(50), default="Аноним")
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

# Создаем базу данных внутри контекста приложения
with app.app_context():
    db.create_all()

friends_list = [
    ("Кот", "cat"), ("Руслан", "ruslan"), ("Андрей", "andrey"),
    ("Тимофка", "timokha"), ("Лёша", "lesha"), ("Ибрагим", "ibragim")
]

friends_info = {
    "cat": ("Кот", "Просто самый лучший", "cat.jpg", [("Steam", "#")]),
    "ruslan": ("Руслан", "Гей и любит Андрея", "ruslan.jpg", [("Steam", "#")]),
    "andrey": ("Андрей", "Опять ест", "andrey.jpg", [("Steam", "#")]),
    "timokha": ("Тимофка", "Жаль, что он с нами", "timokha.jpg", [("Steam", "#")]),
    "lesha": ("Лёша", "Низкий, но удаленький", "lesha.jpg", [("Steam", "#")]),
    "ibragim": ("Ибрагим", "Почти 12 лет", "ibragim.jpg", [("Steam", "#")])
}

@app.route('/')
def home():
    notes = Note.query.order_by(Note.date_posted.desc()).all()
    return render_template('index.html', buttons=friends_list, title="DRAKONCHIK OS", is_home=True, notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    content = request.form.get('content')
    author = request.form.get('author') or "Аноним"
    if content:
        new_note = Note(content=content, author=author)
        db.session.add(new_note)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/<page_name>')
def show_page(page_name):
    data = friends_info.get(page_name)
    if data:
        name, desc, photo, links = data
        return render_template('index.html', title=name, description=desc, photo=photo, links=links, is_home=False)
    return "404 Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)