import pygame


def start_screen():
    # реализовать авторизацию, рейтинг
    pass


class StartScreen:
    def __init__(self, width, height):
        self.__window = ["menu", "sign in", "rating"]
        self.__window_pos = 0
        self.__width = width
        self.__height = height
        self.__label = None
        self.__sign_in = None
        self.__rating = None
        self.__input_user = None
        self.__input_moment = -1

    def render(self, screen):
        color = "red"

        if self.__window[self.__window_pos] == "menu":
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

        if self.__window[self.__window_pos] == "sign in":
            name = "name"
            font = pygame.font.Font(None, 70)
            str_render = font.render(name, 1, pygame.Color(color))
            intro_rect = str_render.get_rect()
            intro_rect = [self.__width // 2 - intro_rect[2] // 2, (self.__height // 2 - intro_rect[3] // 2 - 50),
                          intro_rect[2], intro_rect[3]]
            screen.blit(str_render, intro_rect)
            intro_rect[2] += 100
            intro_rect = [self.__width // 2 - intro_rect[2] // 2, (self.__height // 2 - intro_rect[3] // 2 - 50),
                          intro_rect[2], intro_rect[3]]
            self.__input_user = pygame.Rect(intro_rect)
            pygame.draw.rect(screen, pygame.Color(color), intro_rect, 1)

    def click(self, pos):
        if self.__window[self.__window_pos] == "menu":
            if self.__sign_in and self.__sign_in.collidepoint(pos):
                self.__window_pos = 1

        if self.__window[self.__window_pos] == "sign in":
            if self.__input_user and self.__input_user.collidepoint(pos):
                self.__input_moment *= -1
