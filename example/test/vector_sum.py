#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division
       
class Vector:
    
    def __init__(self,x,y,z):
        self.vt = (x,y,z)
    
    def __add__(self,other):
        self.vt = map(sum,zip(self.vt,other.vt))
        return self.__str__()
        
    def sub(self,si):
        return si[0] - si[1]
    
    def __sub__(self,other):     
        self.vt = map(self.sub,zip(self.vt,other.vt))
        return self.__str__()
        
    def mul(self,si):
        return si[0] * si[1]
    
    def div(self,si):
        return si[0] / si[1]
    
    def __mul__(self,other):
        self.vt = map(self.mul,zip(self.vt,[other]*len(list(self.vt))))
        return self.__str__()
    
    def __truediv__(self,other):
        self.vt = map(self.div,zip(self.vt,[other]*len(list(self.vt))))
        return self.__str__()
    
    def __str__(self):
        self.vt = list(self.vt)
        for i in range(len(self.vt)):
            self.vt[i] = float("{:.1f}".format(self.vt[i]))     
        return str(tuple(self.vt))
        

        
if __name__ == '__main__':
    alist = input().split()
    blist = input().split()
    n = float(input())
    a = Vector(float((alist[0])),float(alist[1]),float(alist[2]))
    b = Vector(float(blist[0]),float(blist[1]),float(blist[2]))    
    
    print ("{} {} {} {}".format(a+b,a-b,a*n,a/n))

 
