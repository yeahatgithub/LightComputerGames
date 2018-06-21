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
    o_piece_img = None
    x_piece_img = None
    you_won_img = None
    computer_won_img = None
    duce_img = None

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
    def load_o_piece_img():
        if not GameResource.o_piece_img:
            GameResource.o_piece_img = pygame.image.load(GameResource.img_path + "o.png")
        return GameResource.o_piece_img

    @staticmethod
    def load_x_piece_img():
        if not GameResource.x_piece_img:
            GameResource.x_piece_img = pygame.image.load(GameResource.img_path + "x.png")
        return GameResource.x_piece_img


    @staticmethod
    def load_you_won_img():
        if not GameResource.you_won_img:
            GameResource.you_won_img = pygame.image.load(GameResource.img_path + "you_won.png").convert_alpha()
        return GameResource.you_won_img

    @staticmethod
    def load_computer_won_img():
        if not GameResource.computer_won_img:
            GameResource.computer_won_img = pygame.image.load(GameResource.img_path + "computer_won.png").convert_alpha()
        return GameResource.computer_won_img

    @staticmethod
    def load_duce_img():
        if not GameResource.duce_img:
            GameResource.duce_img = pygame.image.load(GameResource.img_path + "duce.png").convert_alpha()
        return GameResource.duce_img