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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

@app.route("/use-item", methods=["POST"])
def use_item():
    global player
    if player.use_item():
        result = f"{player.name} użył mikstury i odzyskał 30 HP!"
    else:
        result = f"{player.name} nie ma już mikstur!"
    
    enemy = Enemy()  # możesz też zachować poprzedniego w sesji
    return render_template("battle.html", player=player, enemy=enemy, result=result)
