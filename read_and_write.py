#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/16

file_read = open('ReadMe')
file_write = open('ReadMe 复制', 'w')

while True:
    text_line = file_read.readline()
    if not text_line:
        break
    file_write.write(text_line)

file_read.close()
file_write.close()

