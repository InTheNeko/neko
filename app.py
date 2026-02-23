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
        "cat": ("Кот", "Главный архитектор хаоса. У него лапки, но власть абсолютна.", "cat.jpg", [("Steam", "#")]),
        "ruslan": ("Руслан", "Мастер тактики. Почти всегда берет инициативу на себя.", "ruslan.jpg", [("Steam", "#")]),
        "andrey": ("Андрей", "Легенда состава. Спокоен и крайне опасен.", "andrey.jpg", [("Steam", "#")]),
        "timokha": ("Тимофка", "Стихийное бедствие. Никто не знает его следующий шаг.", "timokha.jpg", [("Steam", "#")]),
        "lesha": ("Лёша", "Надежный как скала. Всегда там, где нужна поддержка.", "lesha.jpg", [("Steam", "#")]),
        "ibragim": ("Ибрагим", "Молодой талант. Будущее этой команды.", "ibragim.jpg", [("Steam", "#")])
    }
    
    data = friends_info.get(page_name)
    if data:
        return render_template('index.html', title=data[0], description=data[1], photo=data[2], links=data[3], is_home=False)
    return "Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)
