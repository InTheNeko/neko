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
    return render_template('index.html', buttons=friends_list, title="Drakonchik v3", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Структура: "ключ": (Имя, Описание, Фото, [Ссылки], Заметка, Видео_URL)
    friends_info = {
        "cat": ("Кот", "Самый главный, у него лапки.", "cat.jpg", 
                [("Steam", "https://steamcommunity.com")], 
                "Заметка: Главный администратор этого списка. Любит спать.",
                "https://www.youtube.com"),
        
        "ruslan": ("Руслан", "Ну так ну сяк почти всегда берёт", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com")],
                   "Заметка: да и так пойдёт", 
                   "https://www.youtube.com"), # Добавь ссылку сюда
        
        "andrey": ("Андрей", "Постояно ест", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com"), ("я гей", "https://youareanidiot.cc")],
                   "Заметка: Если не отвечает, значит ушел на кухню.",
                   "https://www.youtube.com"), # Добавь ссылку сюда
        
        "timokha": ("Тимофка", "Жаль что он с нами.", "timokha.jpg", 
                    [("Steam", "https://steamcommunity.com")],
                    "Заметка: Опасен в кооперативных играх.",
                    "https://www.youtube.com"), # Добавь ссылку сюда
        
        "lesha": ("Лёша", "Гном всегда гном.", "lesha.jpg", 
                  [("Steam", "https://steamcommunity.com")],
                  "Заметка: Маленький рост компенсирует ни чем",
                  "https://www.youtube.com"), # Добавь ссылку сюда
        
        "ibragim": ("Ибрагим", "Почти скоро 12.", "ibragim.jpg", 
                    [("Steam", "https://steamcommunity.com")],
                    "Заметка: Аааа танки",
                    "https://www.youtube.com") # Добавь ссылку сюда
    }
    
    data = friends_info.get(page_name)
    
    if data:
        return render_template('index.html', 
                               title=data[0],        
                               description=data[1],  
                               photo=data[2],        
                               links=data[3],        
                               note=data[4],
                               video_url=data[5], # Передаем 6-й элемент (ссылку на видео)
                               is_home=False)
    
    return "Профиль не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
