import pygame
from sudoku_generator import sudoku_generate
sudoku_generate(1)
from sudoku_generator import task, solution


class Board:
    def __init__(self, n=3):
        self.n = n # количество клеток в районе
        self.board = task
        self.left = 10
        self.top = 10
        self.cell_size = 40
        self.line_width = 5

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        x, y = self.left, self.top
        for h in range(self.n ** 2):
            for w in range(self.n ** 2):
                if h > 0 and h % 3 == 0:
                    pygame.draw.line(screen, pygame.Color("white"), (self.left, y), (self.left + self.cell_size * 9, y), self.line_width)
                if w > 0 and w % 3 == 0:
                    pygame.draw.line(screen, pygame.Color("white"), (x, self.top), (x, self.top + self.cell_size * 9), self.line_width)

                if self.board[h][w] == 0:
                    pygame.draw.rect(screen, pygame.Color("white"), (x, y, self.cell_size, self.cell_size), 1)
                else:
                    font = pygame.font.Font(None, 35)
                    text = font.render(str(self.board[h][w]), True, (100, 255, 100))
                    screen.blit(text, (x + 12, y + 8))
                    pygame.draw.rect(screen, pygame.Color("white"), (x, y, self.cell_size, self.cell_size), 1)
                x += self.cell_size
            x = self.left
            y += self.cell_size


def main():
    pygame.init()
    screen = pygame.display.set_mode((501, 501))
    board = Board()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.render(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()