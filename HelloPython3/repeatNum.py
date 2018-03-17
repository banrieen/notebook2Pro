#!/usr/bin/env python
# -*- conding:utf-8 -*-
 

"""
从一个数列中，找出重复的元素，按照其重复次数排序，返回重复次数最多的前N元素
例如：数列listN = [1,1,1,1,1,5,5,5,5,5,6,66,7,7,7,7,7,7,7,8,8,8,8,9,9,9]
重复结果rpt = {'1':5,'5':5,'6':1,'66':1,'7':7,'8':3,'9':3}
获取重复次数最多的前N=3个数字的元素 [7,1,5,]
Date：2017-09-20
Editor：banrieen
##Doctest cases：
>>> repeatNum().find_Nmemeber([1,1,1,1,1,5,5,5,5,5,6,66,7,7,7,7,7,7,7,8,8,8,8,9,9,9],4)
{7: 7, 1: 5, 5: 5, 8: 4, 9: 5}
"""

import os,sys
import random
import time

class repeatNum:
    def __init__(self):
        #If need random list to test,this is very usefull to creat the random list with repeater memebers
        self.seeds = int(time.strftime("%s",time.gmtime())) % 1000
        if int(self.seeds):
            self.listM = [x for y in range(random.randrange(self.seeds//2)) for x in range(random.randrange(self.seeds//3),self.seeds) ]
            
    def check_repeatCount(self,listN):
        if not listN:
            listN = self.listM
        repeatCount = {}
        listLength = len(listN)
        listM = set(listN)
        for member in listM:
            count = 0
            for ri in range(listLength):
                if listN[ri] == member:
                    count = count + 1
            repeatCount[member] = count
        return repeatCount

    def sortedList_byRepeatCount(self,repeatCount):
        if repeatCount:
            sortByValue = sorted(repeatCount.items(),key=lambda di:di[1],reverse=True)
            return sortByValue
        
    def find_Nmemeber(self,listN,N):
        valueList = []
        resultDict = {}
        sortByValue = self.sortedList_byRepeatCount(self.check_repeatCount(listN))
        if not sortByValue:
            return None
        for (keys,values) in sortByValue:
            valueList.append(values)
            if valueList.index(values) <= N:
                resultDict[keys] = values
        return resultDict

if __name__ == "__main__":
    import doctest
    doctest.testmod()


