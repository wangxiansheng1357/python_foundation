#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/21

import random
import pygame

SCREEN_SIZE_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SECOND = 30
ENEMY_CREAT_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵类"""
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__('./images/background.png', speed=3)
        # 判断是否是第二张图片
        if is_alt:
            self.rect.bottom = 0

    def update(self):
        super().update()
        # 判断是否移出屏幕
        if self.rect.y > SCREEN_SIZE_RECT.height:
            self.rect.bottom = 0


class Enemy(GameSprite):

    def __init__(self):
        super().__init__('./images/enemy1.png', speed=3*random.random()+2)
        self.rect.x = (SCREEN_SIZE_RECT.width - self.rect.width) * random.random()
        self.rect.bottom = 0

    def update(self):
        super().update()
        # 判断敌机是否飞出屏幕
        if self.rect.y > SCREEN_SIZE_RECT.height:
            self.kill()


class Hero(GameSprite):

    def __init__(self):
        super().__init__('./images/me1.png', speed=0)
        self.rect.centerx = SCREEN_SIZE_RECT.centerx
        self.rect.bottom = SCREEN_SIZE_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平移动
        self.rect.x += self.speed
        # 对超出边界进行处理
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > SCREEN_SIZE_RECT.right:
            self.rect.right = SCREEN_SIZE_RECT.right

    def fire(self):
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.top - i*20
            self.bullets.add(bullet)


class Bullet(GameSprite):

    def __init__(self):
        super().__init__('./images/bullet1.png', speed=-5)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

