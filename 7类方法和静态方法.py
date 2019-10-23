#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/16


class Game(object):
    """植物大战僵尸游戏"""
    top_score = 0

    def __init__(self, game_player_name):
        self.game_player_name = game_player_name

    @staticmethod
    def show_help():
        print('不要让僵尸进入大门')

    @classmethod
    def show_top_score(cls):
        print('最高分是%d' % Game.top_score)

    def play(self):
        print('%s玩家开始游戏了' % self.game_player_name)


game = Game('wangzilong')
Game.show_help()
Game.show_top_score()
game.play()