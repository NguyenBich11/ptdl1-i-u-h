# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:30:37 2021

@author: H4-HTTT
"""

def isPrime(n):
    if(n<0):
        return False
    elif(n==0):
        return False
    elif(n==1):
        return False
    elif(n==2):
        return True
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
        return True
    