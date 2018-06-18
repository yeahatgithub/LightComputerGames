# @Time    : 2018/6/17 10:56
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 255)
BLACK = (0, 0, 0)
SELECT_AREA_BGCOLOR =  (250, 100, 50)

LINE_WIDTH = 5
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BOARD_SIZE = 300
MARGIN_TOP = (WINDOW_HEIGHT - BOARD_SIZE)//2
MARGIN_LEFT = (WINDOW_WIDTH - BOARD_SIZE) // 2


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
        draw_select_side(screen)
        pygame.display.update()

def draw_board(screen):
    for r in range(1, 3):
        left_top = ( MARGIN_LEFT, MARGIN_TOP + r * BOARD_SIZE // 3 )
        w_h = (BOARD_SIZE, 5)
        line = pygame.Rect(left_top, w_h)
        pygame.draw.rect(screen, LINE_COLOR, line)

    for c in range(1, 3):
        left_top = ( MARGIN_LEFT + c * BOARD_SIZE // 3,  MARGIN_TOP)
        w_h = (5, BOARD_SIZE)
        line = pygame.Rect(left_top, w_h)
        pygame.draw.rect(screen, LINE_COLOR, line)

def draw_select_side(screen):
    select_tip_font = pygame.font.SysFont('simhei', 24)
    select_tip_surface = select_tip_font.render('点击鼠标选择：', False, BLACK)
    select_tip_position = (MARGIN_LEFT, MARGIN_TOP - 200)
    screen.blit(select_tip_surface, select_tip_position)

    draw_select_button(screen, MARGIN_LEFT, MARGIN_TOP - 150, '选黑棋(X)')
    draw_select_button(screen, MARGIN_LEFT + 150, MARGIN_TOP - 150, '选白棋(O)')

def draw_select_button(screen, x, y, btn_label):
    side_rect = (x, y, 130, 50)
    pygame.draw.rect(screen, SELECT_AREA_BGCOLOR, side_rect)

    side_font = pygame.font.SysFont('simhei', 28)
    side_surface = side_font.render(btn_label, False, BLACK)
    side_position = (x + 5, y + 10)
    screen.blit(side_surface, side_position)

if __name__ == "__main__":
    main()
