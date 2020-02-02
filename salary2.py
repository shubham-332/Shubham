# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 08:52:29 2020

@author: user
"""
salaries=['$876,001','$543,903','$2453,896']
salaries2=[]
for salary in salaries:
    salaries2.append(int("".join(salary[1:].split(','))))
print(salaries2)
    

