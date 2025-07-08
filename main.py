# Импорт модуля sys для работы с системными функциями (в данном случае для sys.exit)
import sys


# Класс, представляющий героя в игре
class Hero:
    # Конструктор класса (вызывается при создании нового объекта Hero)
    def __init__(self, hero_name):
        """
        Инициализация героя
        :param hero_name: строка с именем героя
        """
        # Присваиваем имя героя (переданное в параметре)
        self.name = hero_name
        # Устанавливаем начальное значение здоровья
        self.health = 100
        # Устанавливаем силу атаки героя
        self.attack_power = 20

    # Метод для выполнения атаки другим героем
    def attack(self, other_hero):
        """
        Атака другого героя
        :param other_hero: объект Hero, который будет атакован
        :return: новое значение здоровья атакованного героя
        """
        # Уменьшаем здоровье атакуемого героя на величину атаки
        other_hero.health -= self.attack_power
        # Возвращаем новое значение здоровья
        return other_hero.health

    # Метод проверки, жив ли герой
    def is_alive(self):
        """
        Проверка состояния героя
        :return: True если герой жив (health > 0), иначе False
        """
        # Возвращаем результат сравнения здоровья с нулем
        return self.health > 0


# Класс, управляющий игровым процессом
class Game:
    # Конструктор класса Game
    def __init__(self, game_player_name):
        """
        Инициализация игры
        :param game_player_name: имя игрока (строка)
        """
        # Создаем героя для игрока с указанным именем
        self.player = Hero(game_player_name)
        # Создаем героя для компьютера со стандартным именем
        self.computer = Hero("Компьютер")

    # Основной метод, запускающий игровой процесс
    def start(self):
        """Запуск и управление игровым процессом"""
        # Счетчик ходов (для определения очередности атак)
        turn_counter = 0

        # Основной игровой цикл (пока оба героя живы)
        while self.player.is_alive() and self.computer.is_alive():
            # Если ход четный - атакует игрок
            if turn_counter % 2 == 0:
                # Игрок атакует компьютер
                self.player.attack(self.computer)
                # Вывод информации об атаке (max(0,...) предотвращает отрицательное здоровье)
                print(
                    f"{self.player.name} атаковал(а)! У {self.computer.name} осталось {max(0, self.computer.health)} здоровья")
            else:
                # Если ход нечетный - атакует компьютер
                self.computer.attack(self.player)
                # Вывод информации об атаке
                print(
                    f"{self.computer.name} атаковал! У {self.player.name} осталось {max(0, self.player.health)} здоровья")

            # Увеличиваем счетчик ходов
            turn_counter += 1

        # Определение победителя (последний выживший герой)
        winner = self.player.name if self.player.is_alive() else self.computer.name
        # Вывод сообщения о победителе
        print(f"\nПобедитель: {winner}!")


# Функция для получения и валидации имени игрока
def get_player_name_input():
    """
    Получение и проверка имени игрока
    :return: валидное имя игрока (строка)
    """
    # Бесконечный цикл, пока не будет введено корректное имя
    while True:
        try:
            # Получаем ввод от пользователя, удаляя пробелы по краям
            input_name = input("Введите имя вашего героя (от 2 до 20 символов): ").strip()

            # Проверка на пустую строку
            if not input_name:
                raise ValueError("Имя не может быть пустым")
            # Проверка минимальной длины
            if len(input_name) < 2:
                raise ValueError("Имя слишком короткое (минимум 2 символа)")
            # Проверка максимальной длины
            if len(input_name) > 20:
                raise ValueError("Имя слишком длинное (максимум 20 символов)")
            # Проверка на допустимые символы
            if not input_name.isprintable():
                raise ValueError("Имя содержит недопустимые символы")

            # Возвращаем валидное имя
            return input_name

        # Обработка ошибок валидации
        except ValueError as validation_error:
            print(f"Ошибка: {validation_error}. Пожалуйста, попробуйте еще раз.")
        # Обработка неожиданных ошибок
        except Exception as unexpected_error:
            print(f"Неожиданная ошибка: {unexpected_error}. Пожалуйста, попробуйте еще раз.")


# Основная точка входа в программу
if __name__ == "__main__":
    try:
        # Получаем валидное имя игрока
        validated_name = get_player_name_input()
        # Создаем экземпляр игры
        game_session = Game(validated_name)
        # Запускаем игровой процесс
        game_session.start()

    # Обработка прерывания программы (Ctrl+C)
    except KeyboardInterrupt:
        print("\nИгра прервана пользователем")
        # Корректный выход из программы
        sys.exit(0)

    # Обработка других критических ошибок
    except Exception as critical_error:
        print(f"Критическая ошибка: {critical_error}")
        # Выход с кодом ошибки
        sys.exit(1)