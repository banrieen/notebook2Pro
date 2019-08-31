""" 递增三元组子序列
题目描述

给出一个无序的整数序列，返回是否存在递增的三元组子序列。

如果存在 i, j, k 使得 arr[i]<arr[j]<arr[k] and 0<i<j<k<n-1，即返回true；如果不存在则返回false。
请给出一个O(N)时间复杂度以及O(1)额外空间的算法。
Example 1： [1, 2, 3, 4, 5]
返回true。
Example 2: [5, 4, 3, 2, 1]
返回false。


分析解答

读者不难想到穷举的方法，先穷举第一个数，再穷举找到第二个数（比第一个大），再穷举第三个数（比第二个数大），得到答案。但这样穷举过于低效，与要求的O(N)相距甚远。还有一种穷举方法是先预处理得到一个数组p，p[i]表示是否存在这样的j, j>i and arr[j]>arr[i]。这种方法符合时间复杂度的要求，但是额外空间是O(N)。因此我们需要换种思路，一边穷举一边记录已知的有用信息。当我们穷举到第i个数时，假设我们尚未找到答案，那么有以下几种情况：

    我们只找到一个数（前i-1个数没有递增的两个数），此时我们记录前i-1个数的最小值。我们已找到递增的二元组子序列，此时我们需要记录的是这样的最小二元组（以第二个数为第一关键字）

细心的读者可以发现，有时我们需要记录第三个数。比如已有递增子序列（3，5），之后又出现一个数1，我们必须记录1，因为如果之后出现2，（1，2）当递增序列会覆盖（3，5）。 

# Testcases:

>>> incressingThriplet_O1([1,2,3,4,5,6])
True
>>> incressingThriplet_O1([6,5,5,6,6,6])
False
>>> incressingThriplet_O1([8,9,3,5,8])
True
>>> incressingThriplet_O1([1,2,1,1,1,1])
False
"""

# O(n)时间复杂度 O(1)空间复杂度
def incressingThriplet_O1(numList):
    if len(numList) <= 2: return False;
    # 记录中间值，固定的空间(first, second)
    # first, second 默认取 list 中最大元素，如果是最小的或随机的，第二个递增元素就不能够确定 
    first, second = max(numList), max(numList)
    for iNum in numList:
        if iNum <= first:
            first = iNum
        if iNum > first and iNum <= second: 
            second = iNum
        if iNum > second:
            # print(first, second, iNum)
            return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
