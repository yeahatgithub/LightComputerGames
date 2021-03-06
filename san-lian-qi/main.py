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
            if game_state.stage == CHOOSE_SIDE:
                if select_defensive_side(click_pos):
                    game_state.set_player_side(DEFENSIVE_SIDE)
                if select_offensive_side(click_pos):
                    game_state.set_player_side(OFFENSIVE_SIDE)
            elif game_state.stage == PLAYING:
                if valid_drop(click_pos, game_state):
                    drop_cell = find_cell(click_pos)
                    game_state.player_make_move(drop_cell[0], drop_cell[1])
                    # game_state.print_board()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_state.stage == GAME_END:
                game_state = GameState()

    return game_state


def valid_drop(click_pos, game_state):
    '''鼠标点击在可以落子的格子上吗？'''
    if click_pos[0] <= MARGIN_LEFT or click_pos[0] >= MARGIN_LEFT + BOARD_SIZE \
        or click_pos[1] <= MARGIN_TOP or click_pos[1] >= MARGIN_TOP + BOARD_SIZE:
        return False

    click_x_board = click_pos[0] - MARGIN_LEFT
    click_y_board = click_pos[1] - MARGIN_TOP
    cell_width = BOARD_SIZE // 3
    c = click_x_board // cell_width
    r = click_y_board // cell_width
    #点击位置落在单元格边界线附近吗？
    border = 5
    if (c * cell_width + border <= click_x_board <= (c + 1) * cell_width - border ) \
        and (r * cell_width + border <= click_y_board <= (r + 1) * cell_width - border):
        if game_state.board[r][c] == GameState.BLANK_CELL:
            return True
        else:
            return False
    else:      #点在单元格边界线上的话，视为无效
        return False

def find_cell(click_pos):
    '''点击的是哪一个格子？'''
    click_x_board = click_pos[0] - MARGIN_LEFT
    click_y_board = click_pos[1] - MARGIN_TOP
    cell_width = BOARD_SIZE // 3
    row = click_y_board // cell_width
    column = click_x_board // cell_width
    assert(0 <= row <= 3)
    assert(0 <= column <= 3)
    return (row, column)


def select_defensive_side(click_pos):
    return DEFENSIVE_SIDE_X <= click_pos[0] <= DEFENSIVE_SIDE_X + BUTTON_WIDTH \
           and DEFENSIVE_SIDE_Y <= click_pos[1] <= DEFENSIVE_SIDE_Y + BUTTON_HEIGHT

def select_offensive_side(click_pos):
    return OFFENSIVE_SIDE_X <= click_pos[0] <= OFFENSIVE_SIDE_X + BUTTON_WIDTH \
           and OFFENSIVE_SIDE_Y <= click_pos[1] <= OFFENSIVE_SIDE_Y + BUTTON_HEIGHT

def draw_window(screen, game_state):
    draw_title(screen)

    if game_state.stage == CHOOSE_SIDE:
        draw_select_side(screen)
    else:
        draw_vs_img(screen, game_state.player_side)
        draw_board(screen, game_state)
        if game_state.stage == GAME_END:
            draw_winner_img(screen, game_state.winner)
            draw_newgame_img(screen)

def draw_title(screen):
    title_postion = (MARGIN_LEFT, MARGIN_TOP - 300)
    screen.blit(GameResource.load_game_title_img(), title_postion)


def draw_board(screen, game_state):
    cell_width = BOARD_SIZE // 3
    for r in range(1, 3):
        left_top = ( MARGIN_LEFT, MARGIN_TOP + r * cell_width )
        w_h = (BOARD_SIZE, 5)
        line = pygame.Rect(left_top, w_h)
        pygame.draw.rect(screen, LINE_COLOR, line)

    for c in range(1, 3):
        left_top = ( MARGIN_LEFT + c * cell_width,  MARGIN_TOP)
        w_h = (5, BOARD_SIZE)
        line = pygame.Rect(left_top, w_h)
        pygame.draw.rect(screen, LINE_COLOR, line)

    for r in range(3):
        for c in range(3):
            if game_state.board[r][c] != GameState.BLANK_CELL:
                draw_piece(screen, (r, c),
                           game_state.board[r][c])

def draw_piece(screen, cell, piece_type):
    cell_width = BOARD_SIZE // 3
    r, c = cell
    left = MARGIN_LEFT + 25 + c * cell_width
    top = MARGIN_TOP + 25 + r * cell_width
    if piece_type == DEFENSIVE_SIDE:
        screen.blit(GameResource.load_x_piece_img(), (left, top))
    else:
        screen.blit(GameResource.load_o_piece_img(), (left, top))


def draw_select_side(screen):
    select_tip_font = pygame.font.SysFont('simhei', 24)
    select_tip_surface = select_tip_font.render('点击鼠标选择：', False, BLACK)
    select_tip_position = (MARGIN_LEFT - 200, DEFENSIVE_SIDE_Y + 15)
    screen.blit(select_tip_surface, select_tip_position)

    draw_select_button(screen, DEFENSIVE_SIDE_X, DEFENSIVE_SIDE_Y, '选后手(X)')
    draw_select_button(screen, OFFENSIVE_SIDE_X, OFFENSIVE_SIDE_Y, '选先手(O)')

    demo_position = (MARGIN_LEFT - 100, DEFENSIVE_SIDE_Y + 100)
    screen.blit(GameResource.load_howto_sanlianqi_img(), demo_position)

def draw_select_button(screen, x, y, btn_label):
    side_rect = (x, y, 130, 50)
    pygame.draw.rect(screen, SELECT_AREA_BGCOLOR, side_rect)

    side_font = pygame.font.SysFont('simhei', 28)
    side_surface = side_font.render(btn_label, False, BLACK)
    side_position = (x + 5, y + 10)
    screen.blit(side_surface, side_position)

def draw_vs_img(screen, player_side):
    computer_side = OFFENSIVE_SIDE if player_side == DEFENSIVE_SIDE else DEFENSIVE_SIDE
    side_position = (DEFENSIVE_SIDE_X - 120, DEFENSIVE_SIDE_Y - 40)
    if player_side == DEFENSIVE_SIDE:
        screen.blit(GameResource.load_you_x_vs_computer_o_img(), side_position)
    else:
        screen.blit(GameResource.load_you_o_vs_computer_x_img(), side_position)


def draw_winner_img(screen, winner):
    img_postion = (MARGIN_LEFT + 50, MARGIN_TOP + 50)
    if winner == "player":
        screen.blit(GameResource.load_you_won_img(), img_postion)
    elif winner == "duce":
        screen.blit(GameResource.load_duce_img(), img_postion)
    else:
        screen.blit(GameResource.load_computer_won_img(), img_postion)

def draw_newgame_img(screen):
    img_position = (MARGIN_LEFT - 50, MARGIN_TOP + BOARD_SIZE + 50)
    screen.blit(GameResource.load_newgame_tip_img(), img_position)

if __name__ == "__main__":
    main()

