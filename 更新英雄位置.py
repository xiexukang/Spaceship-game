import pygame
import  sys
from plane_sprites import *
pygame.init()
screen = pygame.display.set_mode((412,627))
bg=pygame.image.load("./images/bg_01.jpg")
screen.blit(bg,(0,0))
#绘制英雄飞机
hero = pygame.image.load("./images/hero0.png")
screen.blit(hero,(150,450))
pygame.display.update()
clock = pygame.time.Clock()
hero_rect = pygame.Rect(150,250,140,178)
#创建敌机的境
enemy = GameSprite("./images/a2-1.png")
enemy2 = GameSprite("./images/a2-2.png", 2)
#创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy,enemy2)
while True:
    clock.tick(60)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           print("游戏推出...")
           pygame.quit()
           exit()#直接终止程序
    hero_rect.y -=1
    if hero_rect.y <= 0:
        hero_rect.y=700
    else:
        pass


    #要想不留下残影，可以重新绘制背景图片
    screen.blit(bg,(0,0))
    screen.blit(hero, hero_rect)

    #让精灵组调用两个方法
    #update
    enemy_group.update()

    #draw
    enemy_group.draw(screen)
    pygame.display.update()
pygame.quit()
