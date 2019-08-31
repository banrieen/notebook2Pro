# usr/bion/env python3
# -*- coding: utf-8 -*-

def add():
    # print("Please input the add numbers, split by backspace' ':  ",end='')
    inStr = input()
    a, b = inStr.split(' ')
    rst = int(a) + int(b)
    # print("The sum is: {}".format(rst))
    print(rst)

def right_number(num):
    num = int(num)
    if num <= 2000 and num >= -2000:
        return num
    else:
        return None

def over_space():
    s1 = input()
    s1 = [num for num in s1.split(' ') if right_number(num)]
    if None in s1:
        return None
    s1_x1, s1_y1, s1_x2, s1_y2 = s1
    s2 = input()
    s2 = [right_number(num) for num in s2.split(' ') ]
    if None in s2:
        return None
    s2_x1, s2_y1, s2_x2, s2_y2 = s2
    col = min(int(s1_x2),int(s2_x2)) - max(int(s1_x1),int(s2_x1))
    row = min(int(s1_y2),int(s2_y2)) - max(int(s1_y1),int(s2_y1))
    overSpace = col * row
    print(overSpace)

import copy
from collections import defaultdict
def helloworld(taskStr="helloworld"):
    s = input()
    s = list(s) 
    if len(taskStr) > len(s):
        return False
    s1 = ''.join([char for char in s if char in taskStr])
    tempIndex = 0
    for char in taskStr:
        if char in s1:
            sIndex = s1.index(char)
            if tempIndex <= sIndex:
                tempIndex = sIndex
            else:
                print("false")
                return False
    print("true")
    return True

    # sd = defaultdict(list)
    # td = defaultdict(list)
    # for k,va in [(v,i) for i,v in enumerate(s1)]:
    #     sd[k].append(va)
    # for k,va in [(v,i) for i,v in enumerate(taskStr)]:
    #     td[k].append(va)
    # sKey = sd.keys()
    # tKey = td.keys()
    # if len(sKey) < len(tKey):
    #     return False
    # for key in tKey:
    #     if key not in sKey:
    #         return False
    #     if tKey[key] == sKey[key]:

    # commonItems = {k: sd[k] for k in sd if k in td and td[k] == sd[k]}

    # commmonStr = ''.join(commonItems.values())
    # commonIndex = commonItems.keys()
    # if commmonStr != taskStr:
    #     print("false")
    #     return False
    # if commonIndex != sorted(commonIndex,reversed=False):
    #     print("false")
    #     return False
    # print("true")
    # return True

def huiwen(s,i,step,rst):
    if i > len(s) - 1:
        return rst
    if s[i] != s[i+step] and s[i+step] == "" and i+step < len(s) - 1:
        step += 1
        return huiwen(s,i,step,rst)
    elif s[i] == s[i+step] and i+step < len(s) - 1:
        rst = s[i] + '+'*step + s[i+step]
        i += step
        step = 1
        return huiwen(s,i,step,rst)
    elif s[i] != s[i+step] and s[i+step] != "" and i+step < len(s) - 1:
        i += step
        step = 1
        return huiwen(s,i,step,rst)
    else:
        rst = s[i] + '_'*step + s[i+step]
        return rst

def asser_huiwen(s):
    s = s.strip('_')
    length = len(s)
    s = s.split("_")
    # s.remove("")
    rst = ""
    huiwen(s,i=0,step=1,rst=rst)
    print(rst)


if __name__ == "__main__":
    # helloworld()
    print(asser_huiwen("__aa_ab__ab"))
""" 
** E - 不连续子串判断

    实现⼀个函数，判断helloworld是否是给定字符串的不连续子串

即helloworld的每个字母均在给定字符串中出现，并且需要保持先后顺序但可以允许不相邻

如helllllllo wwwwwwworld 符合条件，如红色的标记所示。

但helolllllworld不符合条件。


## D - _与+字符变换 
    给定一个只包含小写字母和‘_’的字符串，输出如下变换后的结果：

    字符串被连续的'_'分成了若干子串，如果一段连续的'_'两侧是相同的子串，则将这段'_'的每个字符变为'+'


## F - 观察3D空间中的线段是否相交 
    3D空间里，给定两条长度非零的线段S1、S2（S1与S2不共面），以及一个点O（不在S1、S2上）。

    判断以O点作为观测点观察，S1和S2是否相交（即S1和S2至少要有一个公共点）。 """