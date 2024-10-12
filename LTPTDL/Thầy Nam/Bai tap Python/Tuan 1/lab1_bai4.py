# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:33:07 2021

@author: H4-HTTT
"""

import thuvienham as lib
x = int(input('Nhap so tu nhien : '))

if(lib.isPrime(x) == True):
    print('x la so nguyen to')
else:
    print('x khong la so nguyen to')    