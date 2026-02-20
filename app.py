from flask import Flask, render_template
from datetime import datetime # Импортируем время

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%H:%M:%S") # Получаем текущее время
    user_name = "Neko" # Можешь написать свое имя
    # Передаем переменные в HTML через запятую
    return render_template('index.html', time=current_time, name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
