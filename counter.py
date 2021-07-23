# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:30:19 2021

@author: Vinícius Leitão
"""

file = open("counter.py", "r")
text = file.read()


uppercase = 0
lowcase = 0
numbers = 0
whitespaces = 0
wraps = 0

for char in text:
    
    if char == chr(32):
        whitespaces+= 1
    elif char == chr(10):
        wraps += 1
    elif 65 <= ord(char) <= 90:
        uppercase += 1
    elif 97 <= ord(char) <= 122:
        lowcase += 1
    elif 48 <= ord(char) <= 57:
        numbers += 1

print("The file has: Whitespaces: {0}, Wraps: {1}, Uppercases: {2}, Lowcases: {3} and Numbers: {4}" .format(whitespaces, wraps, uppercase, lowcase, numbers))

file.close()