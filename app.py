from flask import Flask, render_template

app = Flask(__name__)

# Список для главной страницы
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
    # Структура: "ключ": (Имя, Описание, Фото, [Список ссылок])
    friends_info = {
        "ruslan": ("Руслан", "Ну так ну сяк почти всегда берёт", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com/profiles/76561199198583765/"),]),
        
        "andrey": ("Андрей", "постояно ест", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com/profiles/76561198337510525/"),("я гей", "https://youareanidiot.cc/")]),
        
        "timokha": ("Тимофка", "жаль что он с нами.", "timokha.jpg", 
                    [("Steam", "https://steamcommunity.com/profiles/76561199054205841/"),("YouTube", "https://youtube.com")]),
        
        "lesha": ("Лёша", "гном всегда гном.", "lesha.jpg", [
            (("Steam", "https://steamcommunity.com/profiles/76561199096404881/"),"YouTube", "https://youtube.com")
        ]
                  ),
        
        
        "ibragim": ("Ибрагим", "почти скоро 12.", "ibragim.jpg", 
                    [("Steam", "https://steamcommunity.com/profiles/76561199556449044/"),("Discord", "https://discord.com")])
    }
    
    data = friends_info.get(page_name)
    
    if data:
        return render_template('index.html', 
                               title=data[0],        # Имя (индекс 0)
                               description=data[1],  # Описание (индекс 1)
                               photo=data[2],        # Фото (индекс 2)
                               links=data[3],        # Список ссылок (индекс 3)
                               is_home=False)
    
    return "Профиль не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
