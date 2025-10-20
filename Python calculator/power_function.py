# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 01:53:41 2025

@author: MALIK COMPUTERS
"""

def power(num, power):
    i=1
    temp=num
    while i<power:
        temp*=num
        i+=1
    print(f"{num} ^ {power} is {temp}")    
    return 0
n=float(input("Enter a number: "))
p=int(input("Enter power: "))
power(n,p) 
    