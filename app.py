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
    # Структура: "ключ": (Имя, Описание, Фото, [Ссылки], Заметка)
    friends_info = {
        "cat": ("Кот", "Самый главный, у него лапки.", "cat.jpg", 
                [("Steam", "https://steamcommunity.com/profiles/76561199122830516/") ("Валерьянка", "#")], 
                "Заметка: Главный администратор этого списка. Любит спать."),
        
        "ruslan": ("Руслан", "Ну так ну сяк почти всегда берёт", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com/profiles/76561199198583765/")],
                   "Заметка: да и так пойдёт"),
        
        "andrey": ("Андрей", "Постояно ест", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com/profiles/76561198337510525/"), ("я гей", "https://youareanidiot.cc")],
                   "Заметка: Если не отвечает, значит ушел на кухню."),
        
        "timokha": ("Тимофка", "Жаль что он с нами.", "timokha.jpg", 
                    [("Steam", "https://steamcommunity.com/profiles/76561199054205841/")],
                    "Заметка: Опасен в кооперативных играх."),
        
        "lesha": ("Лёша", "Гном всегда гном.", "lesha.jpg", 
                  [("Steam", "https://steamcommunity.com/profiles/76561199096404881/")],
                  "Заметка: Маленький рост компенсирует ни чем"),
        
        "ibragim": ("Ибрагим", "Почти скоро 12.", "ibragim.jpg", 
                    [("Steam", "https://steamcommunity.com/profiles/76561199556449044/")],
                    "Заметка: Аааа танки")
    }
    
    data = friends_info.get(page_name)
    
    if data:
        return render_template('index.html', 
                               title=data[0],        
                               description=data[1],  
                               photo=data[2],        
                               links=data[3],        
                               note=data[4], 
                               is_home=False)
    
    return "Профиль не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
