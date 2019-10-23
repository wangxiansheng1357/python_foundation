#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/21
import pygame
from plane_game.plane_sprites import *


class Plane(object):
    """游戏的主程序"""

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__creat_sprites()

        # 设立定时器事件
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __creat_sprites(self):
        bg1 = Background()
        bg1.rect.y = 0
        bg2 = Background(is_alt=True)
        bg2.rect.bottom = 0
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄和英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        while True:
            # 设置刷新帧率
            self.clock.tick(FREQUENCY)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Plane.__gameover()
            elif event.type == CREAT_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key ==pygame.K_RIGHT:
            #     print('向右移动')

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # TODO:检查碰撞
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            print(enemies)
            self.hero.kill()
            self.__gameover()

    def __update_sprites(self):
        # TODO:更新精灵组
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __gameover():
        print('游戏结束')
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = Plane()
    game.start_game()
