# Определение класса Hero (Герой) - основной класс для создания персонажей игры
class Hero:
    # Конструктор класса (метод __init__), вызывается при создании нового героя
    def __init__(self, name):
        # Инициализация атрибутов героя:
        self.name = name  # Имя героя (передается при создании)
        self.health = 100  # Здоровье героя (начальное значение 100)
        self.attack_power = 20  # Сила атаки героя (начальное значение 20)

    # Метод для атаки другого героя
    def attack(self, other):
        # Уменьшаем здоровье другого героя (other) на величину своей атаки
        other.health -= self.attack_power
        # Возвращаем новое значение здоровья атакованного героя
        return other.health

    # Метод проверки, жив ли герой
    def is_alive(self):
        # Возвращает True, если здоровье больше 0, иначе False
        return self.health > 0


# Класс Game (Игра) - управляет процессом боя между героями
class Game:
    # Конструктор класса игры
    def __init__(self, player_name):
        # Создаем героя для игрока с указанным именем
        self.player = Hero(player_name)
        # Создаем героя для компьютера с именем "Компьютер"
        self.computer = Hero("Компьютер")

    # Основной метод, запускающий игру
    def start(self):
        current_turn = 0  # Счетчик ходов (0 - первый ход)

        # Основной цикл боя: продолжается, пока оба героя живы
        while self.player.is_alive() and self.computer.is_alive():
            # Определяем, чей сейчас ход (четный - игрок, нечетный - компьютер)
            if current_turn % 2 == 0:
                # Игрок атакует компьютер
                self.player.attack(self.computer)
                # Выводим информацию об атаке (max(0, health) чтобы здоровье не было отрицательным)
                print(
                    f"{self.player.name} атаковал(а)! У {self.computer.name} осталось {max(0, self.computer.health)} здоровья")
            else:
                # Компьютер атакует игрока
                self.computer.attack(self.player)
                # Выводим информацию об атаке
                print(
                    f"{self.computer.name} атаковал(а)! У {self.player.name} осталось {max(0, self.player.health)} здоровья")

            current_turn += 1  # Увеличиваем счетчик ходов

        # Определяем победителя (последний оставшийся в живых)
        winner = self.player.name if self.player.is_alive() else self.computer.name
        # Выводим сообщение о победе
        print(f"\nПобедитель: {winner}!")


# Стандартная проверка для запуска кода только при прямом выполнении файла
if __name__ == "__main__":
    # Запрашиваем у пользователя имя героя
    name = input("Введите имя вашего героя: ")
    # Создаем экземпляр игры с указанным именем игрока
    game = Game(name)
    # Запускаем игру
    game.start()