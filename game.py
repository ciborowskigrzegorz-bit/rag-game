import random

class Player:
    def __init__(self, name, hp=100, attack=10):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.inventory = []

class Enemy:
    def __init__(self):
        self.name = random.choice(["Goblin", "Szkieletor", "Ork"])
        self.hp = random.randint(30, 70)
        self.attack = random.randint(5, 15)

def battle(player, enemy):
    log = []
    while player.hp > 0 and enemy.hp > 0:
        enemy.hp -= player.attack
        log.append(f"{player.name} atakuje {enemy.name} i zadaje {player.attack} obrazeń.")
        if enemy.hp <= 0:
            log.append(f"{enemy.name} zostaje zabity!")
            break

        player.hp -= enemy.attack
        log.append(f"{enemy.name} atakuje {player.name} i zadaje {enemy.attack} obrazen.")
        if player.hp <= 0:
            log.append(f"{player.name} zostaje zabity!")
    return log
