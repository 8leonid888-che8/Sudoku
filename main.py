import pygame

from game_screen import Board
from start_screen import StartScreen
from BackBtn import BackButton
from result import Result

window = ["start_screen", "game_screen", "result_screen"]
window_pos = 0


def main():
    global window_pos
    fps = 60
    color = "red"
    pygame.init()
    width = height = 500
    width = 600
    screen = pygame.display.set_mode((width, height))
    back_btn_group = pygame.sprite.Group()
    back_btn_group.add(BackButton(width, 10))
    start_screen = StartScreen(width, height)
    result = Result(0, None, color)
    board = Board(3, 1)
    board.set_view(width, height)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():

            ans_back_btn = False
            for btn in back_btn_group:
                ans_back_btn = btn.update(event)
                if ans_back_btn:
                    break

            if event.type == pygame.QUIT:
                running = False
            if window[window_pos] == "start_screen":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_screen.click(event.pos):
                        window_pos = 1
                if start_screen.window[start_screen.window_pos] == "sign in":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            start_screen.get_name("backspace ")
                        if event.key == pygame.K_RETURN:
                            start_screen.get_name("enter ")
                        else:
                            start_screen.get_name(event.unicode)
                if ans_back_btn:
                    start_screen.change_window()

                if start_screen.window[start_screen.window_pos] == "choice level":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        answer = start_screen.click(event.pos)
                        if answer:
                            board = Board(3, answer)
                            board.set_view(width, height)

            if window[window_pos] == "game_screen":
                answer_board = board.check_points_health()
                if answer_board:
                    window_pos = 2
                    score = board.score
                    status = answer_board
                    result.set_score(score, status, width, height, start_screen.name)
                if ans_back_btn:
                    window_pos = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = board.get_cell(*event.pos)
                    if position:
                        if event.button == 1:
                            if position[2] == "small":
                                board.press_cell(position)
                            else:
                                board.press_back(position)
                                board.press_cell(position)
                        if event.button == 3:
                            pass
                    else:
                        board.press_cell((-1, -1))

        if window[window_pos] == "result_screen":
            if ans_back_btn:
                window_pos = 0
                start_screen = StartScreen(width, height)

        if window[window_pos] == "game_screen":
            board.render(screen)

        if window[window_pos] == "start_screen":
            start_screen.render(screen)

        if window[window_pos] == "result_screen":
            result.render(screen)
        back_btn_group.draw(screen)
        pygame.display.update()
        screen.fill((0, 0, 0))
        clock.tick(fps)


pygame.quit()

if __name__ == "__main__":
    main()
