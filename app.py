from flask import Flask, render_template

app = Flask(__name__)

# Умная функция для любых ссылок YouTube
def format_youtube(url):
    if not url: return None
    # Если это короткая ссылка youtu.be/ID
    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
        return f"https://www.youtube.com{video_id}"
    # Если это обычная ссылка watch?v=ID
    if "watch?v=" in url:
        video_id = url.split("watch?v=")[1].split("&")[0]
        return f"https://www.youtube.com{video_id}"
    # Если уже embed или что-то другое
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
        "cat": ("Кот", "Самый главный, у него лапки.", "cat.jpg", 
                [("Steam", "https://steamcommunity.com")], 
                "Заметка: Главный администратор. Любит спать.",
                ["", "https://youtu.be"]),
        
        "ruslan": ("Руслан", "Ну так ну сяк", "ruslan.jpg", 
                   [("Steam", "https://steamcommunity.com")],
                   "Заметка: да и так пойдёт", 
                   ["https://www.youtube.com"]), 
        
        "andrey": ("Андрей", "Постоянно ест", "andrey.jpg", 
                   [("Steam", "https://steamcommunity.com")],
                   "Заметка: Если не отвечает, значит ушел на кухню.", []),
        
        "timokha": ("Тимофка", "Жаль что он с нами.", "timokha.jpg", [], "Заметка: Опасен.", []
                    [("Steam", "https://steamcommunity.com")],
                   "Заметка: Если не отвечает, значит ушел на кухню.", []),
        "lesha": ("Лёша", "Гном всегда гном.", "lesha.jpg", [], "Заметка: Рост — 0.", []
                  [("Steam", "https://steamcommunity.com")],
                   "Заметка: Если не отвечает, значит ушел на кухню.", []),
        "ibragim": ("Ибрагим", "Почти скоро 12.", "ibragim.jpg", [], "Заметка: Танки.", []
                    [("Steam", "https://steamcommunity.com")],
                   "Заметка: Если не отвечает, значит ушел на кухню.", [])
    }
    
    data = friends_info.get(page_name)
    if data:
        # Форматируем все видео в списке
        raw_videos = data[5]
        formatted_videos = [format_youtube(v) for v in raw_videos]
        
        return render_template('index.html', 
                               title=data[0], description=data[1], photo=data[2], 
                               links=data[3], note=data[4], 
                               video_list=formatted_videos, 
                               is_home=False)
    return "Профиль не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
