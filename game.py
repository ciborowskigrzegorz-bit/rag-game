import random

class Player:
    def __init__(self, name, hp=100, attack=10):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.inventory = []

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = [healing_potion]

    def attack(self, other):
        damage = random.randint(5, self.attack_power)
        other.hp = max(other.hp - damage, 0)
        return damage


class Enemy:
    def __init__(self):
        self.name = random.choice(["Goblin", "Szkieletor", "Ork"])
        self.hp = random.randint(30, 70)
        self.attack = random.randint(5, 15)

    def attack(self, other):
        damage = random.randint(5, self.attack_power)
        other.hp = max(other.hp - damage, 0)
        return damage


class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect  # funkcja, np. przywraca hp

def heal_effect(player):
    heal_amount = 30
    player.hp = min(100, player.hp + heal_amount)
    return f"{player.name} użył {heal_amount} HP mikstury!"

healing_potion = Item("Mikstura Leczenia", heal_effect)

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
