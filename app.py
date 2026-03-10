import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "dragon_russian_edition_2026"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'drakon.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static', 'uploads')

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

db = SQLAlchemy(app)
ADMIN_PASSWORD = "1234" 

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    display_name = db.Column(db.String(100))
    bio = db.Column(db.String(500))
    photo = db.Column(db.String(100), default="default.jpg")
    video = db.Column(db.String(100), default="")
    gallery = db.Column(db.Text, default="") 
    tg_link = db.Column(db.String(100), default="")
    steam_link = db.Column(db.String(100), default="")
    discord_tag = db.Column(db.String(100), default="")

with app.app_context():
    db.create_all()
    # Обновленный список имен
    squad = {
        "cat":"Кот", 
        "ruslan":"Руслан", 
        "andrey":"Андрей", 
        "timokha":"Тимофка", # Изменено здесь
        "lesha":"Лёша", 
        "ibragim":"Ибрагим"
    }
    for nick, name in squad.items():
        if not UserProfile.query.filter_by(username=nick).first():
            db.session.add(UserProfile(username=nick, display_name=name, bio="Описание пока пустое..."))
    db.session.commit()

@app.route('/')
def home():
    profiles = UserProfile.query.all()
    return render_template('index.html', profiles=profiles, is_home=True, title="DRAKONCHIK")

@app.route('/user/<page_name>')
def show_page(page_name):
    user = UserProfile.query.filter_by(username=page_name).first_or_404()
    gallery_list = [img for img in user.gallery.split(',') if img] if user.gallery else []
    return render_template('index.html', user=user, gallery=gallery_list, is_home=False, page_id=page_name)

@app.route('/edit_profile/<page_name>', methods=['POST'])
def edit_profile(page_name):
    if request.form.get('admin_password') != ADMIN_PASSWORD:
        return "Неверный пароль", 403
    user = UserProfile.query.filter_by(username=page_name).first_or_404()
    
    if request.form.get('clear_video'): user.video = ""
    if request.form.get('clear_gallery'): user.gallery = ""
    
    user.bio = request.form.get('bio', user.bio)
    user.tg_link = request.form.get('tg', user.tg_link)
    user.steam_link = request.form.get('steam', user.steam_link)
    user.discord_tag = request.form.get('discord', user.discord_tag)

    f_photo = request.files.get('photo')
    if f_photo and f_photo.filename:
        name = secure_filename(f"at_{page_name}_{f_photo.filename}")
        f_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
        user.photo = name

    f_video = request.files.get('video')
    if f_video and f_video.filename:
        name = secure_filename(f"vi_{page_name}_{f_video.filename}")
        f_video.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
        user.video = name

    f_gallery = request.files.getlist('gallery')
    new_imgs = []
    for f in f_gallery:
        if f.filename:
            name = secure_filename(f"ga_{page_name}_{f.filename}")
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
            new_imgs.append(name)
    if new_imgs:
        old = user.gallery.split(',') if user.gallery else []
        user.gallery = ",".join(old + new_imgs)

    db.session.commit()
    return redirect(url_for('show_page', page_name=page_name))

if __name__ == '__main__':
    app.run(debug=True)