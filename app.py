from flask import Flask, render_template

app = Flask(__name__)

# Список твоих друзей для главной страницы
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
    # Данные для каждого друга (Заголовок, Описание)
    friends_info = {
        "ruslan": ("Руслан", "Топ игрок, всегда на связи и готов к каткам. Любит Андрейя"),
        "andrey": ("Андрей", "Мастер стратегий и просто хороший черт"),
        "timokha": ("Тимофка", "жаль что он с нами"),
        "lesha": ("Лёша", "гном всегда гном."),
        "ibragim": ("Ибрагим", "почти 12 лет")
    }
    
    # Берем данные из словаря
    data = friends_info.get(page_name, ("Ошибка", "Профиль не найден."))
    
    return render_template('index.html', 
                           title=data[0], 
                           description=data[1], 
                           is_home=False)

if __name__ == '__main__':
    app.run(debug=True)
