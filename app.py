from flask import Flask, render_template

app = Flask(__name__)

# Главное меню (названия кнопок и ссылки)
players_list = [
    ("Игрок 1", "player1"),
    ("Игрок 2", "player2"),
    ("Игрок 3", "player3"),
    ("Игрок 4", "player4"),
    ("Игрок 5", "player5")
]

@app.route('/')
def home():
    # Передаем список кнопок и флаг, что мы на главной
    return render_template('index.html', buttons=players_list, title="Выбор игрока", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Словарь: ключ ссылки -> (Заголовок, Имя файла картинки)
    players_info = {
        "player1": ("Игрок 1", "p1.jpg"),
        "player2": ("Игрок 2", "p2.jpg"),
        "player3": ("Игрок 3", "p3.jpg"),
        "player4": ("Игрок 4", "p4.jpg"),
        "player5": ("Игрок 5", "p5.jpg")
    }
    
    # Получаем данные игрока. Если не нашли — ставим заглушку.
    player_data = players_info.get(page_name, ("Ошибка", "default.jpg"))
    
    return render_template('index.html', 
                           title=player_data[0], 
                           photo=player_data[1], 
                           is_home=False)

if __name__ == '__main__':
    app.run(debug=True)
