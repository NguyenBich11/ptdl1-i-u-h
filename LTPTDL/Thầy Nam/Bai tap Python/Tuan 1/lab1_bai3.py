# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:17:56 2021

@author: Asus
"""

kwh = int(input('Nhap so kwh : '))

if kwh <= 100:
    tongtien = kwh*2000
    print('Tong tien la : ', tongtien)
else:
    n = kwh - 100
    print('n = ', n)
    if n == 1:
        tongtien = 100*2000 + (2000+100)
        print('Tong tien la : ', tongtien)
    else:
        x = 2000+100*n
        y = n-1        
        tongtien = 100*2000 + (2000+100) + x
        print('Tong tien la : ', tongtien)
    
