from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "dragon_mega_secret_key_99" # Ключ для работы сессий

# Настройка базы данных
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'drakon.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Таблица пользователей
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Таблица заметок
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(50), default="Аноним")
    recipient = db.Column(db.String(50))
    likes = db.Column(db.Integer, default=0)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

# Данные твоих друзей
friends_info = {
    "cat": ("Кот", "Просто самый лучший", "cat.jpg"),
    "ruslan": ("Руслан", "Мастер тактических решений", "ruslan.jpg"),
    "andrey": ("Андрей", "Легенда состава. Спокойствие врагов пугает.", "andrey.jpg"),
    "timokha": ("Тимофка", "Всегда в деле, когда нужно затащить", "timokha.jpg"),
    "lesha": ("Лёша", "Низкий не удаленький", "lesha.jpg"),
    "ibragim": ("Ибрагим", "Молодой талант с огромным потенциалом", "ibragim.jpg")
}

# --- АВТОРИЗАЦИЯ ---

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip().lower()
        password = request.form.get('password')
        if User.query.filter_by(username=username).first():
            return "Такой ник уже занят!"
        
        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('index.html', is_home=False, auth_mode='register', title="Регистрация")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip().lower()
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user'] = user.username
            return redirect(url_for('home'))
        return "Неверный логин или пароль!"
    return render_template('index.html', is_home=False, auth_mode='login', title="Вход")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# --- ОСНОВНЫЕ СТРАНИЦЫ ---

@app.route('/')
def home():
    friends_list = [(v[0], k) for k, v in friends_info.items()]
    return render_template('index.html', buttons=friends_list, title="DRAGON", is_home=True)

@app.route('/user/<page_name>')
def show_page(page_name):
    data = friends_info.get(page_name)
    if data:
        name, desc, photo = data
        notes = Note.query.filter_by(recipient=page_name).order_by(Note.date_posted.desc()).all()
        return render_template('index.html', title=name, description=desc, photo=photo, 
                               is_home=False, notes=notes, page_id=page_name, auth_mode=None)
    return "404", 404

@app.route('/add_note/<recipient>', methods=['POST'])
def add_note(recipient):
    content = request.form.get('content')
    author = session.get('user', "Аноним")
    if content:
        new_note = Note(content=content, author=author, recipient=recipient)
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
    note = Note.query.get_or_404(note_id)
    # Удалить может автор сообщения или админ
    if session.get('user') == note.author or session.get('user') == 'admin':
        db.session.delete(note)
        db.session.commit()
    return redirect(url_for('show_page', page_name=note.recipient))

if __name__ == '__main__':
    app.run(debug=True)