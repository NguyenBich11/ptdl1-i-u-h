# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:49:38 2021

@author: Asus
"""

fr = open('in.txt')
flines = fr.readlines()

for line in flines:
    print(line)
fr.close()