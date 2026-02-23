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
    return render_template('index.html', buttons=friends_list, title="DRAGON", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Структура: "ключ": (Имя, Описание, Фото, [Ссылки], Уровень %)
    friends_info = {
        "cat": ("Кот", "Главный архитектор хаоса. Обладает безграничной властью и острыми когтями.", "cat.jpg", 
                [("Steam", "#"), ("Валерьянка", "#")], 99),
        
        "ruslan": ("Руслан", "Мастер тактических решений. Почти всегда в деле, когда нужно затащить.", "ruslan.jpg", 
                   [("Steam", "#")], 70),
        
        "andrey": ("Андрей", "Легенда состава. Его спокойствие в бою пугает врагов больше, чем оружие.", "andrey.jpg", 
                   [("Steam", "#")], 85),
        
        "timokha": ("Тимофка", "Стихийное бедствие. Никто не знает, чего от него ждать в следующую минуту.", "timokha.jpg", 
                    [("Steam", "#")], 45),
        
        "lesha": ("Лёша", "Надежный как швейцарские часы. Всегда там, где нужна поддержка.", "lesha.jpg", 
                  [("Steam", "#")], 75),
        
        "ibragim": ("Ибрагим", "Молодой талант с огромным потенциалом. Будущее этой команды.", "ibragim.jpg", 
                    [("Steam", "#")], 60)
    }
    
    data = friends_info.get(page_name)
    
    if data:
        return render_template('index.html', 
                               title=data[0],        
                               description=data[1],  
                               photo=data[2],        
                               links=data[3],
                               power=data[4],    
                               is_home=False)
    
    return "Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)
