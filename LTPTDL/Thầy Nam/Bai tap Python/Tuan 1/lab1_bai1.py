# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = float(input('Nhap a : '))
b = float(input('Nhap b : '))

if a > 0 or a < 0:
    x = -b/a
    print('PT co nghiem la : ', x)
else:
    if b == 0:
        print('PT co vo so nghiem')
    else:
        print('PT vo nghiem')
            