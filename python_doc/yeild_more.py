#!/usr/bin/env python
# -*- coding: utf-8 -*-

for x , y in [ (1,'a') , (2,'b') , (3,'c') ] :
    print ( x , y )

def first_generator():
    for iG in range(30):
        yield iG

first_generator()

'''
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b
for x in fibon(1000000):
    print (x )
'''
names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
dict1= dict(zip(names,ages))

print(dict1)
