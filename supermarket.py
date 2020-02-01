# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 03:18:54 2020

@author: user
"""

from collections import OrderedDict 
od=OrderedDict()
while True:
    str1=(input("Enter item with price :"))
    if inp == '':
        break
    temp=inp.split()
    price=temp[-1]
    item="".join(temp[:-1])
    od[item]=od.get(item,0)+int(price)
    for key,value in od.items():
        print(key,value)
        