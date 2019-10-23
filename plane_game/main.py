#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/21


import pygame
from plane_game.plane_sprites import *

frequency = 30
bg_width = 480
bg_height = 700
hero_speed_y = 3
hero_width = 102
hero_height = 126
hero_start_postion_x = 200
hero_start_postion_y = 500

pygame.init()

# ->创建游戏背景
screen = pygame.display.set_mode((bg_width, bg_height))
# ->加载图像
bg = pygame.image.load('./images/background.png')
hero = pygame.image.load('./images/me1.png')
# ->blit方法，将图片添加到屏幕上面
screen.blit(bg, (0, 0))
screen.blit(hero, (hero_start_postion_x, hero_start_postion_y))
# ->更新显示
pygame.display.update()
# ->创建游戏时钟对象
clock = pygame.time.Clock()

# 1创建英雄初始位置
hero_rect = pygame.Rect(hero_start_postion_x, hero_start_postion_y, hero_width, bg_height)

# 创建敌机精灵
enemy = GameSprite('./images/enemy1.png', speed=2)
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy)

quit_flag = False
# ->游戏循环
while True:
    clock.tick(frequency)  # 指定循环体内部代码循环频率
    # 对游戏屏幕进行更新
    pygame.display.update()

    # 游戏监听事件
    for event in pygame.event.get():
        # print(type(event))
        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            quit_flag = True
            break

    if quit_flag:
        break

    if hero_rect.bottom < 0:
        hero_rect.y = bg_height
    # 英雄的位置每次减1
    hero_rect.y -= hero_speed_y
    # 绘制英雄图片到屏幕上
    screen.blit(bg, (0, 0))
    screen.blit(hero, (hero_rect.x, hero_rect.y))

    # 精灵组调用两个方法 update和draw
    # update方法让精灵组中所有精灵更新位置
    enemy_group.update()
    # draw方法，将精灵组中所有精灵画到屏幕上
    enemy_group.draw(screen)



pygame.quit()