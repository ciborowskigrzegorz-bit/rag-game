from flask import Flask, render_template, request
from game import Player, Enemy, battle

app = Flask(__name__)

player = None

@app.route("/", methods=["GET", "POST"])
def index():
    global player
    if request.method == "POST":
        name = request.form["name"]
        player = Player(name)
        return render_template("battle.html", player=player, enemy=None, result=None)
    return render_template("index.html")

@app.route("/fight", methods=["POST"])
def fight():
    global player
    enemy = Enemy()
    result = battle(player, enemy)
    return render_template("battle.html", player=player, enemy=enemy, result=result)

if __name__ == "__main__":
    app.run(debug=True)
