import pygame
from pygame.examples.moveit import WIDTH

from game_screen import Board
from start_screen import StartScreen
window = ["start_screen", "game_screen"]
window_pos = 0


def main():
    global window_pos
    fps = 60
    pygame.init()
    width = 501
    height = 501
    screen = pygame.display.set_mode((501, 501))
    board = Board()
    start_screen = StartScreen(width, height)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if window[window_pos] == "start_screen":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    window_pos = start_screen.click(event.pos)
                if start_screen.window[start_screen.window_pos] == "sign in":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            start_screen.get_name("backspace ")
                        if event.key == pygame.K_RETURN:
                            window_pos = start_screen.get_name("enter ")

                        else:
                            start_screen.get_name(event.unicode)


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

        if window[window_pos] == "start_screen":
            start_screen.render(screen)
        pygame.display.update()
        screen.fill((0,0,0))
        clock.tick(fps)


pygame.quit()


if __name__ == "__main__":
    main()
