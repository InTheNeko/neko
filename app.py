from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Создаем список: (Название, Ссылка)
    # Важно: имя переменной 'my_buttons' должно совпадать с тем, что в HTML!
    my_buttons = [
        ("Главная", "/"),
        ("Обо мне", "/about"),
        ("Проекты", "/projects"),
        ("Галерея", "/gallery"),
        ("Контакты", "/contact")
    ]
    return render_template('index.html', buttons=my_buttons)

# Добавим обработку для всех кнопок, чтобы не было ошибки 404
@app.route('/<name>')
def pages(name):
    return f"<h1>Страница: {name}</h1><a href='/'>Назад на главную</a>"

if __name__ == '__main__':
    app.run(debug=True)
