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

