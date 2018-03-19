#!/usr/bin/env pyton
# -*- coding: utf-8 -*-

"""
斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到。
用计算机程序输出斐波那契數列的前 N 个数.
Date: 2017-09-21
Editor:Banrieen
"""

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for ni in fab(120):
    print (ni)

    
