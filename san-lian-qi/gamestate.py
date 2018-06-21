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
        self.move_cnt = 0
        self.board = [[' ', ' ', ' '],   #表示棋盘。空格字符表示该格子为空。
                      [' ', ' ', ' '],   #O字母表示该格子下了白棋，X字母表示下了黑棋。
                      [' ', ' ', ' '] ]

    def set_player_side(self, side):
        self.player_side = side
        self.stage = PLAYING
        if side == DEFENSIVE_SIDE:
            self.computer_side = OFFENSIVE_SIDE
            self.computer_move()
        else:
            self.computer_side = DEFENSIVE_SIDE

    def stop_game(self):
        self.is_playing = False

    # def increase_round(self):
    #     self.move_cnt += 1

    def player_make_move(self, row, column):
        '''玩家在单元格(row, column)落子'''
        self.make_move(self.player_side, row, column)
        if self.player_wins():
            print("you wins!")
            self.stage = GAME_END
        if self.stage != GAME_END and self.move_cnt < 9:
            self.computer_move()
        if self.stage != GAME_END and self.move_cnt == 9:
            print("Duce.")
            self.stage = GAME_END


    def make_move(self, piece_type, row, column):
        GameState.make_move_on_board(self.board, piece_type, row, column)
        self.move_cnt += 1

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
            print("Computer wins!")
            self.stage = GAME_END
            return

        #找到玩家会获胜的落子位置，抢先落子
        player_win_cell = self.find_player_lucky_cell()
        if player_win_cell:
            r, c = player_win_cell
            self.make_move(self.computer_side, r, c)
            return

        #尝试在4个角落子
        for r in [0, 2]:
            for c in [0, 2]:
                if self.board[r][c] == GameState.BLANK_CELL:
                    self.make_move(self.computer_side, r, c)
                    return

        #尝试在中心落子
        if self.board[1][1] == GameState.BLANK_CELL:
            self.make_move(self.computer_side, 1, 1)
            return

        #在四个边落子
        for r, c in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            if self.board[r][c] == GameState.BLANK_CELL:
                self.make_move(self.computer_side, r, c)
                return


    def find_computer_lucky_cell(self):
        return self.find_lucky_cell(self.computer_side)

    def find_player_lucky_cell(self):
        return self.find_lucky_cell(self.player_side)

    def find_lucky_cell(self, side):
        for r in range(3):
            for c in range(3):
                board_copy = GameState.copy_board(self.board)
                if self.board[r][c] == GameState.BLANK_CELL:
                    GameState.make_move_on_board(board_copy, side, r, c)
                    if GameState.wins(board_copy, side):
                        return r, c
        return None

    @staticmethod
    def copy_board(board):
        copy = []
        for r in board:
            copy.append(r[:])
        return copy

    def computer_wins(self):
        return GameState.wins(self.board, self.computer_side)

    def player_wins(self):
        return GameState.wins(self.board, self.player_side)

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



