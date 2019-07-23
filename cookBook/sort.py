# usr/bin/env python3 



def bubble_sort(arry):
    # 冒泡排序，依次比较大小，交换位置
    i,j = 0,0
    length = len(arry)
    for i in range(length):
        for j in range(i+1,length):
            if arry[j] < arry[i]:
                arry[j], arry[i] = arry[i], arry[j]
            else:
                continue
    return arry


def selection_sort(arry):
    # 选择排序，每次都把最小的找出放在左边
    length = len(arry)
    minFlag = 0
    for i in range(0, length):
        print(i)
        minFlag = i
        for j in range(i+1,length):
            if arry[j] < arry[minFlag]:
                minFlag = j
        if i != minFlag:
            arry[i], arry[minFlag] = arry[minFlag], arry[i]
    return arry

def insertion_sort(arry):
    # 插入排序，选取一个目标数字，从右开始比较，放在最小的位置上
    length = len(arry)
    for i in range(1,length):
        preIndex = i - 1
        while preIndex > 0 and arry[preIndex+1] < arry[preIndex]:
            arry[preIndex+1], arry[preIndex] = arry[preIndex], arry[preIndex+1]
            preIndex -= 1
    return arry

def merge_sort_index(array,low=0,high=0):
    # 归并排序使用数组下标
    if low < high:
        mid = (low+high-1)//2
        merge_sort_index(array,low,mid)
        merge_sort_index(array,mid+1,high)
        merge_arry(array,low,mid,high)

def merge_arry(array,low,mid,high):
    mergeList = []
    left = low
    right = mid + 1
    while left <= mid and right <= high-1:
        if array[left] <= array[right] :
            mergeList.append(array[left])
            left += 1
        else:
            mergeList.append(array[right])
            right += 1
    while left <= mid:
        mergeList.append(array[left])
        left += 1
    while right <= high-1:
        mergeList.append(array[right])
        right += 1
    for i in range(len(mergeList)):
        array[low+i] = mergeList[i]

def merge_sort(lists):
    # 归并排序使用数组切片
    if len(lists) <= 1:
        return lists
    num = int(len(lists)/2)
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


def merge(left, right):
    ri, le = 0, 0
    result = []
    while le < len(left) and ri < len(right):
        if left[le] < right[ri]:
            result.append(left[le])
            le += 1
        else:
            result.append(right[ri])
            ri += 1
    result += left[le:]   # 剩下的左边的
    result += right[ri:]  # 剩下的右边的
    return result


import random
def quick_sort(array):
    length = len(array)
    if length <= 1:
        return array
    # pivot = array[length // 2]
    pivot = array[random.randint(0,length)]
    lesser = [element for element in array if element < pivot]
    greater = [element for element in array if element > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

# data = list(range(10))  # 产生一个有序列表
# random.shuffle(data)  # 调用shuffle函数打乱顺序

if __name__ == "__main__":
    import copy
    import time
    array = [1,4,8,7,454,23,45,564,99,80]
    # print("bubble_sort: {}".format(bubble_sort(arry)))
    # print("selection_sort: {}".format(selection_sort(arry)))
    # rst = insertion_sort(arry)
    # print("insertion_sort: {}".format(rst))
    # merge_sort_index(array,low=0,high=len(array))
    # array = merge_sort(array)
    
    array = quick_sort(array)
    print(array)