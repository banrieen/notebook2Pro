""" 实现列表中重复元素最后一次出现的索引位置

>>> get_last_exist_dir([3,4,5,6,6,5,4,3,2,1,7,8,8,3], 5)
5
>>> get_last_exist_dir([3,4,5,6,6,5,4,3,2,1,7,8,8,3], 8)
12
>>> get_dir([3,4,5,6,6,5,4,3,2,1,7,8,8,3], 5)
5
>>> get_dir([3,4,5,6,6,5,4,3,2,1,7,8,8,3], 8)
12
 """

listA = [3,4,5,6,6,5,4,3,2,1,7,8,8,3]
target = 5
def get_last_exist_dir(listA, target):
    # 倒置 list，查找其第一次出现的位置
    return len(listA)- 1 - listA[::-1].index(target) 
    # for index, num in listA[::-1]:
    #     if num == target:
    #         return index

def get_dir(listA, target):
    # 二分法 和 快速排序想法尝试，并不能有效解决所有情况！
    rst = None
    length = len(listA)
    left = 0
    right = length - 1
    # listA = listA[::-1]
    while left < right:
        mid = left + (right-left) // 2
        # if target in listA[mid:]:
        if target >= listA[mid]:
            rst = mid
            left = mid + 1
        else:
            right = mid - 1
    return rst

if __name__ == "__main__":
    import doctest
    doctest.testmod()



