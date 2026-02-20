from flask import Flask, render_template

app = Flask(__name__)

# Список игроков: (Название для кнопки, часть ссылки)
players = [
    ("Игрок 1", "player1"),
    ("Игрок 2", "player2"),
    ("Игрок 3", "player3"),
    ("Игрок 4", "player4"),
    ("Игрок 5", "player5")
]

@app.route('/')
def home():
    return render_template('index.html', 
                           buttons=players, 
                           title="Выбор игрока", 
                           is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Словарь имён для заголовка
    names = {
        "player1": "Игрок 1",
        "player2": "Игрок 2",
        "player3": "Игрок 3",
        "player4": "Игрок 4",
        "player5": "Игрок 5"
    }
    
    # Берем имя из словаря, если не нашли — пишем "Ошибка"
    current_player = names.get(page_name, "Неизвестный игрок")
    
    return render_template('index.html', 
                           title=current_player, 
                           is_home=False)

if __name__ == '__main__':
    app.run(debug=True)
