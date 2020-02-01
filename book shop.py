# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:29:20 2020

@author: user
"""
orders=[["34587","learning python,Mark Lutz",4,40.95],
["98762","programming python,Mark Lutz",5,56.80],
["77226","head first python,Paul Barry", 3,32.95],
["88112","einfuhrung in python3,Bernd klien",3,24.99]]
minorder=100

invoicetotal=list(map(lambda x: x if x[1]>= minorder else (x[0], x[1] + 10), 
            map(lambda x: (x[0],round(x[2] * x[3],2)), orders)))
print(invoicetotal)

