# @Time    : 2018/6/19 10:01
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
from settings import *
class GameState():
    BLANK_CELL = ' '
    def __init__(self):
        self.player_side = None   #玩家先手还是后手？
        self.computer_side = None  #计算机先手还是后手？
        self.stage = CHOOSE_SIDE   #一共3个阶段。见GAME_STAGES的定义
        self.is_playing = True
        self.round_cnt = 0
        # self.next = ""   #下一步谁下子？next的取两种值："you"，"computer".
        self.board = [[' ', ' ', ' '],   #表示棋盘。空格字符表示该格子为空。
                      [' ', ' ', ' '],   #O字母表示该格子下了白棋，X字母表示下了黑棋。
                      [' ', ' ', ' '] ]

    def set_player_side(self, side):
        self.player_side = side
        self.stage = PLAYING
        if side == DEFENSIVE_SIDE:
            self.computer_side = OFFENSIVE_SIDE
            # self.next = "computer"
            self.computer_move()
            # self.next = "you"
        else:
            self.computer_side = DEFENSIVE_SIDE
            # self.next = "you"

    def stop_game(self):
        self.is_playing = False

    def increase_round(self):
        self.round_cnt += 1
        # if self.next == "you":
        #     self.next == "computer"
        # else:
        #     self.next = "you"

    def drop_piece(self, row, column):
        '''玩家在单元格(row, column)落子'''
        self.make_move(self.player_side, row, column)
        # self.next = "computer"
        self.computer_move()
        # self.next = "you"

    def make_move(self, piece_type, row, column):
        GameState.make_move_on_board(self.board, piece_type, row, column)

    @staticmethod
    def make_move_on_board(board, piece_type, row, column):
        board[row][column] = piece_type

    def print_board(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == ' ':
                    print('-', end='')
                else:
                    print(self.board[r][c])
            print()

    def computer_move(self):
        #找到使计算机获胜的落子
        computer_win_cell = self.find_computer_lucky_cell()
        if computer_win_cell:
            r, c = computer_win_cell
            self.make_move(self.computer_side, r, c)
        else:
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == GameState.BLANK_CELL:
                        self.make_move(self.computer_side, r, c)
                        return

    def find_computer_lucky_cell(self):
        for r in range(3):
            for c in range(3):
                board_copy = GameState.copy_board(self.board)
                if self.board[r][c] == GameState.BLANK_CELL:
                    GameState.make_move_on_board(board_copy, self.computer_side, r, c)
                    if self.computer_wins(board_copy):
                        return r, c
        return None

    @staticmethod
    def copy_board(board):
        copy = []
        for r in board:
            copy.append(r[:])
        return copy

    def computer_wins(self, board):
        return GameState.wins(board, self.computer_side)

    @staticmethod
    def wins(board, side):
        #行
        if board[0][0] == side and board[0][1] == side and board[0][2] == side:
            return True
        if board[1][0] == side and board[1][1] == side and board[1][2] == side:
            return True
        if board[2][0] == side and board[2][1] == side and board[2][2] == side:
            return True

        #列
        if board[0][0] == side and board[1][0] == side and board[2][0] == side:
            return True
        if board[0][1] == side and board[1][1] == side and board[2][1] == side:
            return True
        if board[0][2] == side and board[1][2] == side and board[2][2] == side:
            return True

        #对角线
        if board[0][0] == side and board[1][1] == side and board[2][2] == side:
            return True
        if board[0][2] == side and board[1][1] == side and board[2][0] == side:
            return True

        return False

