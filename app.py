from flask import Flask, render_template

app = Flask(__name__)

# Список для главной: (Имя, ссылка)
friends = [
    ("Руслан", "ruslan"),
    ("Андрей", "andrey"),
    ("Тимоха", "timokha"),
    ("Лёша", "lesha"),
    ("Ибрагим", "ibragim")
]

@app.route('/')
def home():
    return render_template('index.html', buttons=friends, title="Выбор профиля", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Словарь: ключ -> (Имя, Описание, Файл_картинки)
    data = {
        "ruslan": ("Руслан", "Топ игрок, всегда на связи.", "ruslan.jpg"),
        "andrey": ("Андрей", "Мастер стратегий.", "andrey.jpg"),
        "timokha": ("Тимоха", "Главный по юмору.", "timokha.jpg"),
        "lesha": ("Лёша", "Никогда не подводит.", "lesha.jpg"),
        "ibragim": ("Ибрагим", "Легендарный скилл.", "ibragim.jpg")
    }
    
    res = data.get(page_name, ("Ошибка", "Не найдено", "default.jpg"))
    
    return render_template('index.html', 
                           title=res[0], 
                           description=res[1], 
                           photo=res[2], 
                           is_home=False)
