import random
import solver
from math import floor

easy_lvl = 45
medium_lvl = 35
hard_lvl = 25
legendary_lvl = 12
class Grid:
    def __init__(self, n=3):
        """ Generation of the base table """
        self.n = n
        self.table = [[floor((i * n + i / n + j) % (n * n) + 1) for j in range(n * n)] for i in range(n * n)]
        print("The base table is ready!")

    def __del__(self):
        pass

    def show(self):
        for i in range(self.n * self.n):
            print(self.table[i])

    def transposing(self):
        """ Transposing the whole grid """
        self.table = list(map(list, zip(*self.table)))

    def swap_rows_small(self):
        """ Swap the two rows """
        area = random.randrange(0, self.n, 1)
        line1 = random.randrange(0, self.n, 1)
        # получение случайного района и случайной строки
        N1 = area * self.n + line1
        # номер 1 строки для обмена

        line2 = random.randrange(0, self.n, 1)
        # случайная строка, но не та же самая
        while (line1 == line2):
            line2 = random.randrange(0, self.n, 1)

        N2 = area * self.n + line2
        # номер 2 строки для обмена

        self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def swap_colums_small(self):
        Grid.transposing(self)
        Grid.swap_rows_small(self)
        Grid.transposing(self)

    def swap_rows_area(self):
        """ Swap the two area horizon """
        area1 = random.randrange(0, self.n, 1)
        # получение случайного района

        area2 = random.randrange(0, self.n, 1)
        # ещё район, но не такой же самый
        while (area1 == area2):
            area2 = random.randrange(0, self.n, 1)

        for i in range(0, self.n):
            N1, N2 = area1 * self.n + i, area2 * self.n + i
            self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def swap_colums_area(self):
        Grid.transposing(self)
        Grid.swap_rows_area(self)
        Grid.transposing(self)

    def mix(self, amt=10):
        mix_func = ['self.transposing()',
                    'self.swap_rows_small()',
                    'self.swap_colums_small()',
                    'self.swap_rows_area()',
                    'self.swap_colums_area()']
        for i in range(1, amt):
            id_func = random.randrange(0, len(mix_func), 1)
            eval(mix_func[id_func])


example = Grid()
example.mix()
flook = [[0 for j in range(example.n * example.n)] for i in range(example.n * example.n)]
iterator = 0
difficult = example.n ** 4  # Первоначально все элементы на месте
solution = example.table


def sudoku_generate(diff=3):
    global difficult, iterator
    example = Grid()
    example.mix()
    flook = [[0 for j in range(example.n * example.n)] for i in range(example.n * example.n)]
    iterator = 0
    difficult = example.n ** 4  # Первоначально все элементы на месте
    solution = example.table.copy()
    missing_nums = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    while iterator < example.n ** 4:
        if diff == 1 and difficult == easy_lvl:
            break
        if diff == 2 and difficult ==medium_lvl:
            break
        if diff == 3 and difficult == hard_lvl:
            break
        if diff == 4 and difficult == legendary_lvl:
            break

        i, j = random.randrange(0, example.n * example.n, 1), random.randrange(0, example.n * example.n,
                                                                               1)  # Выбираем случайную ячейку
        if flook[i][j] == 0:  # Если её не смотрели
            iterator += 1
            flook[i][j] = 1  # Посмотрим

            temp = example.table[i][j]  # Сохраним элемент на случай если без него нет решения или их слишком много
            example.table[i][j] = 0
            difficult -= 1  # Усложняем если убрали элемент
            missing_nums[temp] += 1

            table_solution = []
            for copy_i in range(0, example.n * example.n):
                table_solution.append(example.table[copy_i][:])  # Скопируем в отдельный список

            i_solution = 0
            for solution in solver.solve_sudoku((example.n, example.n), table_solution):
                i_solution += 1  # Считаем количество решений

            if i_solution != 1:  # Если решение не одинственное вернуть всё обратно
                example.table[i][j] = temp
                difficult += 1  # Облегчаем
                missing_nums[temp] -= 1
    task = example.table
    return solution, task, missing_nums, difficult
