""" 二分查找 """

def binary_search(listA, target):
    left = 0
    right = len(listA) - 1 
    while left <= right:
        midpoint = (left + right) // 2
        current_item = listA[midpoint]
        # if listA[left] == target:
        #     return left
        # elif listA[right] == target:
        #     return right
        if current_item == target:
            return midpoint
        else:
            if target < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return None


if __name__ == "__main__":
    listA = [1,4,8,9,12,45,78]
    target = 12
    rst = binary_search(listA, target)
    if rst:
        print("OK: ",rst)
    else:
        print("Not found !")