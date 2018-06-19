# @Time    : 2018/6/19 10:01
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
from settings import *
class GameState():
    def __init__(self):
        self.player_side = None   #玩家下哪种子？
        self.after_selecting_side = False
        self.is_playing = True
        self.round_cnt = 0
        self.next = ""   #下一步谁下子？next的取两种值："you"，"computer".

    def set_player_side(self, side):
        self.player_side = side
        self.after_selecting_side = True
        if side == BLACK_SIDE:
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
