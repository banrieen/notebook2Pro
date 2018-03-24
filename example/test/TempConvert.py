#! /usr/bin/python 
# -*- coding: UTF-8 -*-

'''
Created on 2018年3月15日

@author: lizhen
'''



TempStr = input("Please input the temp: ")

if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) -32) / 1.8
    print("The converted Temp is: {:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("The Convert F is: {:.2f}F".format(F))
else:
    print("Error Format String !")
 
#圆周率
    
r = 25
area = 3.1415926 * r * r
print("{:.2f}m2".format(area))

#同心圆
import turtle
turtle.pensize(2)
turtle.circle(10)
turtle.circle(40)
turtle.circle(80)

#8角星

from turtle import *
color('red','green')
begin_fill()
for i in range(8):
    fd(200)
    rt(144)
    
end_fill()