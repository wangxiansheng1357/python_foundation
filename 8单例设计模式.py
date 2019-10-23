#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/16


class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        print('开始分配空间')
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance
        else:
            return cls.instance

    def __init__(self):
        if not MusicPlayer.init_flag:
            MusicPlayer.init_flag = True
            print('进行初始化工作')
        else:
            pass


player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)
