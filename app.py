from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "drakon_secret_key_1337"

# Настройка базы данных
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'drakon.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель заметок
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(50), default="Аноним")
    recipient = db.Column(db.String(50))
    likes = db.Column(db.Integer, default=0)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

# Данные профилей
friends_info = {
    "cat": ("Кот", "Просто самый лучший", "cat.jpg", [("Steam", "#")]),
    "ruslan": ("Руслан", "Мастер тактических решений", "ruslan.jpg", [("Steam", "#")]),
    "andrey": ("Андрей", "Легенда состава. Спокойствие — его конек.", "andrey.jpg", [("Steam", "#")]),
    "timokha": ("Тимофка", "Всегда на связи, когда нужно затащить", "timokha.jpg", [("Steam", "#")]),
    "lesha": ("Лёша", "Низкий, но очень удаленький", "lesha.jpg", [("Steam", "#")]),
    "ibragim": ("Ибрагим", "Молодой талант с огромным потенциалом", "ibragim.jpg", [("Steam", "#")])
}

@app.route('/')
def home():
    friends_list = [(v[0], k) for k, v in friends_info.items()]
    return render_template('index.html', buttons=friends_list, title="DRAGON PROJECT", is_home=True)

@app.route('/user/<page_name>')
def show_page(page_name):
    data = friends_info.get(page_name)
    if data:
        name, desc, photo, links = data
        notes = Note.query.filter_by(recipient=page_name).order_by(Note.date_posted.desc()).all()
        return render_template('index.html', title=name, description=desc, photo=photo, 
                               links=links, is_home=False, notes=notes, page_id=page_name)
    return "Пользователь не найден", 404

@app.route('/add_note/<recipient>', methods=['POST'])
def add_note(recipient):
    content = request.form.get('content')
    author = request.form.get('author') or "Аноним"
    if content:
        new_note = Note(content=content, author=author, recipient=recipient, likes=0)
        db.session.add(new_note)
        db.session.commit()
    return redirect(url_for('show_page', page_name=recipient))

@app.route('/like/<int:note_id>', methods=['POST'])
def like_note(note_id):
    note = Note.query.get_or_404(note_id)
    note.likes = (note.likes or 0) + 1
    db.session.commit()
    return redirect(url_for('show_page', page_name=note.recipient))

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    password = request.form.get('password')
    note = Note.query.get_or_404(note_id)
    recipient = note.recipient
    if password == "1234": # Твой секретный пароль
        db.session.delete(note)
        db.session.commit()
    return redirect(url_for('show_page', page_name=recipient))

if __name__ == '__main__':
    app.run(debug=True)