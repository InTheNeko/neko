from flask import Flask, render_template

app = Flask(__name__)

# Список для кнопок на главной (Имя, URL-путь)
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
    return render_template('index.html', buttons=friends_list, title="Выберите профиль", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Данные: "ключ": (0:Имя, 1:Описание, 2:Фото, 3:[Ссылки], 4:Статус, 5:Игра)
    friends_info = {
        "cat": ("Кот", "Самый главный, у него лапки и власть.", "cat.jpg", 
                [("Steam", "https://steamcommunity.com"), ("Валерьянка", "#")], "В сети", "Stray"),
        
        "ruslan": ("Руслан", "Ну так ну сяк почти всегда берёт", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com")], "Спит", "Dota 2"),
        
        "andrey": ("Андрей", "Постоянно ест, но всё равно тащит.", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com"), ("Секрет", "https://youareanidiot.cc")], "В игре", "CS 2"),
        
        "timokha": ("Тимофка", "Жаль, что он с нами (но мы любя).", "timokha.jpg", 
                    [("Steam", "https://steamcommunity.com")], "Offline", "Roblox"),
        
        "lesha": ("Лёша", "Гном всегда гном. Мал, да удал.", "lesha.jpg", 
                  [("Steam", "https://steamcommunity.com")], "В сети", "Lethal Company"),
        
        "ibragim": ("Ибрагим", "Почти скоро 12. Растёт не по дням.", "ibragim.jpg", 
                    [("Steam", "https://steamcommunity.com")], "Учит уроки", "Minecraft")
    }
    
    data = friends_info.get(page_name)
    
    if data:
        return render_template('index.html', 
                               title=data[0],        
                               description=data[1],  
                               photo=data[2],        
                               links=data[3],
                               status=data[4],
                               game=data[5],
                               is_home=False)
    
    return "Профиль не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
