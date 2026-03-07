from flask import Flask, render_template

app = Flask(__name__)

# Список для главной страницы (название кнопки, ссылка)
friends_list = [
    ("Кот", "cat"), ("Руслан", "ruslan"), ("Андрей", "andrey"),
    ("Тимофка", "timokha"), ("Лёша", "lesha"), ("Ибрагим", "ibragim")
]

# Общая база данных друзей
friends_info = {
    "cat": ("Кот", "просто самый лучший", "cat.jpg", [("Steam", "https://steamcommunity.com")]),
    "ruslan": ("Руслан", "гей и любит андрея", "ruslan.jpg", [("Steam", "https://steamcommunity.com")]),
    "andrey": ("Андрей", "опять ест", "andrey.jpg", [("Steam", "https://steamcommunity.com")]),
    "timokha": ("Тимофка", "жаль что он с нами", "timokha.jpg", [("Steam", "https://steamcommunity.com")]),
    "lesha": ("Лёша", "низки не удаленький", "lesha.jpg", [("Steam", "https://steamcommunity.com")]),
    "ibragim": ("Ибрагим", "почти 12 лет ", "ibragim.jpg", [("Steam", "https://steamcommunity.com")])
}

@app.route('/')
def home():
    return render_template('index.html', buttons=friends_list, title="DRAGON", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    data = friends_info.get(page_name)
    
    if data:
        # Распаковываем кортеж: имя, описание, фото, ссылки
        name, desc, photo, links = data
        return render_template(
            'index.html', 
            title=name, 
            description=desc, 
            photo=photo, 
            links=links, 
            is_home=False
        )
    
    return "Страница не найдена", 404

if __name__ == '__main__':
    app.run(debug=True)