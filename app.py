from flask import Flask, render_template, request, jsonify
from game import NPC, Dialogue, Player, Enemy, battle, World, Location, Battle

app = Flask(__name__)

player = None
enemy = None
battle_instance = None

#  Inicjalizacja świata
world = World()
world.add_location(Location("Wioska", "Mała spokojna wioska.", events=["spotykasz starszego mieszkańca"]))
world.add_location(Location("Las", "Mroczny las pełen dzikich zwierząt.", events=["atak wilka"]))
world.current_location = world.locations["Wioska"]

#  NPC
npc = NPC("Starszy mieszkaniec", ["Witaj, młody podróżniku!", "Uważaj w lesie!"])
dialogue = Dialogue(npc)


@app.route("/move/<location>")
def move(location):
    return jsonify({"message": world.move_to(location)})


@app.route("/battle", methods=["POST"])
def battle_route():
    global battle_instance
    action = request.json.get("action", "atak")
    if not battle_instance:
        return jsonify({"message": "Walka jeszcze się nie rozpoczęła!"}), 400
    result = battle_instance.fight_turn(action)
    return jsonify({"message": result})


@app.route("/talk/<npc>/<int:choice>")
def talk(npc, choice):
    return jsonify({"message": dialogue.talk(choice)})


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
    global player, enemy, battle_instance
    enemy = Enemy()
    battle_instance = Battle(player, enemy)  # tworzymy instancję walki
    result = battle(player, enemy)           # jednorazowa runda
    return render_template("battle.html", player=player, enemy=enemy, result=result)


@app.route("/use-item", methods=["POST"])
def use_item():
    global player, enemy
    if player.use_item():
        result = f"{player.name} użył mikstury i odzyskał 30 HP!"
    else:
        result = f"{player.name} nie ma już mikstur!"
    
    return render_template("battle.html", player=player, enemy=enemy, result=result)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
