from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Настройка БД
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'drakon.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(50), default="Аноним")
    recipient = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

friends_info = {
    "cat": ("Кот", "Просто самый лучший", "cat.jpg", [("Steam", "https://steamcommunity.com")]),
    "ruslan": ("Руслан", "Гей и любит андрея", "ruslan.jpg", [("Steam", "https://steamcommunity.com")]),
    "andrey": ("Андрей", "Опять ест", "andrey.jpg", [("Steam", "https://steamcommunity.com")]),
    "timokha": ("Тимофка", "Жаль что он с нами", "timokha.jpg", [("Steam", "https://steamcommunity.com")]),
    "lesha": ("Лёша", "Низки не удаленький", "lesha.jpg", [("Steam", "https://steamcommunity.com")]),
    "ibragim": ("Ибрагим", "Почти 12 лет", "ibragim.jpg", [("Steam", "https://steamcommunity.com")])
}

@app.route('/')
def home():
    friends_list = [(v[0], k) for k, v in friends_info.items()]
    return render_template('index.html', buttons=friends_list, title="DRAKONCHIK V3", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    data = friends_info.get(page_name)
    if data:
        name, desc, photo, links = data
        notes = Note.query.filter_by(recipient=page_name).order_by(Note.date_posted.desc()).all()
        return render_template('index.html', title=name, description=desc, photo=photo, links=links, is_home=False, notes=notes, page_id=page_name)
    return "404", 404

@app.route('/add_note/<recipient>', methods=['POST'])
def add_note(recipient):
    content = request.form.get('content')
    author = request.form.get('author') or "Аноним"
    if content:
        new_note = Note(content=content, author=author, recipient=recipient)
        db.session.add(new_note)
        db.session.commit()
    return redirect(url_for('show_page', page_name=recipient))

if __name__ == '__main__':
    app.run(debug=True)