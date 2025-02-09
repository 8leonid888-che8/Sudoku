import pygame

from sudoku_generator import medium_lvl


class Result:
    def __init__(self, score, status, color):
        self.score = score
        self.status = status
        self.color = color
        self.width = 600
        self.height = 500
        self.status = "Victory"
        self.color = "red"
        self.name = None

    def set_score(self, score, status, width, height, name):
        self.score = score
        self.status = status
        self.width = width
        self.height = height
        self.name = name

    def render(self, screen):
        y = 20
        font = pygame.font.Font(None, 50)
        str_render = font.render(self.status, 1, pygame.Color(self.color))
        rect = str_render.get_rect()
        rect.center = [self.width // 2, self.height // 4]
        y += rect[1] + rect[3]
        screen.blit(str_render, rect)

        font = pygame.font.Font(None, 30)
        str_render = font.render(f"Score: {self.score}", 1, pygame.Color(self.color))
        rect = str_render.get_rect()
        rect.center = [self.width // 2, y]
        screen.blit(str_render, rect)
