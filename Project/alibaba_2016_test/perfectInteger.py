#!/usr/bin/env python
# -*- coding:utf-8 -*-

    def divisors(num):
        if num < 6:
            return 0
        divs = []
        for x in range(num//2,0,-1):
            if num % x == 0:
               divs.append(x) 
            else:
                continue
        if len(divs):
            return divs, num
        
    def checkDivisors(divs,num):
        sum = 0
        for di in divs:
            sum += di
        if sum == num:
            return Num
    
    def countWanmeishu(nums):
        """
        完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
        它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
        如果一个数恰好等于它的因子之和，则称该数为“完全数”。
        第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。
        求某个范围内的完全数，先获取该范围内的所有数的约数（整除数），在验证约数之和是否等于自身。
        调用divisors(num) 获取每个数的约数
        调用checkDivisors(divs,num) 验证约数之和是否等于自身
        """
        counts = []
        for ni in range(nums):
            divs = divisors(ni)       
            if divs and checkDivisors(divs[0],divs[1]):
                print "完美数： {}, 因子：{} \n".format(divs[1],divs[0])
                counts.append((divs))
        return counts   