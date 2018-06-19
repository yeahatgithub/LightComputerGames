# @Time    : 2018/6/19 10:04
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame

class GameResource():
    img_path = "images/"
    game_title_img = None
    your_turn_img = None
    computer_trun_img = None
    you_o_vs_computer_x_img = None
    you_x_vs_computer_o_img = None

    def __init__(self):
        pass

    @staticmethod
    def load_game_title_img():
        if not GameResource.game_title_img:
            GameResource.game_title_img = pygame.image.load(GameResource.img_path + "san-lian-qi.png").convert_alpha()
        return GameResource.game_title_img

    @staticmethod
    def load_you_o_vs_computer_x_img():
        if not GameResource.you_o_vs_computer_x_img:
            GameResource.you_o_vs_computer_x_img = pygame.image.load(GameResource.img_path + "you_o_vs_computer_x.png").convert_alpha()
        return GameResource.you_o_vs_computer_x_img


    @staticmethod
    def load_you_x_vs_computer_o_img():
        if not GameResource.you_x_vs_computer_o_img:
            GameResource.you_x_vs_computer_o_img = pygame.image.load(GameResource.img_path + "you_x_vs_computer_o.png").convert_alpha()
        return GameResource.you_x_vs_computer_o_img

    @staticmethod
    def load_your_turn_img():
        if not GameResource.your_turn_img:
            GameResource.your_turn_img = pygame.image.load(GameResource.img_path + "your_turn.png").convert_alpha()
        return GameResource.your_turn_img

    @staticmethod
    def load_computer_turn_img():
        if not GameResource.computer_trun_img:
            GameResource.computer_trun_img = pygame.image.load(GameResource.img_path + "computer_turn.png").convert_alpha()
        return GameResource.computer_trun_img