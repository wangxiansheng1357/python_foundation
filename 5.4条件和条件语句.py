#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/9

from math import sqrt


# assert语句可以检查参数是否满足要求
# age = int(input('please enter a number between 1 and 100:'))
# assert 0 < age < 100, 'The age must be realistic'


# zip语句可以将两个序列连接起来
# names = ['anne', 'beth', 'george', 'damon']
# ages = [12, 45, 32, 102]
# for name, age in zip(names, ages):
#     print(name, 'is', age, 'years old.')
#
# names2 = ('zhangsan', 'lisi', 'wangwu')
# ages2 = (1, 2, 3)
# for name, age in zip(names2, ages2):
#     print(name, 'is', age, 'years old.')

# enumerate函数
sentences = ['hello', 'ello', 'world']
# for string in sentences:
#     if 'llo' in string:
#         index = sentences.index(string)
#         sentences[index] = 'wangzilong'
# print(sentences)

# for index, string in enumerate(sentences):
#     if 'llo' in string:
#         sentences[index] = 'wang'
# print(sentences)

# sorted和reversed函数
# string1 = 'hello,world'
# string2 = 'DabcFg'
# result1 = ''.join(sorted(string1))
# result2 = list(reversed(string1))
# result3 = ''.join(sorted(string2, key=str.lower))
# print('sorted处理的结果是', result1)
# print('reversed处理的结果是', result2)
# print('sorted加上str.lower处理的结果是', result3)

for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it")
