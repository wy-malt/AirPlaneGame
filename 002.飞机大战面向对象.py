# coder:wy-malt
# 开发时间:2022/11/27 13:57
import random

import pygame
from pygame import *
import time

# 飞机类
class HeroPlane(object):
    def __init__(self, screen):
        # 创建一个图片 作为玩家飞机
        self.player = pygame.image.load("Images/hero1.png")
        self.x = 480 / 2 - 100 / 2
        self.y = 600
        # 飞机速度
        self.speed = 8
        # 记录当前窗口对象
        self.screen = screen
        # 装子弹的列表
        self.bullets = []

    def key_concrol(self):
        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.x += self.speed
        if key_pressed[K_SPACE]:
            # 按下空格发射子弹
            bullet = Bullet(self.screen,self.x,self.y)
            # 把子弹放到列表中
            self.bullets.append(bullet)

    def display(self):
        # 将飞机图片贴到窗口中
        self.screen.blit(self.player, (self.x,self.y))
        # 遍历所有子弹
        for bullet in self.bullets:
            # 让子弹飞 改变子弹的y坐标
            bullet.auto_move()
            # 子弹显示在窗口
            bullet.display()


# 敌方飞机
class EnemyPlane(object):
    def __init__(self, screen):
        # 创建一个图片 作为敌方飞机
        self.player = pygame.image.load("Images/enemy1.png")    # 57*43
        self.x = 0
        self.y = 0
        # 飞机速度
        self.speed = 8
        # 记录当前窗口对象
        self.screen = screen
        # 装子弹的列表
        self.bullets = []
        # 敌机移动方向
        self.direction = 'right'

    def display(self):
        # 将飞机图片贴到窗口中
        self.screen.blit(self.player, (self.x,self.y))
        # 遍历所有子弹
        for bullet in self.bullets:
            # 让子弹飞 改变子弹的y坐标
            bullet.auto_move()
            # 子弹显示在窗口
            bullet.display()

    def auto_move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        if self.x > 480-57:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def auto_fire(self):
        # 自动开火
        random_num = random.randint(1,10)
        if random_num == 8:
            bullet = EnemyBullet(self.screen, self.x, self.y)
            self.bullets.append(bullet)


# 子弹类
class Bullet(object):
    def __init__(self,screen,x,y):
        # 坐标
        self.x = x + 102/2 - 1
        self.y = y - 11
        # 图片
        self.image = pygame.image.load('Images/bullet1.png')
        # 窗口
        self.screen = screen
        # 速度
        self.speed = 10
    def display(self):
        # 显示子弹到窗口
        self.screen.blit(self.image,(self.x,self.y))

    def auto_move(self):
        # 让子弹飞 改变子弹y坐标
        self.y -= self.speed

# 敌方子弹类
class EnemyBullet(object):
    def __init__(self,screen,x,y):
        # 坐标
        self.x = x + 56/2 - 10/2
        self.y = y + 43
        # 图片
        self.image = pygame.image.load('Images/bullet2.png')
        # 窗口
        self.screen = screen
        # 速度
        self.speed = 8
    def display(self):
        # 显示子弹到窗口
        self.screen.blit(self.image,(self.x,self.y))

    def auto_move(self):
        # 让子弹飞 改变子弹y坐标
        self.y += self.speed


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()     # 背景音乐初始化
        pygame.mixer.music.load()



def main():
    # 1创建一个窗口
    screen = pygame.display.set_mode((480,752), 0, 32)
    # 2创建一个图片 作为背景
    background = pygame.image.load("Images/background.png")

    player = HeroPlane(screen)
    enemyPlane = EnemyPlane(screen)
    while True:
        # 3将背景图片贴到窗口中
        screen.blit(background, (0, 0))

        # 获取事件
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == QUIT:
                # 执行pygame退出
                pygame.quit()
                # pygame程序退出
                exit()

        # 执行飞机的按键监听
        player.key_concrol()
        # 显示飞机
        player.display()
        # 显示敌方飞机
        enemyPlane.display()
        # 敌方飞机自动移动
        enemyPlane.auto_move()
        # 敌方飞机自动开火
        enemyPlane.auto_fire()
        # 4显示窗口中的内容
        pygame.display.update()
        time.sleep(0.01)    # 单位为秒


if __name__ == '__main__':
    main()



































