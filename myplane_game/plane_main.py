#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/21

from myplane_game.game_sprites import *


class PlaneGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE_RECT.size)
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(ENEMY_CREAT_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        self.__creat_sprites()

    def __creat_sprites(self):

        # 创建背景精灵组
        bg1 = Background()
        bg2 = Background(is_alt=True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌人精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        while True:
            # 设置频率
            self.clock.tick(FRAME_PER_SECOND)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == ENEMY_CREAT_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __myupdate(self, mysprit):
        mysprit.update()
        mysprit.draw(self.screen)

    def __update_sprites(self):
        for sprite in [self.bg_group, self.enemy_group, self.hero_group, self.hero.bullets]:
            self.__myupdate(sprite)

    @staticmethod
    def __game_over():
        print('游戏结束')
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()