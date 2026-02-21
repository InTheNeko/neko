from flask import Flask, render_template

app = Flask(__name__)

friends_list = [
    ("Руслан", "ruslan"),
    ("Андрей", "andrey"),
    ("Тимофка", "timokha"),
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
        "ruslan": ("Руслан", "Ну так ну сяк почти всегда берёт", "ruslan.jpg"),
        "andrey": ("Андрей", "постояно ест", "andrey.jpg"), # Без фото
        "timokha": ("Тимофка", "жаль что он с нами.", "timokha.jpg"),
        "lesha": ("Лёша", "гном всегда гном.", "lesha.jpg"),
        "ibragim": ("Ибрагим", "почти скоро 12.", "ibragim.jpg")
    }
    
    data = friends_info.get(page_name, ("Ошибка", "Профиль не найден.", None))
    
    return render_template('index.html', 
                           title=data[0], 
                           description=data[1], 
                           photo=data[2], # Передаем фото
                           is_home=False)

if __name__ == '__main__':
    app.run(debug=True)
