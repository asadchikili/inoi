
import random

class Player:
    def __init__(self, name, strength, health, intellect, item):
        self.name = name
        self.base_strength = strength
        self.base_health = health
        self.base_intellect = intellect
        self.item = item
        self.strength = self.base_strength
        self.health = self.base_health
        self.intellect = self.base_intellect
        self.estus_flasks = 3  # Начальное количество эстусов

    def attack(self):
        if self.item == "Меч":
            return random.randint(1, 10) + self.strength
        elif self.item == "Магический всплеск":
            return random.randint(1, 10) + self.intellect
        elif self.item == "Жар солнца":
            return random.randint(1, 10) + self.strength + self.intellect

    def use_estus(self):
        if self.estus_flasks > 0:
            self.estus_flasks -= 1
            self.health += 5  # Предположим, что каждый эстус восстанавливает 5 единиц здоровья
            print("Вы использовали Эстус и восстановили здоровье.")
        else:
            print("У вас закончились эстусы. Вы не можете восстановить здоровье.")

def print_status(player, boss):
    print(f"{player.name}: Сила - {player.strength}, Жизни - {player.health}, Интеллект - {player.intellect}, Эстусы - {player.estus_flasks}")
    print(f"{boss['name']}: Жизни - {boss['health']}")

def level_up(player):
    player.strength += 1
    player.health += 2
    player.intellect += 1
    print("Вы получили новый уровень! Ваши характеристики улучшились.")

def fight_boss(player, boss):
    print(f"Вы встретили босса {boss['name']}. Начинается бой!")

    while player.health > 0 and boss['health'] > 0:
        print_status(player, boss)

        # Предоставим игроку возможность использовать Эстус после каждого хода
        use_estus = input("Хотите использовать Эстус? (да/нет): ")
        if use_estus.lower() == "да":
            player.use_estus()

        attack_result = player.attack()

        print(f"Вы атакуете с использованием {player.item} и наносите {attack_result} урона!")

        if attack_result >= boss['defeat_threshold']:
            print(f"{boss['name']} погиб! Вы выиграли!")
            break
        else:
            boss_attack = random.randint(1, 10)
            player.health -= boss_attack
            print(f"{boss['name']} атакует вас и наносит {boss_attack} урона!")

    if player.health <= 0:
        print("Вы проиграли. Ваши жизни закончились.")
        return False
    else:
        print_status(player, boss)
        return True

def main():
    bosses = [
        {"name": "Горгулья", "health": 20, "defeat_threshold": 5},
        {"name": "Ведьма Хаоса Квилег", "health": 25, "defeat_threshold": 6},
        {"name": "Неутомимый воин", "health": 30, "defeat_threshold": 7},
        {"name": "Сиф Великий Волк", "health": 35, "defeat_threshold": 8},
        {"name": "Орнштейн Драконоборец", "health": 40, "defeat_threshold": 9},
        {"name": "Палач Смоуг", "health": 45, "defeat_threshold": 10}
    ]

    print("Выберите свой класс:")
    print("1. Мечник")
    print("2. Маг")
    print("3. Пиромант")

    choice = input("Введите номер класса: ")

    if choice == "1":
        player = Player("Мечник", 10, 8, 3, "Меч")
    elif choice == "2":
        player = Player("Маг", 2, 4, 12, "Магический всплеск")
    elif choice == "3":
        player = Player("Пиромант", 4, 6, 8, "Жар солнца")
    else:
        print("Неверный выбор. Завершение игры.")
        return

    print(f"Вы выбрали {player.name}!")
    print(f"Характеристики: Сила - {player.strength}, Жизни - {player.health}, Интеллект - {player.intellect}")
    print(f"Ваш предмет: {player.item}")

    for boss in bosses:
        if not fight_boss(player, boss):
            break

        level_up_choice = input("Хотите повысить свой уровень? (да/нет): ")
        if level_up_choice.lower() == "да":
            level_up(player)

    print("Поздравляю! Вы победили всех боссов и завершили игру.")

if __name__ == "__main__":
    main()
