# @Time    : 2018/6/19 10:01
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
from settings import *
class GameState():
    BLANK_CELL = ' '
    def __init__(self):
        self.player_side = None   #玩家下哪种子？
        self.stage = CHOOSE_SIDE   #一共3个阶段。见GAME_STAGES的定义
        self.is_playing = True
        self.round_cnt = 0
        self.next = ""   #下一步谁下子？next的取两种值："you"，"computer".
        self.board = [[' ', ' ', ' '],   #表示棋盘。空格字符表示该格子为空。
                      [' ', ' ', ' '],   #O字母表示该格子下了白棋，X字母表示下了黑棋。
                      [' ', ' ', ' '] ]

    def set_player_side(self, side):
        self.player_side = side
        self.stage = PLAYING
        if side == DEFENSIVE_SIDE:
            self.next = "computer"
        else:
            self.next = "you"

    def stop_game(self):
        self.is_playing = False

    def increase_round(self):
        self.round_cnt += 1
        if self.next == "you":
            self.next == "computer"
        else:
            self.next = "you"

    def drop_piece(self, row, column):
        '''玩家在单元格(row, column)落子'''
        self.next = "computer"
        self.set_board_cell(self.player_side, row, column)

    def set_board_cell(self, piece_type, row, column):
        self.board[row][column] = piece_type

    def print_board(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == ' ':
                    print('-', end='')
                else:
                    print(self.board[r][c])
            print()
