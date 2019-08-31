""" 快速归并排序 """

def merge_sort_fast(listA):
    start = []
    end = []
    while len(listA) > 1:
        a = min(listA)
        b = max(listA)
        start.append(a)
        end.append(b)
        listA.remove(a)
        listA.remove(b)
    if listA:
        start.append(listA[0])
    end.reverse()
    return start + end

if __name__ == "__main__":
    listA = [0, 5, 3, 2, 2]
    sortedList = merge_sort_fast(listA)
    print(sortedList)
