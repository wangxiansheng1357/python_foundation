#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/21

import pygame
from random import random
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)  # 屏幕大小常量
FREQUENCY = 30  # 刷新频率（帧数）
CREAT_ENEMY_EVENT = pygame.USEREVENT  # 创建敌机常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1  # 英雄开枪事件


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵类"""
    def __init__(self, image_name, speed=1):

        # 调用父类的方法
        super().__init__()
        # 新建属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        super().__init__('./images/background.png', speed=5)
        if is_alt:
            self.rect.bottom = 0

    def update(self):
        super().update()
        # 判断图像是否移除屏幕，移除屏幕把图像设置到图像上方
        if self.rect.y > self.rect.height:
            self.rect.bottom = 0


class Enemy(GameSprite):
    """敌机精灵类"""
    def __init__(self):
        super().__init__('./images/enemy1.png', speed=3*random()+2)
        # 敌机的位置是随机的
        self.rect.x = (SCREEN_RECT.width - self.rect.width)*random()
        self.rect.bottom = 0

    def update(self):
        super().update()
        # 判断敌机是否从屏幕飞出，飞出即删除
        if self.rect.y > SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        super().__init__('./images/me1.png', speed=0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 生成子弹精灵
        bullet1 = Bullet()
        bullet2 = Bullet()
        bullet3 = Bullet()
        # 设置子弹初始位置
        bullet1.rect.centerx = self.rect.centerx
        bullet1.rect.bottom = self.rect.top
        bullet2.rect.centerx = self.rect.centerx
        bullet2.rect.y = bullet1.rect.y - 20
        bullet3.rect.centerx = self.rect.centerx
        bullet3.rect.y = bullet2.rect.y - 20
        # 将子弹添加到精灵组
        self.bullets.add(bullet1, bullet2, bullet3)


class Bullet(GameSprite):

    def __init__(self):
        super().__init__('./images/bullet1.png', speed=-5)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()


