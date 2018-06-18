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

BLACK_SIDE = 'X'
WHITE_SIDE = 'O'
BLACK_SIDE_X = MARGIN_LEFT
BLACK_SIDE_Y = MARGIN_TOP - 150
WHITE_SIDE_X = MARGIN_LEFT + 150
WHITE_SIDE_Y = MARGIN_TOP - 150
SELECT_AREA_WIDTH = 130
SELECT_AREA_HEIGHT = 50

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("三连棋")
    game_state = GameState()

    while game_state.is_playing:
        game_state = check_events(game_state)

        screen.fill(WHITE)
        draw_board(screen)
        if not game_state.after_selecting_side:
            draw_select_side(screen)
        else:
            draw_whose_turn(screen, game_state.player_side)
        pygame.display.update()

def check_events(game_state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.stop_game()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            if select_black_side(click_pos):
                game_state.set_player_side(BLACK_SIDE)

            if select_white_side(click_pos):
                game_state.set_player_side(WHITE_SIDE)

    return game_state

def select_black_side(click_pos):
    return BLACK_SIDE_X <= click_pos[0] <= BLACK_SIDE_X + SELECT_AREA_WIDTH \
            and BLACK_SIDE_Y <= click_pos[1] <= BLACK_SIDE_Y + SELECT_AREA_HEIGHT

def select_white_side(click_pos):
    return WHITE_SIDE_X <= click_pos[0] <= WHITE_SIDE_X + SELECT_AREA_WIDTH \
            and WHITE_SIDE_Y <= click_pos[1] <= WHITE_SIDE_Y + SELECT_AREA_HEIGHT

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

    draw_select_button(screen, BLACK_SIDE_X, BLACK_SIDE_Y, '选黑棋(X)')
    draw_select_button(screen, WHITE_SIDE_X, WHITE_SIDE_Y, '选白棋(O)')

def draw_select_button(screen, x, y, btn_label):
    side_rect = (x, y, 130, 50)
    pygame.draw.rect(screen, SELECT_AREA_BGCOLOR, side_rect)

    side_font = pygame.font.SysFont('simhei', 28)
    side_surface = side_font.render(btn_label, False, BLACK)
    side_position = (x + 5, y + 10)
    screen.blit(side_surface, side_position)

def draw_whose_turn(screen, player_side):
    computer_side = WHITE_SIDE if player_side == 'X' else BLACK_SIDE
    vs_str = "你(" + player_side + ")  VS  电脑(" + computer_side + ")"

    side_font = pygame.font.SysFont('simhei', 28)
    side_surface = side_font.render(vs_str, False, BLACK)
    side_position = (BLACK_SIDE_X, BLACK_SIDE_Y)
    screen.blit(side_surface, side_position)

class GameState():
    def __init__(self):
        self.player_side = BLACK_SIDE   #默认为黑方
        self.after_selecting_side = False
        self.is_playing = True

    def set_player_side(self, side):
        self.player_side = side
        self.after_selecting_side = True

    def stop_game(self):
        self.is_playing = False

if __name__ == "__main__":
    main()

