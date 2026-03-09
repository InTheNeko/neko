from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "dragon_final_key_2026"

# Настройки базы данных и папки для фото
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'drakon.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')

db = SQLAlchemy(app)

# Секретный пароль для редактирования профилей
ADMIN_PASSWORD = "1234" 

# Таблица профилей (сохраняется навсегда)
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    display_name = db.Column(db.String(50))
    bio = db.Column(db.String(500))
    photo = db.Column(db.String(100))

# Таблица заметок
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(50), default="Аноним")
    recipient = db.Column(db.String(50))
    likes = db.Column(db.Integer, default=0)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

# Создание базы и начальное заполнение
with app.app_context():
    db.create_all()
    
    initial_squad = {
        "cat": ("Кот", "Просто самый лучший", "cat.jpg"),
        "ruslan": ("Руслан", "Мастер тактических решений", "ruslan.jpg"),
        "andrey": ("Андрей", "Легенда состава. Спокойствие и мощь.", "andrey.jpg"),
        "timokha": ("Тимофка", "Всегда в деле", "timokha.jpg"),
        "lesha": ("Лёша", "Низкий не удаленький", "lesha.jpg"),
        "ibragim": ("Ибрагим", "Молодой талант", "ibragim.jpg")
    }

    for nick, (name, bio, img) in initial_squad.items():
        if not UserProfile.query.filter_by(username=nick).first():
            new_p = UserProfile(username=nick, display_name=name, bio=bio, photo=img)
            db.session.add(new_p)
    db.session.commit()

@app.route('/')
def home():
    profiles = UserProfile.query.all()
    buttons = [(p.display_name, p.username) for p in profiles]
    return render_template('index.html', buttons=buttons, title="DRAGON SQUAD", is_home=True)

@app.route('/user/<page_name>')
def show_page(page_name):
    user = UserProfile.query.filter_by(username=page_name).first_or_404()
    notes = Note.query.filter_by(recipient=page_name).order_by(Note.date_posted.desc()).all()
    return render_template('index.html', user=user, title=user.display_name, 
                           is_home=False, notes=notes, page_id=page_name)

@app.route('/edit_profile/<page_name>', methods=['POST'])
def edit_profile(page_name):
    if request.form.get('admin_password') != ADMIN_PASSWORD:
        return "Неверный пароль!", 403
    
    user = UserProfile.query.filter_by(username=page_name).first_or_404()
    user.bio = request.form.get('description')
    
    file = request.files.get('photo')
    if file and file.filename != '':
        filename = secure_filename(f"upd_{page_name}.jpg")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user.photo = filename
        
    db.session.commit()
    return redirect(url_for('show_page', page_name=page_name))

@app.route('/add_note/<recipient>', methods=['POST'])
def add_note(recipient):
    content = request.form.get('content')
    if content:
        note = Note(content=content, author=request.form.get('author') or "Аноним", recipient=recipient)
        db.session.add(note)
        db.session.commit()
    return redirect(url_for('show_page', page_name=recipient))

@app.route('/like/<int:note_id>', methods=['POST'])
def like_note(note_id):
    note = Note.query.get_or_404(note_id)
    note.likes += 1
    db.session.commit()
    return redirect(url_for('show_page', page_name=note.recipient))

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    if request.form.get('password') == "1234":
        note = Note.query.get_or_404(note_id)
        db.session.delete(note)
        db.session.commit()
    return redirect(request.referrer)

if __name__ == '__main__':
    app.run(debug=True)