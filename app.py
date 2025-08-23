from flask import Flask, render_template, request
from game import NPC, Player, Enemy, battle, World, Location

app = Flask(__name__)

player = None

world = World()
world.add_location(Location("Wioska", "Mała spokojna wioska.", events=["spotykasz starszego mieszkańca"]))
world.add_location(Location("Las", "Mroczny las pełen dzikich zwierząt.", events=["atak wilka"]))
world.current_location = world.locations["Wioska"]
npc = NPC("Starszy mieszkaniec", ["Witaj, młody podróżniku!", "Uważaj w lesie!"])
dialogue = Dialogue(npc)
print(dialogue.talk(0))  # Witaj, młody podróżniku!


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

@app.route("/use-item", methods=["POST"])
def use_item():
    global player
    if player.use_item():
        result = f"{player.name} użył mikstury i odzyskał 30 HP!"
    else:
        result = f"{player.name} nie ma już mikstur!"
    
    enemy = Enemy()  # możesz też zachować poprzedniego w sesji
    return render_template("battle.html", player=player, enemy=enemy, result=result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


