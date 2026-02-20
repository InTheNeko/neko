from flask import Flask, render_template

app = Flask(__name__)

friends_list = [
    ("Руслан", "ruslan"),
    ("Андрей", "andrey"),
    ("Тимоха", "timokha"),
    ("Лёша", "lesha"),
    ("Ибрагим", "ibragim")
]

@app.route('/')
def home():
    return render_template('index.html', buttons=friends_list, title="Выбор профиля", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Словарь: "ключ": ("Имя", "Описание", "файл_картинки")
    friends_info = {
        "ruslan": ("Руслан", "Топ игрок, всегда на связи.", "ruslan.jpg"),
        "andrey": ("Андрей", "Мастер стратегий.", None), # Без фото
        "timokha": ("Тимоха", "Главный по юмору.", None),
        "lesha": ("Лёша", "Никогда не подводит.", None),
        "ibragim": ("Ибрагим", "Легендарный скилл и мощь.", "ibragim.jpg")
    }
    
    data = friends_info.get(page_name, ("Ошибка", "Профиль не найден.", None))
    
    return render_template('index.html', 
                           title=data[0], 
                           description=data[1], 
                           photo=data[2], # Передаем фото
                           is_home=False)

if __name__ == '__main__':
    app.run(debug=True)
