import pygame
from pygame import Color

from sudoku_generator import sudoku_generate

solution, task, missing_nums, dif = sudoku_generate(1)
print("dif", dif)
print(missing_nums)
print(solution)

print(task)


class Board:
    def __init__(self, n=3):
        self.n = n  # количество клеток в районе
        self.board = task
        for y in range(n ** 2):
            for x in range(n ** 2):
                val = self.board[y][x]
                if val:
                    self.board[y][x] = {"num": val, "change": False, "selected": False}
                else:
                    self.board[y][x] = {"num": 0, "change": True, "selected": False}

        # self.pressed_cell = [[False] * (n ** 2) for _ in range(n ** 2)]
        self.left = 10
        self.top = 10
        self.cell_size = 40
        self.line_width = 5
        self.width = n ** 2
        self.height = n ** 2
        self.moment_choice = False
        self.missing_nums = missing_nums
        self.last_selected_cell = None
        self.keys_missing_nums = list(self.missing_nums.keys())
        # self.game_board = [list(map(lambda x: False if x > 0 else 0, i)) for i in task]

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, x_point, y_point):
        if 0 <= x_point - self.left <= self.width * self.cell_size and 0 <= y_point - self.top <= self.height * self.cell_size:
            x_cell = (x_point - self.left) // self.cell_size
            y_cell = (y_point - self.top) // self.cell_size
            return x_cell, y_cell, "big"
        if 0 <= x_point - self.left <= self.width * self.cell_size and 0 <= y_point - (
                self.top + self.cell_size * 10 - 10) <= 2 * self.cell_size:
            x_cell = (x_point - self.left) // self.cell_size
            y_cell = (y_point - (self.top + self.cell_size * 10 - 10)) // self.cell_size
            return x_cell, y_cell, "small"
        else:
            return None

    def press_cell(self, pos):
        if pos == (-1, -1):
            if self.last_selected_cell is not None:
                self.board[self.last_selected_cell[1]][self.last_selected_cell[0]]["selected"] = False
            self.last_selected_cell = None
            return
        if pos[2] == "big":
            if not self.board[pos[1]][pos[0]]["num"]:
                if self.last_selected_cell:
                    self.board[self.last_selected_cell[1]][self.last_selected_cell[0]]["selected"] = False
                self.board[pos[1]][pos[0]]["selected"] = True
                self.moment_choice = True
                self.last_selected_cell = pos
            else:
                self.moment_choice = False
                if self.last_selected_cell is not None:
                    self.board[self.last_selected_cell[1]][self.last_selected_cell[0]]["selected"] = False
                    self.last_selected_cell = None
        if pos[2] == "small":
            if self.moment_choice:
                num = self.keys_missing_nums[pos[0]]
                if self.missing_nums[num] != 0 and self.last_selected_cell:
                    self.board[self.last_selected_cell[1]][self.last_selected_cell[0]]["num"] = num
                    self.missing_nums[num] -= 1

    def press_back(self, pos):
        x, y, _ = pos
        if pos[2] == "big":
            if self.board[y][x]["change"] and self.board[y][x]["num"]:
                num = self.board[y][x]["num"]
                self.board[y][x]["num"] = 0
                self.missing_nums[num] += 1
                self.board[y][x]["selected"] = False

    def render(self, screen):
        x, y = self.left, self.top
        for h in range(self.n ** 2):
            for w in range(self.n ** 2):
                if self.board[h][w]["selected"]:
                    pygame.draw.rect(screen, pygame.Color("red"), (x, y, self.cell_size, self.cell_size), 6)
                if h > 0 and h % 3 == 0:
                    pygame.draw.line(screen, pygame.Color("white"), (self.left, y),
                                     (self.left + self.cell_size * 9 - 1, y), self.line_width)
                    # горизонтальные
                if w > 0 and w % 3 == 0:
                    pygame.draw.line(screen, pygame.Color("white"), (x, self.top),
                                     (x, self.top + self.cell_size * 9 - 1), self.line_width)
                    # вертикальные
                if self.board[h][w]["num"] == 0:
                    pygame.draw.rect(screen, pygame.Color("white"), (x, y, self.cell_size, self.cell_size), 1)
                else:
                    font = pygame.font.Font(None, 35)
                    if self.board[h][w]["change"]:
                        text = font.render(str(self.board[h][w]["num"]), True, pygame.Color("blue"))
                    else:
                        text = font.render(str(self.board[h][w]["num"]), True, (100, 255, 100))

                    screen.blit(text, (x + 12, y + 8))
                    pygame.draw.rect(screen, pygame.Color("white"), (x, y, self.cell_size, self.cell_size), 1)
                x += self.cell_size
            x = self.left
            y += self.cell_size

        x, y = self.left, self.top + self.cell_size * 10 - 10

        for h in range(2):
            for w in range(self.n ** 2):
                if h == 0:
                    font = pygame.font.Font(None, 35)
                    text = font.render(str(self.keys_missing_nums[w]), True, Color("blue"))
                    screen.blit(text, (x + 12, y + 8))
                    pygame.draw.rect(screen, pygame.Color("white"), (x, y, self.cell_size, self.cell_size), 1)
                else:
                    font = pygame.font.Font(None, 35)
                    text = font.render(str(self.missing_nums[self.keys_missing_nums[w]]), True, Color("blue"))
                    screen.blit(text, (x + 12, y + 8))
                    pygame.draw.rect(screen, pygame.Color("white"), (x, y, self.cell_size, self.cell_size), 1)

                x += self.cell_size
            x = self.left
            y += self.cell_size
