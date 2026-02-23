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
    friends_info = {
        "cat": ("Кот", "Главный архитектор хаоса. Обладает безграничной властью и самыми острыми когтями.", "cat.jpg", 
                [("Steam", "https://steamcommunity.com")]),
        
        "ruslan": ("Руслан", "Мастер тактических решений. Почти всегда в деле, когда нужно затащить.", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com")]),
        
        "andrey": ("Андрей", "Легенда состава. Его спокойствие в бою пугает врагов больше, чем оружие.", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com")]),
        
        "timokha": ("Тимофка", "Стихийное бедствие. Никто не знает, чего от него ждать в следующую минуту.", "timokha.jpg", 
                    [("Steam", "https://steamcommunity.com")]),
        
        "lesha": ("Лёша", "Надежный как швейцарские часы. Всегда там, где нужна поддержка.", "lesha.jpg", 
                  [("Steam", "https://steamcommunity.com")]),
        
        "ibragim": ("Ибрагим", "Молодой талант с огромным потенциалом. Будущее этой команды.", "ibragim.jpg", 
                    [("Steam", "https://steamcommunity.com")])
    }
    
    data = friends_info.get(page_name)
    if data:
        return render_template('index.html', title=data, description=data, photo=data, links=data, is_home=False)
    return "Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)
