# @Time    : 2018/6/17 10:56
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame
from settings import *
from gamestate import GameState
from gameresource import GameResource

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("三连棋")
    game_state = GameState()

    while game_state.is_playing:
        game_state = check_events(game_state)

        screen.fill(WHITE_BGCOLOR)
        draw_window(screen, game_state)
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

def draw_window(screen, game_state):
    draw_title(screen)

    if not game_state.after_selecting_side:
        draw_select_side(screen)
    else:
        draw_vs_img(screen, game_state.player_side)
        draw_whose_turn(screen, game_state.next)

    draw_board(screen)

def draw_title(screen):
    title_postion = (MARGIN_LEFT, MARGIN_TOP - 300)
    screen.blit(GameResource.load_game_title_img(), title_postion)


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
    select_tip_position = (MARGIN_LEFT - 200,  BLACK_SIDE_Y + 15)
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

def draw_vs_img(screen, player_side):
    computer_side = WHITE_SIDE if player_side == BLACK_SIDE else BLACK_SIDE
    side_position = (BLACK_SIDE_X - 120, BLACK_SIDE_Y - 40)
    if player_side == BLACK_SIDE:
        screen.blit(GameResource.load_you_x_vs_computer_o_img(), side_position)
    else:
        screen.blit(GameResource.load_you_o_vs_computer_x_img(), side_position)

def draw_whose_turn(screen, next):
    #白方先下
    # is_your_turn = (player_side == BLACK_SIDE and round_cnt % 2 == 1) or (player_side == WHITE_SIDE and round_cnt % 2 == 0)
    turn_position = (MARGIN_LEFT, MARGIN_TOP - 120)
    if next == "you":
        screen.blit(GameResource.load_your_turn_img(), turn_position)
    else:
        screen.blit(GameResource.load_computer_turn_img(), turn_position)

if __name__ == "__main__":
    main()

