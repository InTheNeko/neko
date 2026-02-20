from flask import Flask, render_template

app = Flask(__name__)

friends = [
    ("Руслан", "ruslan"),
    ("Андрей", "andrey"),
    ("Тимоха", "timokha"),
    ("Лёша", "lesha"),
    ("Ибрагим", "ibragim")
]

@app.route('/')
def home():
    return render_template('index.html', buttons=friends, title="SYSTEM SELECT", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Данные: ключ -> (Имя, Описание, Файл_фото или None)
    data = {
        "ruslan": ("Руслан", "Топ игрок, всегда на связи.", "ruslan.jpg"),
        "andrey": ("Андрей", "Мастер стратегий и тактики.", None), # Без фото
        "timokha": ("Тимоха", "Главный по юмору в команде.", None), # Без фото
        "lesha": ("Лёша", "Спокойный и расчетливый игрок.", None), # Без фото
        "ibragim": ("Ибрагим", "Легендарный скилл и мощь.", "ibragim.jpg")
    }
    
    res = data.get(page_name, ("Ошибка", "Профиль не найден", None))
    
    return render_template('index.html', 
                           title=res[0], 
                           description=res[1], 
                           photo=res[2], 
                           is_home=False)
