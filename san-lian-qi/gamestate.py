# @Time    : 2018/6/19 10:01
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
from settings import *
class GameState():
    def __init__(self):
        self.player_side = BLACK_SIDE   #默认为黑方
        self.after_selecting_side = False
        self.is_playing = True
        self.round_cnt = 0

    def set_player_side(self, side):
        self.player_side = side
        self.after_selecting_side = True

    def stop_game(self):
        self.is_playing = False
