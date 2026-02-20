from flask import Flask, render_template

app = Flask(__name__)

players_list = [
    ("Player 01", "player1"),
    ("Player 02", "player2"),
    ("Player 03", "player3"),
    ("Player 04", "player4"),
    ("Player 05", "player5")
]

@app.route('/')
def home():
    return render_template('index.html', buttons=players_list, title="System Select", is_home=True)

@app.route('/<page_name>')
def show_page(page_name):
    players_info = {
        "player1": ("Player 01", "p1.jpg"),
        "player2": ("Player 02", "p2.jpg"),
        "player3": ("Player 03", "p3.jpg"),
        "player4": ("Player 04", "p4.jpg"),
        "player5": ("Player 05", "p5.jpg")
    }
    player_data = players_info.get(page_name, ("Error", "default.jpg"))
    return render_template('index.html', title=player_data[0], photo=player_data[1], is_home=False)

if __name__ == '__main__':
    app.run(debug=True)
