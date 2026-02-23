from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('index.html', buttons=friends_list, title="Выберите бойца", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Новая структура: (Имя, Описание, Фото, Ссылки, Статус, Любимая игра)
    friends_info = {
       "cat": ("Кот", "Самый главный, у него лапки и власть.", "cat.jpg", 
                [("Steam", "https://steamcommunity.com/profiles/76561199122830516/"), ("Валерьянка", "#")]),
        
        "ruslan": ("Руслан", "Ну так ну сяк почти всегда берёт", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com/profiles/76561199198583765/")]),
        
        "andrey": ("Андрей", "постояно ест", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com/profiles/76561198337510525/"), ("я гей", "https://youareanidiot.cc")]),
        
        "timokha": ("Тимофка", "жаль что он с нами.", "timokha.jpg", 
                    [("Steam", "https://steamcommunity.com/profiles/76561199054205841/"), ]),
        
        "lesha": ("Лёша", "гном всегда гном.", "lesha.jpg", 
                  [("Steam", "https://steamcommunity.com/profiles/76561199096404881/"), ]),
        
        "ibragim": ("Ибрагим", "почти скоро 12.", "ibragim.jpg", 
                    [("Steam", "https://steamcommunity.com/profiles/76561199556449044/"), ])
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
