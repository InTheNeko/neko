from flask import Flask, render_template

app = Flask(__name__)

# Список для главной страницы
friends_list = [
    ("Кот", "cat"),
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
    # Структура: "ключ": (Имя, Описание, Фото, [Ссылки], Заметка)
    friends_info = {
        "cat": ("Кот", "Самый главный.", "cat.jpg", 
                [("YouTube", "https://youtube.com")], 
                "Заметка: Купить корм, поспать 20 часов, захватить мир."),
        
        "ruslan": ("Руслан", "Ну так ну сяк...", "ruslan.jpg", 
                   [("Steam", "#")], 
                   "Заметка: Почти всегда в сети, но редко отвечает."),
        
        "andrey": ("Андрей", "Постоянно ест", "andrey.jpg", 
                   [("Steam", "#")], 
                   "Заметка: Если не отвечает, значит ушел за добавкой."),
        
        "timokha": ("Тимофка", "Жаль что он с нами.", "timokha.jpg", 
                    [("Steam", "#")], 
                    "Заметка: С ним опасно играть в кооперативе."),
        
        "lesha": ("Лёша", "Гном всегда гном.", "lesha.jpg", 
                  [("Steam", "#")], 
                  "Заметка: Маленький рост — большая ярость."),
        
        "ibragim": ("Ибрагим", "Почти скоро 12.", "ibragim.jpg", 
                    [("Steam", "#")], 
                    "Заметка: Самый молодой в команде.")
    }
    
    data = friends_info.get(page_name)
    
    if data:
        return render_template('index.html', 
                               title=data[0],
                               description=data[1],
                               photo=data[2],
                               links=data[3],
                               note=data[4], # Передаем заметку
                               is_home=False)
    
    return "Профиль не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
