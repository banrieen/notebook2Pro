#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''示例1: 最简单的函数,表示调用了两次'''
'''
def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func
 
def myfunc():
    print(" now myfunc() called.")
 
myfunc = deco(myfunc)
 
myfunc()


def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func
 
@deco
def myfunc():
    print(" now myfunc() called.")
 
myfunc()
'''

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(4)