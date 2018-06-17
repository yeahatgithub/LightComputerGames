# @Time    : 2018/6/17 10:56
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame
WHITE = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("三连棋")
    is_playing = True

    while is_playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False

        screen.fill(WHITE)
        pygame.display.update()


if __name__ == "__main__":
    main()

