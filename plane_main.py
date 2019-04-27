import pygame
from  plane_sprites import *
class PlaneGame(object):
    '''飞机大战主游戏'''
    def __init__(self):
        print("游戏初始化")
        #1. 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        #2. 创建游戏的时钟
        #3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)
    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)


        self.back_group = pygame.sprite.Group(bg1,bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
    def start_game(self):
        print("游戏开始")
        while True:
            #1. 设置刷新镇率
            self.clock.tick(FRAME_PRE_SEC)
            #2. 事件监听
            self.__event_handler()
            #3. 碰撞检测
            self.__check_collide()
            #4.g更新精灵
            self.__update_sprites()
            #5. 更新显示
            pygame.display.update()
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场。。。")
                #创建敌机
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                print("发射子弹...")
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
            #使用键盘提供的方法获取键盘按键--按键元组

            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0
    def __check_collide(self):
        #子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        # 2.敌机吹英雄
        enemys =pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemys) >0:
            self.hero.kill()
            PlaneGame.__game_over()
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()
if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
