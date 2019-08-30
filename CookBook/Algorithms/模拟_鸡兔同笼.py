""" 鸡兔同笼
一个笼子里关有若干只鸡，兔子，已经知道总脚数 a， 则笼子里至少有多少只动物，至多有多少只动物？
# 输入数据： 一个正整数 n (n<=1000)，表示测试数据的组数n,接下来n组数据一行，每一行一个正整数a（a<=32768)
# 输出要求：包含n行，每行对应一个输入，包含2个正整数，第一个是最少动物数，第二个是最多动物数，用空格分开，如果没有满足的答案，用0 表示
 """
# 兔子和鸡必须同时存在的情况，枚举法，容易超时
def count_animal(n):
    rabit = 4
    chiken = 2
    for  i in range(1,n+1):
        for j in range(i, n+1):
            if 4*i + 2*j == n:
                print(f"rabit: {i}, chiken: {j}")
            else: 
                print(f"rabit: 0, chiken: 0")

# 模拟分析法
def count_animal_like(n):
    nFeets = 4
    nCases = 2
    while (1):
        nCases = nCase=int(input("测试数据行数： "))
        if not nCases:
            break
        for case in range(0, nCases):
            nFeets = int(input("总脚数： "))
            if nFeets % 4 == 0:
                print(f"min: {nFeets // 4}, max:{nFeets // 2}")
            elif nFeets % 2 == 0:
                min = (nFeets // 4) + 1 if nFeets >=4 else 1
                print(f"min: {min}, max:{nFeets // 2}")
            else:
                print(f"min: {0}, max:{0}")

count_animal_like(100)