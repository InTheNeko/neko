from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Создаем список кнопок: (Текст на кнопке, Ссылка)
    menu_items = [
        ("Главная", "/"),
        ("Обо мне", "/about"),
        ("Проекты", "/projects"),
        ("Галерея", "/gallery"),
        ("Контакты", "/contact")
    ]
    return render_template('index.html', menu=menu_items)

# Создадим один универсальный маршрут для всех остальных страниц
@app.route('/<page_name>')
def page(page_name):
    return f"<h1>Вы перешли на страницу: {page_name}</h1><br><a href='/'>Назад на главную</a>"

if __name__ == '__main__':
    app.run(debug=True)
