from flask import Flask, render_template

app = Flask(__name__)

# Список для главной страницы (Кот первый)
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
        "cat": ("Кот", "Самый главный, у него лапки.", "cat.jpg", 
                [("YouTube", "https://youtube.com")], 
                "Заметка: Главный администратор этого списка. Любит спать."),
        
        "ruslan": ("Руслан", "Ну так ну сяк почти всегда берёт", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com")],
                   "Заметка: да и так пойдёт"),
        
        "andrey": ("Андрей", "постояно ест", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com"), ("я гей", "https://youareanidiot.cc")],
                   "Заметка: Если не отвечает, значит ушел на кухню."),
        
        "timokha": ("Тимофка", "жаль что он с нами.", "timokha.jpg", 
                    [("Steam", "https://steamcommunity.com"), ("YouTube", "https://youtube.com")],
                    "Заметка: Опасен в кооперативных играх."),
        
        "lesha": ("Лёша", "гном всегда гном.", "lesha.jpg", 
                  [("Steam", "https://steamcommunity.com"), ("YouTube", "https://youtube.com")],
                  "Заметка: Маленький рост компенсирует ни чем "),
        
        "ibragim": ("Ибрагим", "почти скоро 12.", "ibragim.jpg", 
                    [("Steam", "https://steamcommunity.com"), ("Discord", "https://discord.com")],
                    "Заметка: аааа танки")
    }
    
    data = friends_info.get(page_name)
    
    if data:
        return render_template('index.html', 
                               title=data[0],        
                               description=data[1],  
                               photo=data[2],        
                               links=data[3],        
                               note=data[4], # Заметка
                               is_home=False)
    
    return "Профиль не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
