class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        return other.health

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        current_turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if current_turn % 2 == 0:
                self.player.attack(self.computer)
                print(f"{self.player.name} атаковал! У {self.computer.name} осталось {self.computer.health} здоровья")
            else:
                self.computer.attack(self.player)
                print(f"{self.computer.name} атаковал! У {self.player.name} осталось {self.player.health} здоровья")
            current_turn += 1

        winner = self.player.name if self.player.is_alive() else self.computer.name
        print(f"\nПобедитель: {winner}!")
