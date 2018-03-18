#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division

class People:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Student(People):
    
    def __init__(self,name,age,id):
        People.__init__(self, name, age)
        self.id = id
        
    def getId(self):
        return self.id

class Xdict(dict):
    
    def __init__(self,new_dict):
        dict.__init__(self)
        self.new_dict = dict(new_dict)
        
    def getKeys(self,value):
        if value in self.new_dict.values():
            key_list = []
            for ikey in self.new_dict.keys():
                if value in self.new_dict[ikey]:
                    key_list.append(ikey)
            return key_list
        else:
            return None

        
class Vector:
    
    def __init__(self,x,y,z):
        self.vt = (x,y,z)
    
    def __add__(self,other):
        return self.format(map(sum,zip(self.vt,other.vt)))
        
    def sub(self,si):
        return si[0] - si[1]
    
    def __sub__(self,other):     
        return self.format(map(self.sub,zip(self.vt,other.vt)))
        
    def mul(self,si):
        return si[0] * si[1]
    
    def div(self,si):
        return si[0] / si[1]
    
    def __mul__(self,other):
        return self.format(map(self.mul,zip(self.vt,[other]*len(self.vt))))

    
    def __truediv__(self,other):
        return self.format(map(self.div,zip(self.vt,[other]*len(self.vt))))
    
    def format(self,mps):
        for i in range(len(mps)):
            mps[i] = float("{:.1f}".format(mps[i]))
        return str(tuple(mps))
    
    def __str__(self): 
        for i in range(len(self.vt)):
            self.vt[i] = float("{:.1f}".format(self.vt[i]))     
        return str(tuple(self.vt))
        

        
if __name__ == '__main__':
    alist = input().split()
    blist = input().split()
    n = float(input())
    
    a = Vector(float(alist[0]),float(alist[1]),float(alist[2]))    
    b = Vector(float(blist[0]),float(blist[1]),float(blist[2]))    
    
    print "{} {} {} {}".format(a+b,a-b,a*n,a/n)

 #==============================================================================
 #    name = input()
 #    age = int(input())
 #    id = input()
 #    
 #    S = Student(name,age,id)
 #    print("{} {} {}".format(S.getName(), S.getAge(),S.getId()))
 # 
 #    p = People(name,age)
 #    print("{} {}".format(p.getName(),p.getAge()))
 #    alist = list(input().split())
 #    blist = list(input().split())
 #    target = input()
 #    d = Xdict(zip(alist,blist))
 #    print(sorted(d.getKeys(target)))
 #==============================================================================
