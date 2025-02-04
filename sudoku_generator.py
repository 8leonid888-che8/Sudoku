import random
from math import floor

# Уровни сложности
easy_lvl = 45
middle_lvl = 35
hard_lvl = 25
legendary_lvl = 17  # Уменьшим количество оставшихся чисел для уровня "легенда"


class Grid:
    def __init__(self, n=3):
        """ Генерация базовой таблицы """
        self.n = n
        self.table = [[floor((i * n + j) % (n * n) + 1) for j in range(n * n)] for i in range(n * n)]
        print("Базовая таблица готова!")

    def show(self):
        for row in self.table:
            print(row)

    def transposing(self):
        """ Транспонирование всей сетки """
        self.table = list(map(list, zip(*self.table)))

    def swap_rows_small(self):
        """ Обмен двух строк внутри одной области """
        area = random.randrange(0, self.n)
        line1, line2 = random.sample(range(self.n), 2)
        N1 = area * self.n + line1
        N2 = area * self.n + line2
        self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def swap_columns_small(self):
        self.transposing()
        self.swap_rows_small()
        self.transposing()

    def swap_rows_area(self):
        """ Обмен двух областей """
        area1, area2 = random.sample(range(self.n), 2)
        for i in range(self.n):
            N1, N2 = area1 * self.n + i, area2 * self.n + i
            self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def swap_columns_area(self):
        self.transposing()
        self.swap_rows_area()
        self.transposing()

    def mix(self, amt=10):
        mix_funcs = [
            self.transposing,
            self.swap_rows_small,
            self.swap_columns_small,
            self.swap_rows_area,
            self.swap_columns_area
        ]
        for _ in range(amt):
            random.choice(mix_funcs)()


def sudoku_generate(diff):
    example = Grid()
    example.mix()

    flook = [[0] * (example.n * example.n) for _ in range(example.n * example.n)]
    iterator = 0
    difficult = example.n * example.n * example.n * example.n  # Изначально все элементы на месте
    solution = [row[:] for row in example.table]  # Копируем начальное решение

    missing_nums = {i: 0 for i in range(1, example.n * example.n + 1)}

    while iterator < example.n ** 4:
        if ((diff == 1 and difficult <= easy_lvl) or
                (diff == 2 and difficult <= middle_lvl) or
                (diff == 3 and difficult <= hard_lvl) or
                (diff == 4 and difficult <= legendary_lvl)):
            break

        i, j = random.randrange(0, example.n * example.n), random.randrange(0, example.n * example.n)

        if flook[i][j] == 0:
            iterator += 1
            flook[i][j] = 1

            temp = example.table[i][j]
            example.table[i][j] = 0
            difficult -= 1
            missing_nums[temp] += 1

    print(f"Сгенерировано судоку уровня {diff} с {difficult} известными числами.")
    example.show()
    task = example.table
    return solution, task, missing_nums, difficult


