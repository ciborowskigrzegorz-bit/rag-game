import random

class Character:
    def __init__(self, name, hp=100, attack_power=20):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(5, self.attack_power)
        other.hp = max(other.hp - damage, 0)
        return damage

class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.items = {"potion": 1}  # przykładowy przedmiot

    def use_item(self):
        if self.items["potion"] > 0:
            self.hp = min(self.hp + 30, 100)
            self.items["potion"] -= 1
            return True
        return False

class Enemy(Character):
    def __init__(self):
        names = ["Goblin", "Ork", "Wilkołak"]
        name = random.choice(names)
        hp = random.randint(50, 100)
        attack_power = random.randint(10, 25)
        super().__init__(name, hp, attack_power)

class Location:
    def __init__(self, name, description, events=None):
        self.name = name
        self.description = description
        self.events = events or []

class World:
    def __init__(self):
        self.locations = {}
        self.current_location = None

    def add_location(self, location):
        self.locations[location.name] = location

    def move_to(self, location_name):
        if location_name in self.locations:
            self.current_location = self.locations[location_name]
            return f"Przenosisz się do {location_name}.\n{self.current_location.description}"
        else:
            return "Nie możesz tam iść!"
        
class NPC:
    def __init__(self, name, dialogues):
        self.name = name
        self.dialogues = dialogues

class Dialogue:
    def __init__(self, npc):
        self.npc = npc

    def talk(self, choice_index):
        if 0 <= choice_index < len(self.npc.dialogues):
            return self.npc.dialogues[choice_index]
        else:
            return "Nie ma takiej opcji dialogowej."

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight_turn(self, action):
        # Akcja gracza
        if action == "atak":
            self.enemy.hp -= self.player["attack"]
        elif action == "unik":
            return "Unikłeś ataku wroga!"
        
        # Akcja wroga
        if self.enemy.hp > 0:
            self.player["hp"] -= self.enemy.attack
        
        return f"{self.player['name']} HP: {self.player['hp']}, {self.enemy.name} HP: {self.enemy.hp}"


def battle(player, enemy):
    result_log = ""

    # Gracz atakuje
    dmg_to_enemy = player.attack(enemy)
    result_log += f"{player.name} zadaje {dmg_to_enemy} obrażeń {enemy.name}.<br>"

    # Przeciwnik atakuje, jeśli żyje
    if enemy.hp > 0:
        dmg_to_player = enemy.attack(player)
        result_log += f"{enemy.name} zadaje {dmg_to_player} obrażeń {player.name}.<br>"
    else:
        result_log += f"{enemy.name} został pokonany!<br>"

    if player.hp <= 0:
        result_log += f"{player.name} poległ w walce!<br>"

    return result_log

