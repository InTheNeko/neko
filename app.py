from flask import Flask, render_template

app = Flask(__name__)

# Список для главной страницы
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
    return render_template('index.html', buttons=friends_list, title="Выберите бойца", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    # Структура: "ключ": (Имя[0], Описание[1], Фото[2], [Ссылки][3], Статус[4], Игра[5])
    friends_info = {
        "cat": ("Кот", "Самый главный, у него лапки и власть.", "cat.jpg", 
                [("Steam", "https://steamcommunity.com"), ("Валерьянка", "#")], ),
        
        "ruslan": ("Руслан", "Ну так ну сяк почти всегда берёт", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com")], ),
        
        "andrey": ("Андрей", "Постоянно ест, но всё равно тащит.", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com")], ),
        
        "timokha": ("Тимофка", "Жаль, что он с нами (но мы любя).", "timokha.jpg", 
                    [("Steam", "https://steamcommunity.com")], ),
        
        "lesha": ("Лёша", "Гном всегда гном. Мал, да удал.", "lesha.jpg", 
                  [("Steam", "https://steamcommunity.com")], ),
        
        "ibragim": ("Ибрагим", "Почти скоро 12. Растёт не по дням.", "ibragim.jpg", 
                    [("Steam", "https://steamcommunity.com")], )
    }
    
    data = friends_info.get(page_name)
    
    if data:
        # Передаем данные строго по индексам из кортежа выше
        return render_template('index.html', 
                               title=data[0],        
                               description=data[1],  
                               photo=data[2],        
                               links=data[3],
                               status=data[4],
                               game=data[5],
                               is_home=False)
    
    return "Профиль не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
