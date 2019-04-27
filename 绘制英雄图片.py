import pygame
pygame.init()
screen = pygame.display.set_mode((412,627))
bg=pygame.image.load("./images/bg_01.jpg")
screen.blit(bg,(0,0))
#绘制英雄飞机
hero = pygame.image.load("./images/hero0.png")
screen.blit(hero,(150,450))
pygame.display.update()
i = 0
clock = pygame.time.Clock()
while True:
    clock.tick(60)
pygame.quit()
