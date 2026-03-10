import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "dragon_mega_update_2026"

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
    # Поле для хранения имен доп. фото через запятую
    gallery = db.Column(db.Text, default="") 
    tg_link = db.Column(db.String(100), default="")
    steam_link = db.Column(db.String(100), default="")
    discord_tag = db.Column(db.String(100), default="")

with app.app_context():
    db.create_all()
    initial_squad = {
        "cat": ("Кот", "Архитектор хаоса"),
        "ruslan": ("Руслан", "Мастер тактических решений"),
        "andrey": ("Андрей", "Легенда состава"),
        "timokha": ("Тимоха", "Всегда в деле"),
        "lesha": ("Лёша", "Низкий не удаленький"),
        "ibragim": ("Ибрагим", "Молодой талант")
    }
    for nick, (name, bio) in initial_squad.items():
        if not UserProfile.query.filter_by(username=nick).first():
            new_p = UserProfile(username=nick, display_name=name, bio=bio)
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
    gallery_list = user.gallery.split(',') if user.gallery else []
    return render_template('index.html', user=user, gallery=gallery_list, is_home=False, page_id=page_name)

@app.route('/edit_profile/<page_name>', methods=['POST'])
def edit_profile(page_name):
    if request.form.get('admin_password') != ADMIN_PASSWORD:
        return "Ошибка: Неверный пароль!", 403
    
    user = UserProfile.query.filter_by(username=page_name).first_or_404()
    
    # Обновление текста
    if 'description' in request.form:
        user.bio = request.form.get('description')
        user.tg_link = request.form.get('tg_link')
        user.steam_link = request.form.get('steam_link')
        user.discord_tag = request.form.get('discord_tag')
    
    # Одиночное фото (Аватар)
    photo_file = request.files.get('photo')
    if photo_file and photo_file.filename != '':
        p_filename = secure_filename(f"avatar_{page_name}_{photo_file.filename}")
        photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'], p_filename))
        user.photo = p_filename

    # Видео
    video_file = request.files.get('video')
    if video_file and video_file.filename != '':
        v_filename = secure_filename(f"video_{page_name}_{video_file.filename}")
        video_file.save(os.path.join(app.config['UPLOAD_FOLDER'], v_filename))
        user.video = v_filename

    # Галерея (Много фото)
    gallery_files = request.files.getlist('gallery_photos')
    new_photos = []
    for f in gallery_files:
        if f and f.filename != '':
            g_filename = secure_filename(f"gal_{page_name}_{f.filename}")
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], g_filename))
            new_photos.append(g_filename)
    
    if new_photos:
        current_gal = user.gallery.split(',') if user.gallery else []
        user.gallery = ",".join(current_gal + new_photos)
        
    db.session.commit()
    return redirect(url_for('show_page', page_name=page_name))

if __name__ == '__main__':
    app.run(debug=True)