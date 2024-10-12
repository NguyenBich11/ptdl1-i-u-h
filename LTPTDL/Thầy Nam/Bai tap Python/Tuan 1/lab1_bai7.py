# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:53:32 2021

@author: Asus
"""

n = int(input('Nhap so n : '))
fw = open('out.txt','w')

for i in range(n):
    if(i%2 ==0):
        fw.write(str(i)+'\r\n')     
fw.close()