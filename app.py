from flask import Flask, render_template

app = Flask(__name__)

# Обновленный список кнопок
menu_items = [
    ("Игрок 1", "/player1"),
    ("Игрок 2", "/player2"),
    ("Игрок 3", "/player3"),
    ("Игрок 4", "/player4"),
    ("Игрок 5", "/player5")
]

@app.route('/')
def home():
    return render_template('index.html', 
                           buttons=menu_items, 
                           title="Выбор игрока", 
                           text="Выберите игрока из списка ниже, чтобы просмотреть его профиль.")

@app.route('/<page_name>')
def show_page(page_name):
    # Данные для каждого игрока
    players_info = {
        "player1": ("Игрок 1", "Характеристики: Сила 10, Ловкость 5."),
        "player2": ("Игрок 2", "Характеристики: Магия 12, Интеллект 8."),
        "player3": ("Игрок 3", "Характеристики: Защита 15, Здоровье 100."),
        "player4": ("Игрок 4", "Характеристики: Скорость 20, Скрытность 10."),
        "player5": ("Игрок 5", "Характеристики: Удача 7, Меткость 9.")
    }
    
    # Ищем инфо по ключу (например, 'player1')
    info = players_info.get(page_name, ("Упс!", "Игрок не найден."))
    
    return render_template('index.html', 
                           buttons=menu_items, 
                           title=info[0], 
                           text=info[1])

if __name__ == '__main__':
    app.run(debug=True)
