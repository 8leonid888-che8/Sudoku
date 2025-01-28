import pygame
from game_screen import Board

window = ["start_screen", "game_screen"]
window_pos = 1


def main():
    fps = 60
    pygame.init()
    screen = pygame.display.set_mode((501, 501))
    board = Board()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if window[window_pos] == "game_screen":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = board.get_cell(*event.pos)
                    if position:
                        if event.button == 1:
                            board.press_cell(position)
                            board.press_back(position)
                        if event.button == 3:
                            pass
                    else:
                        board.press_cell((-1, -1))
                    print(position)


        if window[window_pos] == "game_screen":
            board.render(screen)
        pygame.display.update()
        screen.fill((0,0,0))
        clock.tick(fps)


pygame.quit()


if __name__ == "__main__":
    main()
