#!/usr/bin/env python3
""" 找零钱问题
# 对于现实生活中的找零问题，假设有数目不限，面值为2,5,10的硬币, 求出找零方案。
# 发现这个问题跟 鸡兔同笼，背包问题
# 对于此类问题，贪心算法可以找到近似最优解；
# 动态规划可以找到最优解；其中也可以根据具体情况做一些优化。
# 
# moneyValues = [2,5,10]
# moneyCount = [i, j, k]  #示例 [30,40,50]
# price = N #示例 95

# Testtcases：(从面值大的币种查找的用例)
>>> change([2,5,10],[30,40,50],95)
95 可找零为 9 张10元，1 张5元，0 张2元

>>> change([2,5,10],[30,40,50],94)
94 可找零为 9 张10元，0 张5元，2 张2元

>>> change([2,5,10],[30,40,50],90)
90 可找零为 9 张10元，0 张5元，0 张2元

>>> change([2,5,10],[30,40,50],109)
109 可找零为 10 张10元，1 张5元，2 张2元

# 判断币种组合
>>> change([2,5,10],[30,40,50],93)
93 不能找零

>>> change([2,5,10],[30,40,50],91)
91 不能找零

# 判断数量限制
>>> change([2,5,10],[5,40,5],90)
90 可找零为 5 张10元，8 张5元，0 张2元

>>> change([2,5,10],[30,0,50],95)
95 不能找零

>>> change([2,5,10],[30,40,1],94)
94 可找零为 1 张10元，16 张5元，2 张2元
 """

def change(moneyValues, moneyCount, priceN):
    moneyCounts = dict(zip(moneyValues, moneyCount))
    if not assert_kinds_enough(moneyValues, priceN):
        return display(None, priceN)

    rst = get_DP_set_from_max(moneyCounts, priceN)
    # rst = get_DP_set_from_min(moneyCounts, priceN)
    # rst = get_greedy_set(moneyValues, priceN)
    return display(rst, priceN)

def get_DP_set_from_max(moneyCounts, priceN):
    # 规划 i,j,k 的“最优”组合，算法复杂度主要在此
    # 动态规划
    
    # 尽量使用大额面值，这样张数最少，且少了一层循环
    # 时间复杂度为 面值种类数M，空间复杂度为O(1),结果的 rst 用的一个有限 dict
    moneyCounts = dict(sorted(moneyCounts.items(), key=lambda x:x[0], reverse=True))
    rst = {value:0 for value, count in moneyCounts.items()}
    if sum(value * count for value, count in moneyCounts.items()) < priceN:
        return None
    for value, count in moneyCounts.items():
        if priceN <= 0:
            break
        tmpCount = priceN // value
        if count > 0 or count >= tmpCount:
            if count <= tmpCount:
                rst[value] += count
            else:
                rst[value] += tmpCount
            priceN -= rst[value] * value
        else:
            continue
    if priceN > 0:
        return None
    else:
        return rst

def get_DP_set_from_min(moneyCounts, priceN):
    # 规划 i,j,k 的“最优”组合，算法复杂度主要在此
    # 动态规划
    
    # 尽量使用小额面值，这样张数最多，在张数限制下确定是否有解
    # 时间复杂度 O(MN),M为面值种类数，N为给定的找零的钱数；空间复杂度为O(1),结果的 rst 用的一个有限 dict
    moneyCounts = sorted(moneyCounts.items(), key=lambda x:x[0], reverse=False)
    rst = {moneyValue:0 for moneyValue, count in moneyCounts}
    if sum(moneyValue * count for moneyValue, count in moneyCounts) < priceN:
        return None
    for i in range(0,len(moneyCounts)):
        iCount = 0
        if moneyCounts[i][1] <= 0:
            continue
        for j in range(0, moneyCounts[i][1]+1):
            if i > (len(moneyCounts)-2):
                break
            if (priceN - moneyCounts[i][0]*j) % moneyCounts[i+1][0] == 0:
                iCount = j
            if iCount*moneyCounts[i][0] >= priceN:
                break
        if iCount != 0:
            rst[moneyCounts[i][0]] += iCount
            priceN -= iCount * moneyCounts[i][0] 
        elif  moneyCounts[i][1] == 0:
            continue
        else:
            rst[moneyCounts[i][0]] += priceN // moneyCounts[i][0]
            priceN -= rst[moneyCounts[i][0]] * moneyCounts[i][0]
        if priceN <= 0:
            break
    if priceN > 0:
        return None  
    return rst

def get_greedy_set(moneyValues, priceN):
    # 规划 i,j,k 的“最优”组合：贪心算法
    # 时间复杂度 O(MN),M为面值种类数，N为给定的找零的钱数；空间复杂度 O(1),至多用到2个确定大小的 dict
    
    # 尽量使用大额面值，不考虑币种数量限制
    moneyValues = sorted(moneyValues, reverse=True)

    rst = {moneyValue:0 for moneyValue in moneyValues}
    for moneyValue in moneyValues:
        while priceN >= moneyValue and priceN > 0:
            priceN -= moneyValue
            rst[moneyValue] += 1
    return rst

def assert_kinds_enough(moneyValues, price):
    # 面值中不包含1， 所以定有一部分 N 不能够组合，如1, 3, 等
    if price % 5 == 0:
        return True
    elif price % 2 == 0:
        return True
    elif (price % 5 != 0) and ((price % 5) % 2 == 0):
        return True
    else:
        return None

def display(rst, price):
    if rst:
        print(f"{price} 可找零为 {rst[10]} 张10元，{rst[5]} 张5元，{rst[2]} 张2元")
    else:
        print(f"{price} 不能找零")


if __name__ == "__main__":
    import doctest
    doctest.testmod()

