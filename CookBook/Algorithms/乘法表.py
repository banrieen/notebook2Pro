#! /usr/bin/env python
# -*- coding: utf-8 -*-


def chengfabiao(n):
    """ 9 * 9 乘法表
        用逗号分隔每个打印项，如果print的最后没有逗号，每一次循环都会换行。 
    """
    if n <= 0:
        return 0
    for cs in range(1,n):
        print '\n'
        for cbs in range(1,cs + 1):
            print "%d x %d=%2d "%(cs,cbs,cs * cbs) , 