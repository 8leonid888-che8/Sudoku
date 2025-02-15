import pygame
from rating_bd import fetch_all_data


class StartScreen:
    def __init__(self, width, height):
        self.window = ["menu", "sign in", "choice level", "rating"]
        self.window_pos = 0
        self.__width = width
        self.__height = height
        self.__label = None
        self.__sign_in = None
        self.__rating = None
        self.__input_user = None
        self.__button_play = None
        self.__btn_medium_lvl = None
        self.__btn_easy_lvl = None
        self.__btn_hard_lvl = None
        self.name = "write your name"
        self.__input_moment = -1

    def __render_menu(self, screen, color):
        top = 0
        step = 20
        for i in ["Sudoku", "Sign in", "Rating"]:
            font = pygame.font.Font(None, 40)
            if i == "Sudoku":
                font = pygame.font.Font(None, 70)
            str_render = font.render(i, 1, pygame.Color(color))
            intro_rect = str_render.get_rect()
            if i == "Sudoku":
                intro_rect = [self.__width // 2 - intro_rect[2] // 2,
                              (self.__height // 2 - intro_rect[3] // 2 - 50), intro_rect[2], intro_rect[3]]
            else:
                intro_rect = [self.__width // 2 - intro_rect[2] // 2, top, intro_rect[2], intro_rect[3]]
            screen.blit(str_render, intro_rect)
            if i == "Sudoku":
                self.__label = pygame.Rect(intro_rect)
                top = self.__label.y + self.__label.height
            if i == "Sign in":
                self.__sign_in = pygame.Rect(intro_rect)
                top = self.__sign_in.y + self.__sign_in.height
            if i == "Rating":
                self.__rating = pygame.Rect(intro_rect)
                top = self.__rating.y + self.__rating.height
            top += step

    def __render_sign_in(self, screen, color):
        distance = 50
        font = pygame.font.Font(None, 30)
        str_render = font.render(self.name, 1, pygame.Color(color))
        intro_rect = str_render.get_rect()
        intro_rect = [self.__width // 2 - intro_rect[2] // 2, (self.__height // 2 - intro_rect[3] // 2 - 100),
                      intro_rect[2], intro_rect[3]]
        screen.blit(str_render, intro_rect)
        intro_rect[2] += 20
        intro_rect[3] += 10
        intro_rect = [self.__width // 2 - intro_rect[2] // 2, (self.__height // 2 - intro_rect[3] // 2 - 100),
                      intro_rect[2], intro_rect[3]]
        distance += intro_rect[1] + intro_rect[3]
        self.__input_user = pygame.Rect(intro_rect)
        pygame.draw.rect(screen, pygame.Color(color), intro_rect, 1)

        font_2 = pygame.font.Font(None, 70)
        play_str = font_2.render("Play", 1, pygame.Color(color))
        play_rect = play_str.get_rect()
        play_rect = [self.__width // 2 - play_rect[2] // 2, distance,
                     play_rect[2], play_rect[3]]
        self.__button_play = pygame.Rect(play_rect)
        screen.blit(play_str, play_rect)

    def __render_choice_lvl(self, screen, color):
        step = 4
        words = ["medium", "easy", "hard"]
        x_pos = length = 0
        y_pos = 0
        font = pygame.font.Font(None, 40)
        for word in words:
            str_render = font.render(word, 1, pygame.Color(color))
            word_rect = str_render.get_rect()
            word_rect = [self.__width // 2 - word_rect[2] // 2, (self.__height // 2 - word_rect[3] // 2 - 100),
                         word_rect[2], word_rect[3]]
            if word == "medium":
                x = word_rect[0]
                y_pos = word_rect[1] + word_rect[3]
                length = word_rect[2]
                screen.blit(str_render, word_rect)
                word_rect = [word_rect[0] - step, word_rect[1] - step, word_rect[2] + step * 2, word_rect[3] + step * 2]
                pygame.draw.rect(screen, pygame.Color(color), word_rect, 1)
                self.__btn_medium_lvl = pygame.Rect(word_rect)
            if word == "easy":
                word_rect[0] = word_rect[0] - 20 - length
                screen.blit(str_render, word_rect)
                word_rect = [word_rect[0] - step, word_rect[1] - step, word_rect[2] + step * 2, word_rect[3] + step * 2]
                pygame.draw.rect(screen, pygame.Color(color), word_rect, 1)
                self.__btn_easy_lvl = pygame.Rect(word_rect)
            if word == "hard":
                word_rect[0] = word_rect[0] + 20 + length
                screen.blit(str_render, word_rect)
                word_rect = [word_rect[0] - step, word_rect[1] - step, word_rect[2] + step * 2, word_rect[3] + step * 2]
                pygame.draw.rect(screen, pygame.Color(color), word_rect, 1)
                self.__btn_hard_lvl = pygame.Rect(word_rect)

    def __render_rating(self, screen, color):
        data = sorted(fetch_all_data(), key=lambda x: x[2], reverse=True)
        x = self.__width // 2
        top = 40
        step = 10
        for i in range(len(data)):
            font = pygame.font.Font(None, 30)
            str_render = font.render(f"{i + 1}. {data[i][1]} {data[i][2]}", 1, pygame.Color(color))
            rect = str_render.get_rect()
            rect.x = x - rect.w // 2
            rect.y = top + step
            top += step + rect.height
            screen.blit(str_render, rect)

    def render(self, screen):
        color = "red"
        if self.window[self.window_pos] == "menu":
            self.__render_menu(screen, color)
        if self.window[self.window_pos] == "sign in":
            self.__render_sign_in(screen, color)
        if self.window[self.window_pos] == "choice level":
            self.__render_choice_lvl(screen, color)
        if self.window[self.window_pos] == "rating":
            self.__render_rating(screen, color)

    def get_name(self, word):
        if self.__input_moment == 1:
            if word == "enter " and self.name != "write your name" and self.name != "":
                self.__input_moment = False
                self.window_pos = 2
                # return 1
            if word == "backspace " and len(self.name) != 0:
                self.name = self.name[0:-1]
            else:
                if word.isalpha() or word.isdigit():
                    if self.name == "write your name":
                        self.name = word
                    else:
                        self.name += word

    def click(self, pos):
        if self.window[self.window_pos] == "menu":
            if self.__sign_in and self.__sign_in.collidepoint(pos):
                self.window_pos = 1
            if self.__rating and self.__rating.collidepoint(pos):
                self.window_pos = 3

        if self.window[self.window_pos] == "sign in":
            if self.__input_user and self.__input_user.collidepoint(pos):
                self.__input_moment *= -1
            else:
                if self.__input_moment == 1:
                    self.__input_moment = -1
            if self.__button_play and self.__button_play.collidepoint(
                    pos) and self.name != "write your name" and self.name != "":
                self.window_pos = 2

        if self.window[self.window_pos] == "choice level":
            if self.__btn_easy_lvl and self.__btn_easy_lvl.collidepoint(pos):
                return 1
            if self.__btn_medium_lvl and self.__btn_medium_lvl.collidepoint(pos):
                return 2
            if self.__btn_hard_lvl and self.__btn_hard_lvl.collidepoint(pos):
                return 3

    def change_window(self):
        if self.window[self.window_pos] == "sign in" or self.window[self.window_pos] == "rating":
            self.window_pos = 0
        if self.window[self.window_pos] == "choice level":
            self.window_pos = 1
