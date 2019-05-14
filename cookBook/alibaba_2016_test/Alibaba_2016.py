#! /usr/bin/env python
# -*- coding: utf-8 -*-

            
"""
1.1 对于数列a = [1,2,3,4,5] 
"""
a = [1,2,3,4,5] 
a[::2] = [1,3,5] a[::-2] = [5,3,1]


"""
1.2. 一行代码实现对列表a的偶数位的元素加3求和
"""
sum([x for x in a if a.index(x) % 2 ==0 and x != 1])


"""
1.3. 将列表a的元素顺序打乱，再对a进行排序得到列表b，然后把a和b按元素顺序构造一个字典d。
"""
import math

math.shuffle(a)
#[1, 3, 2, 5, 4]
b = sorted(a,reverse=True)
#[5, 4, 3, 2, 1]
d = dict(zip(a,b))
#{1: 5, 2: 3, 3: 4, 4: 1, 5: 2}

"""
2. 用python实现统计一篇英文文章内每个单词的出现频率，并返回出现频率最高的前10个单词及其出现次数，并解答以下问题？（标点符号可忽略）
   英文实例文件使用test_example/How the iPhone rewired Apple
"""