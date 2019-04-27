import random
import pygame
# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,500,700)
FRAME_PRE_SEC = 60
#敌机定时器的常量
CREATE_ENEMY_EVENT=pygame.USEREVENT
#英雄发射制单事件
HERO_FIRE_EVENT = pygame.USEREVENT+1
class GameSprite(pygame.sprite.Sprite):
    '''飞机大战游戏竟能'''
    def __init__(self, image_name, speed =1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y +=self.speed
class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self,is_alt=False):
        #1. 带哦用父类方法实现精灵创建
        super().__init__("./images/img_bg_level_1.jpg")
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        #1. 调用父类方法实现
        super().update()
        #2. 判断是否驶出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
class Enemy(GameSprite):
    #敌机精灵类
    def __init__(self):
        #1.调用父类方法，创建敌机精灵
        number = random.randint(1,3)
        super().__init__("./images/a2-%d.png" % (number))
        #2.指定敌机速度
        max_x = SCREEN_RECT.width - self.rect.width
        self.speed = random.randint(1,2)
        self.rect.x = random.randint(0,max_x)
        self.rect.bottom = 0
        #self.rect.y = random.randint(-2*self.rect.height,-self.rect.height)
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            #print("飞出屏幕，需要删除。。。")
            self.kill()
    def __del__(self):
       # print("敌机挂了 %s" % self.rect)
         pass
class Hero(GameSprite):
    def __init__(self):
        #1. 调用父类方法，设置初始
        super().__init__("./images/hero.png",0)
        self.rect.centerx =  SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom
        #创建精灵的精灵组
        self.bullets = pygame.sprite.Group()
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >=SCREEN_RECT.width- self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
            print(self.rect.x,SCREEN_RECT.width)
        if self.rect.x <=0:
            self.rect.x = 0
    def fire(self):
        print("发射。。。")
        #1. 创建子弹

        bullet = Bullet()
        #2. 设置精灵的位置
        bullet.rect.bottom = self.rect.y -20
        bullet.rect.centerx = self.rect.centerx
        #3.
        self.bullets.add(bullet)
class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet.png",-2)
        pass
    def update(self):
        #调用父类方法，让子弹言垂直方向飞行
        super().update()
        if self.rect.bottom <0 :
            self.kill()

    def __del__(self):
        print("子弹被销毁...")
