#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/14

# 测试split返回结果
names = 'wang zi long'
name = names.split()
# print(name)
# 字符串调用split，返回列表[]


# 测试字典调用setdefault,返回值
mydict = {'name': 'wangzilong'}
setdefault_result = mydict.setdefault('name', 'luoyangfeng')
# print(setdefault_result)
# 如果有原本字典里的key，返回原本字典字典的值，否则返回设置的值


def story(**kwds):  # 测试format_map()函数用法
    return 'Once upon a time, there was a {job} called {name}.'.format_map(kwds)


story_dict = {'job': 'student', 'name': 'wangzilong'}
# print(story(**story_dict))
# print(story(job='student', name='wangzilong'))

# 测试全局变量
x = 1


def change_global():
    # global x
    globals()['x'] += 1
    # x += 1

change_global()
# print(x)

# 测试python除和整除
print(3/2)
print(3//2)