""" 递归方法处理快速排序 """

def quick_sort(listA):
    length = len(listA)
    if length <= 1:
        return listA
    else:
        pivot = listA[0]
        # import random
        # pivot = random.choice(listA)
        greater = [element for element in listA[1:] if element > pivot]
        lesser = [element for element in listA[1:] if element <= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    listA = [0, 5, 3, 2, 2]
    sortedList = quick_sort(listA)
    print(sortedList)

