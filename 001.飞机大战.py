# coder:wy-malt
# 开发时间:2022/11/27 13:57

import pygame
from pygame import *
import time

def main():
    # 1创建一个窗口
    screen = pygame.display.set_mode((480,752), 0, 32)
    # 2创建一个图片 作为背景
    background = pygame.image.load("Images/background.png")
    # 创建一个图片 作为玩家飞机
    player = pygame.image.load("Images/hero1.png")

    x = 480/2-100/2
    y = 600
    speed = 8
    while True:
        # 3将背景图片贴到窗口中
        screen.blit(background, (0, 0))
        # 将飞机图片贴到窗口中
        screen.blit(player, (x, y))
        # 获取事件
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == QUIT:
                # 执行pygame退出
                pygame.quit()
                # pygame程序退出
                exit()
            '''elif event.type == KEYDOWN:
                # 检查按键是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('左')
                # 检查按键是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('右')
                # 判断按键是否是空格
                elif event.key == K_SPACE:
                    print('空格')'''
        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            print('上')
            y -= speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            print('下')
            y += speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print('左')
            x -= speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            print('右')
            x += speed
        if key_pressed[K_SPACE]:
            print('空格')
        # 4显示窗口中的内容
        pygame.display.update()
        time.sleep(0.01)    # 单位为秒


if __name__ == '__main__':
    main()



































