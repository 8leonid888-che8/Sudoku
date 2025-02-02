import pygame


class StartScreen:
    def __init__(self, width, height):
        self.window = ["menu", "sign in", "rating"]
        self.window_pos = 0
        self.__width = width
        self.__height = height
        self.__label = None
        self.__sign_in = None
        self.__rating = None
        self.__input_user = None
        self.__button_play = None
        self.__name = "write your name"
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
        str_render = font.render(self.__name, 1, pygame.Color(color))
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

    def render(self, screen):
        color = "red"
        if self.window[self.window_pos] == "menu":
            self.__render_menu(screen, color)
        if self.window[self.window_pos] == "sign in":
            self.__render_sign_in(screen, color)

    def get_name(self, word):
        if self.__input_moment == 1:
            if word == "enter " and self.__name != "write your name":
                self.__input_moment = False
                return 1
            if word == "backspace " and len(self.__name) != 0:
                self.__name = self.__name[0:-1]
            else:
                if word.isalpha() or word.isdigit():
                    if self.__name == "write your name":
                        self.__name = word
                    else:
                        self.__name += word

        return 0

    def click(self, pos):
        if self.window[self.window_pos] == "menu":
            if self.__sign_in and self.__sign_in.collidepoint(pos):
                self.window_pos = 1

        if self.window[self.window_pos] == "sign in":
            if self.__input_user and self.__input_user.collidepoint(pos):
                self.__input_moment *= -1
            else:
                if self.__input_moment == 1:
                    self.__input_moment = -1
            if self.__button_play and self.__button_play.collidepoint(pos) and self.__name != "write your name":
                return 1
        return 0
