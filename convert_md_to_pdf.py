#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WangZilong  time:2019/10/17

import pypandoc
# import pdflatex

pypandoc.convert_file(source_file='file/敌机出场.md', to='html',
                      format='md', outputfile='pygame.html')
