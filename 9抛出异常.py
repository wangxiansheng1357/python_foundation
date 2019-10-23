#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/16


def input_password():
    """用户输入密码"""
    password = input('请输入密码：')
    if len(password) < 8:
        ex = Exception(('密码长度不够', 'mimachangdubugou'))
        raise ex
    return password


try:
    mypassword = input_password()
except Exception as result:
    print('未知错误 %s' % result)
