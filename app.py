from flask import Flask, render_template

app = Flask(__name__)

friends_list = [
    ("Кот", "cat"), ("Руслан", "ruslan"), ("Андрей", "andrey"),
    ("Тимофка", "timokha"), ("Лёша", "lesha"), ("Ибрагим", "ibragim")
]

@app.route('/')
def home():
    return render_template('index.html', buttons=friends_list, title="DRAGON", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Структура: "ключ": (Имя, Описание, Фото, [Ссылки], [Мета-теги для декора])
    friends_info = {
        "cat": ("Кот", "Главный архитектор хаоса. Обладает безграничной властью.", "cat.jpg", 
                [("Steam", "https://steamcommunity.com")], 
                ["ВЛАСТЬ", "ЛАПКИ", "9 ЖИЗНЕЙ"]),
        
        "ruslan": ("Руслан", "Мастер тактических решений. Почти всегда в деле.", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com")], 
                   ["ТАКТИКА", "STAMINA", "RELIABLE"]),
        
        "andrey": ("Андрей", "Легенда состава. Его спокойствие пугает врагов.", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com")], 
                   ["FOOD_BUFF", "CHILL", "LEGEND"]),
        
        "timokha": ("Тимофка", "Стихийное бедствие. Никто не знает, чего от него ждать.", "timokha.jpg", 
                    [("Steam", "https://steamcommunity.com")], 
                    ["CHAOS", "RANDOM", "LUCK: 100"]),
        
        "lesha": ("Лёша", "Надежный как швейцарские часы. Всегда поддержит.", "lesha.jpg", 
                  [("Steam", "https://steamcommunity.com")], 
                  ["STABILITY", "DWARVEN_ARMOR", "SUPPORT"]),
        
        "ibragim": ("Ибрагим", "Молодой талант с огромным потенциалом. Гроза серверов.", "ibragim.jpg", 
                    [("Steam", "https://steamcommunity.com")], 
                    ["FUTURE", "TALENT", "SPEED"])
    }
    
    data = friends_info.get(page_name)
    if data:
        return render_template('index.html', title=data[0], description=data[1], photo=data[2], 
                               links=data[3], tags=data[4], is_home=False)
    return "Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)
