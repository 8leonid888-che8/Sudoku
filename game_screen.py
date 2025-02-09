import pygame
from pygame import Color
# from BackBtn import BackButton
from sudoku_generator import sudoku_generate
import copy


# solution, task, missing_nums, dif = sudoku_generate(1)
# print("dif", dif)
# print(missing_nums)
# print(solution)
# print(task)


class Board:
    def __init__(self, n=3, lvl=1):
        self.n = n  # количество клеток в районе
        self.__solution, self.board, self.missing_nums, diff, self.lvl = sudoku_generate(lvl)
        # self.board = copy.deepcopy(self.__solution)
        # self.board[0][0] = 0
        print(self.__solution)
        print(self.board)
        print(diff, self.lvl)
        for y in range(n ** 2):
            for x in range(n ** 2):
                val = self.board[y][x]
                if val:
                    self.board[y][x] = {"num": val, "change": False, "selected": False}
                else:
                    self.board[y][x] = {"num": 0, "change": True, "selected": False, "correct": None}
        self.left = 10
        self.top = 10
        self.cell_size = 40
        self.line_width = 5
        self.width = n ** 2
        self.height = n ** 2
        self.moment_choice = False
        self.last_selected_cell = None
        self.keys_missing_nums = list(self.missing_nums.keys())
        self.score = 0
        self.health = 3
        self.k = 1
        self.color = "red"
        self.width = None
        self.height = None
        self.last_val = None
        # self.btn_back = pygame.sprite.Group()
        # BackButton(self.width, self.top, self.btn_back)

    def set_view(self, width, height):
        self.cell_size = round(40 * height / 500)
        # self.left = round((width // 2 - self.cell_size * 9 // 2) * 0.5)
        self.left = 30
        self.top = 20
        self.k = height / 500
        self.width = width
        self.height = height
        # print(self.k)

    def get_cell(self, x_point, y_point):
        if 0 <= x_point - self.left <= self.width * self.cell_size and 0 <= y_point - self.top <= self.height * self.cell_size:
            x_cell = (x_point - self.left) // self.cell_size
            y_cell = (y_point - self.top) // self.cell_size
            if 0 <= x_cell <= 8 and 0 <= y_cell <= 8:
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
                if self.last_selected_cell and self.board[self.last_selected_cell[1]][self.last_selected_cell[0]]["num"] == num:
                    return
                if self.missing_nums[num] != 0 and self.last_selected_cell:
                    n = self.board[self.last_selected_cell[1]][self.last_selected_cell[0]]["num"]
                    if n != 0:
                        self.missing_nums[n] += 1
                        self.check(self.last_selected_cell, "del")
                    self.board[self.last_selected_cell[1]][self.last_selected_cell[0]]["num"] = num
                    self.missing_nums[num] -= 1
                    self.last_val = num
            self.check(self.last_selected_cell, "add")

    def press_back(self, pos):
        x, y, _ = pos
        print(pos)
        if pos[2] == "big":
            if self.board[y][x]["change"] and self.board[y][x]["num"]:
                num = self.board[y][x]["num"]
                self.board[y][x]["num"] = 0
                self.missing_nums[num] += 1
                self.board[y][x]["selected"] = False
                self.press_cell(pos)
                self.check(pos, "del")

    def check(self, pos, latter):
        if pos:
            x, y, _ = pos
            if latter == "add":
                if self.board[y][x]["change"]:
                    if self.board[y][x]["num"] == self.__solution[y][x]:
                        self.board[y][x]["correct"] = True
                        self.board[y][x]["change"] = False
                        self.board[y][x]["selected"] = False
                        self.last_selected_cell = None
                        if self.lvl == 1:
                            self.score += 35 * self.lvl
                        if self.lvl == 2:
                            self.score += 45 * self.lvl
                        if self.lvl == 3:
                            self.score += 63 * self.lvl
                    else:
                        self.board[y][x]["correct"] = False
                        if self.health != 0:
                            self.health -= 1
            if latter == "del":
                print("dell")
                if self.board[y][x]["correct"]:
                    self.board[y][x]["correct"] = None
                    if self.score > 0:
                        if self.lvl == 1:
                            self.score -= 35 * self.lvl
                        if self.lvl == 2:
                            self.score -= 45 * self.lvl
                        if self.lvl == 3:
                            self.score -= 63 * self.lvl

            print(pos, "pos", self.board[y][x])
            print(self.score)

    # def press_back_btn(self, arg):
    #     answer  = self.btn_back.update(*arg)

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
                    font = pygame.font.Font(None, round(35 * self.k))
                    if self.board[h][w]["change"]:
                        if self.board[h][w]["correct"]:
                            text = font.render(str(self.board[h][w]["num"]), True, pygame.Color("blue"))
                        else:
                            text = font.render(str(self.board[h][w]["num"]), True, pygame.Color("red"))
                    else:
                        text = font.render(str(self.board[h][w]["num"]), True, (100, 255, 100))
                    text_rect = text.get_rect()
                    # text_rect = [x + round(text_rect[2] / 1.7), y + round(text_rect[3] / 1.8), text_rect[2], text_rect[3]]
                    screen.blit(text, (round(x + 13 * self.k), round(y + 10 * self.k)))
                    pygame.draw.rect(screen, pygame.Color("white"), (x, y, self.cell_size, self.cell_size), 1)
                x += self.cell_size
            x = self.left
            y += self.cell_size

        x, y = self.left, self.top + self.cell_size * 10 - 10

        for h in range(2):
            font = pygame.font.Font(None, round(35 * self.k))
            for w in range(self.n ** 2):
                if h == 0:
                    # font = pygame.font.Font(None, round(35 * self.k))
                    text = font.render(str(self.keys_missing_nums[w]), True, Color("blue"))
                    screen.blit(text, (round(x + 13 * self.k), round(y + 10 * self.k)))
                    pygame.draw.rect(screen, pygame.Color("white"), (x, y, self.cell_size, self.cell_size), 1)
                else:
                    # font = pygame.font.Font(None, round(35 * self.k))
                    text = font.render(str(self.missing_nums[self.keys_missing_nums[w]]), True, Color("blue"))
                    screen.blit(text, (round(x + 13 * self.k), round(y + 10 * self.k)))
                    pygame.draw.rect(screen, pygame.Color("white"), (x, y, self.cell_size, self.cell_size), 1)

                x += self.cell_size
            x = self.left
            y += self.cell_size

        y = self.top + self.cell_size
        font = pygame.font.Font(None, round(35 * self.k))
        text = font.render(f"score: {self.score}", True, self.color)
        text_rect = text.get_rect()
        x = round((self.width - self.left - self.cell_size * 9) / 2 - text_rect[2] / 2) + self.left + self.cell_size * 9
        text_rect = [x, y, text_rect[2], text_rect[3]]
        screen.blit(text, text_rect)
        # self.btn_back.draw(screen)

    def check_points_health(self):
        f = []
        for y in self.board:
            for x in y:
                if x["change"]:
                    f.append(x["num"] != 0 and x["correct"])
        if self.health == 0:
            print(self.health, f)
            self.health = 3
            return "Game over"
        if all(f):
            self.health = 3
            return "Victory"
