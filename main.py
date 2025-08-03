import os

def load_map(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def print_map(game_map):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in game_map:
        print(''.join(row))

def find_player(game_map):
    for y, row in enumerate(game_map):
        for x, char in enumerate(row):
            if char == '@':
                return x, y
    return None

def move_player(game_map, dx, dy):
    x, y = find_player(game_map)
    new_x, new_y = x + dx, y + dy
    target = game_map[new_y][new_x]

    if target == '#':
        return "Nie możesz iść przez ścianę."
    elif target == '$':
        game_map[y][x] = ' '
        game_map[new_y][new_x] = '@'
        return "Znalazłeś skarb! 💰"
    elif target == 'E':
        game_map[y][x] = ' '
        game_map[new_y][new_x] = '@'
        return "Spotkałeś wroga! ⚔️ Walka!"
    elif target == ' ':
        game_map[y][x] = ' '
        game_map[new_y][new_x] = '@'
        return "Idziesz dalej..."

    return "Nieznany obiekt."

def main():
    game_map = load_map('map.txt')

    while True:
        print_map(game_map)
        print("\nSterowanie: w (góra), s (dół), a (lewo), d (prawo), q (wyjście)")
        move = input("Twój ruch: ").lower()

        if move == 'q':
            print("Do zobaczenia!")
            break
        elif move in ['w', 's', 'a', 'd']:
            dx = dy = 0
            if move == 'w': dy = -1
            elif move == 's': dy = 1
            elif move == 'a': dx = -1
            elif move == 'd': dx = 1

            msg = move_player(game_map, dx, dy)
            print(msg)
            input("\n[Enter] kontynuuj...")
        else:
            print("Nieprawidłowy ruch!")
            input("\n[Enter] kontynuuj...")

if __name__ == '__main__':
    main()
