# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:28:50 2020

@author: user
"""
for number in range(1,51): 
    if (number % 15 == 0):
        print("FizzBuzz")
        continue
    elif (number % 3 == 0):
        print("Fizz")
        continue
    elif (number % 5 == 0):
        print("Buzz")
        continue
    print(number) 


    
