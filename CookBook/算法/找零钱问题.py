#!/usr/bin/env python3
""" 找钱问题
# 对于现实生活中的找零问题，假设有数目不限，面值为2,5,10的硬币, 求出找零方案。
# 
# 对于此类问题，贪心算法可以找到近似最优解；
# 动态规划可以找到最优解；其中也可以根据具体情况做一些优化。
# 
# moneysValues = [2,5,10]
# moneysCount = [i, j, k]  #示例 [30,40,50]
# price = N #示例 95

# Testtcases：
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
90 不能找零

>>> change([2,5,10],[30,0,50],95)
95 不能找零

>>> change([2,5,10],[30,40,1],94)
94 不能找零
 """

def change(moneysValues, moneysCount, priceN):
    moneysCounts = dict(zip(moneysValues, moneysCount))
    if not assert_kinds_enough(moneysValues, priceN):
        return display(None, priceN)

    rst = get_greedy_set(moneysValues, priceN)
 
    # 一般不考虑数量限制
    rst= assert_money_counts(rst, moneysCounts)
    return display(rst, priceN)

def get_DP_set(moneysValues, priceN):
    # 规划 i,j,k 的“最优”组合，算法复杂度主要在此
    # 动态规划
    rst = {m:0 for m in moneysValues}
    for moneyValue, count in moneysCount.items():
        while priceN > 0 and priceN >= moneyValue :
            priceN -= moneyValue
            rst[moneyValue] += 1
    return rst


def get_greedy_set(moneysValues, priceN):
    # 规划 i,j,k 的“最优”组合：贪心算法
    # 时间复杂度 O(MN),M为面值种类数，N为给定的找零的钱数；空间复杂度 O(1),至多用到2个确定大小的 dict
    
    # 尽量使用大额面值，此题面值10,5,2有限，贪心算法可以得到最优解
    moneysValues = sorted(moneysValues, reverse=True)
    # 尽量使用小额面值
    # moneysValues = sorted(moneysValues, reverse=False)

    rst = {moneyValue:0 for moneyValue in moneysValues}
    for moneyValue in moneysValues:
        while priceN >= moneyValue and priceN > 0:
            priceN -= moneyValue
            rst[moneyValue] += 1
    return rst

def assert_money_counts(rst, moneysCounts):
    # 判断组合是否符合 i,j,k 数量限制: rst[i] <= moneysCounts[i]
    # 此处也可以考虑数量限制的特殊情况

    if rst[2]%5 > moneysCounts[2]:
        return False
    elif rst[5]%2 > moneysCounts[5]:
        return False
    elif rst[10]%10 > moneysCounts[10]:
        return False
    else:
        return rst

def assert_kinds_enough(moneysValues, price):
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
    # 
    # change([2,5,10],[30,40,50],109)

