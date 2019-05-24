""" 富途面试题 """

""" for循环中的lambda与闭包
# https://www.jianshu.com/p/84f3e0f4d218
def funx():
    return [lambda x : i*x for i in range(0,4)]
[0,1,2,3]
# ss = [fun(2) for fun in funx()]
print(funx())
for fun in funx():
    print(fun)
    print(fun(2)) """

""" 赋值与地址引用
def fun(x=0,y=[]):
    y.append(x)
    return y

print(fun())
print(fun(1,[1]))
print(fun(2)) """


""" 数字i 都大于左边的数字，都小于右边的数字
listA = [1,2,4,3]
rst = [1,2]
def findI(listA):
    rst = []
    length = len(listA)
    for i in range(length):
        if i == 0 and listA[0] < min(listA[1:]):
            rst.append(listA[0])
        elif i == length - 1 and listA[-1] > max(listA[:-1]):
            rst.append(listA[-1])
            break
        elif listA[i] <= min(listA[i:]) and listA[i] > max(listA[:i]):
            rst.append(listA[i])
        else:
            continue
    return rst
print(listA)
print(findI(listA)) """

""" 斐波那契递归数组
 楼梯有n阶台阶，上楼可以一步上1阶,2阶，3阶，编程序计算共有多少种不同的走法？


def dianTi(n):
    if n <= 2:
        return n
    elif n == 3: #4-> 1,2,1-1-2,2-1-1,1-2-1
        return 3
    else:
        return dianTi(n-1)+dianTi(n-2)
for n in range(10):
    print(dianTi(n))

"""


""" 跨域访问 JSONP
aa.net -> bb.net
https://www.cnblogs.com/aszx0413/articles/1886819.html
https://www.cnblogs.com/chenshishuo/p/4919224.html
 """

 """  类的重载 __new__
 https://howto.lintel.in/python-__new__-magic-method-explained/
 https://www.codevoila.com/post/68/new-and-init-in-python
      初始化   __init__
 """