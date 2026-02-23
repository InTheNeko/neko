from flask import Flask, render_template

app = Flask(__name__)

# Функция-помощник: превращает обычную ссылку в ссылку для плеера
def format_youtube(url):
    if not url: return None
    if "watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    return url

friends_list = [
    ("Кот", "cat"), ("Руслан", "ruslan"), ("Андрей", "andrey"),
    ("Тимофка", "timokha"), ("Лёша", "lesha"), ("Ибрагим", "ibragim")
]

@app.route('/')
def home():
    return render_template('index.html', buttons=friends_list, title="Drakonchik v3", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    friends_info = {
        # Теперь сюда можно вставлять ОБЫЧНЫЕ ссылки!
        "cat": ("Кот", "Самый главный, у него лапки.", "cat.jpg", 
                [("Steam", "https://steamcommunity.com/profiles/76561199122830516/")
                 ("Валерьянка", "#")], 
                "Заметка: Главный администратор. Любит спать.",
                ["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com"]),
        
        "ruslan": ("Руслан", "Ну так ну сяк", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com/profiles/76561199198583765/")],
                   "Заметка: да и так пойдёт", 
                   ["https://www.youtube.com"]), 
        
        "andrey": ("Андрей", "Постоянно ест", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com/profiles/76561198337510525/")
                    ("я гей", "https://youareanidiot.cc")],
                   "Заметка: Если не отвечает, значит ушел на кухню.", []),
        
        "timokha": ("Тимофка", "Жаль что он с нами.", "timokha.jpg", 
                    [("Steam", "https://steamcommunity.com/profiles/76561199054205841/")], 
                    "Заметка: туда сюда.", []),
        
        "lesha": ("Лёша", "Гном всегда гном.", "lesha.jpg", 
                  [("Steam", "https://steamcommunity.com/profiles/76561199096404881/")], 
                  "Заметка: Рост — 0.", []),
        
        "ibragim": ("Ибрагим", "Почти скоро 12.", "ibragim.jpg", 
                    [("Steam", "https://steamcommunity.com/profiles/76561199556449044/")], 
                    "Заметка: Танки.", [])
    }
    
    data = friends_info.get(page_name)
    if data:
        # Автоматически исправляем все ссылки в списке перед отправкой на сайт
        formatted_videos = [format_youtube(v) for v in data[5]]
        
        return render_template('index.html', 
                               title=data[0], description=data[1], photo=data[2], 
                               links=data[3], note=data[4], 
                               video_list=formatted_videos, 
                               is_home=False)
    return "Профиль не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
