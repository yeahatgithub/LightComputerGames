# @Time    : 2018/6/17 10:56
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame
WHITE = (255, 255, 255)
LINE_COLOR = (0, 255, 0)
LINE_WIDTH = 5
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BOARD_SIZE = 300


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("三连棋")
    is_playing = True

    while is_playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False

        screen.fill(WHITE)
        draw_board(screen)
        pygame.display.update()

def draw_board(screen):
    for r in range(1, 3):
        left_top = ( (WINDOW_WIDTH - BOARD_SIZE) // 2, (WINDOW_HEIGHT - BOARD_SIZE)//2 + r * BOARD_SIZE // 3 )
        w_h = (BOARD_SIZE, 5)
        line = pygame.Rect(left_top, w_h)
        pygame.draw.rect(screen, LINE_COLOR, line)

    for c in range(1, 3):
        left_top = ( (WINDOW_WIDTH - BOARD_SIZE) // 2 + c * BOARD_SIZE // 3, (WINDOW_HEIGHT - BOARD_SIZE)//2 )
        w_h = (5, BOARD_SIZE)
        line = pygame.Rect(left_top, w_h)
        pygame.draw.rect(screen, LINE_COLOR, line)

if __name__ == "__main__":
    main()

