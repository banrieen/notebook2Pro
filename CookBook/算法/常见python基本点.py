# 检查 For else
""" 在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。 """
""" for loops also have an else clause which most of us are unfamiliar with. The else clause executes after the loop completes normally. This means that the loop did not encounter a break statement. They are really useful once you understand where to use them. I, myself, came to know about them a lot later. """

for  i in range(3):
    if i == 2:
        print(i)
        break

else:
    print(0)

for i in range(3):
    if i == 2:
        print(i)
else:
    print(0)


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')            
# 检查  Try except else
"""
# try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
  try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。

    如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
    如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印默认的出错信息）。
    如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。 """
""" ou can include an else clause when catching exceptions with a try statement. The statements inside the else block will be executed only if the code inside the try block doesn’t generate an exception. """
""" try-finally 语句无论是否发生异常都将执行最后的代码。 
try:
<语句>
finally:
<语句>    #退出try时总会执行
raise
 """
def A():
    try:
        print(1)
        a=3//0
    except:
        print(2)
        return
    finally:
        print(3)
    print(4)
    return

def B():   
    try:
        fh = open("testfile", "w")
        fh.write("这是一个测试文件，用于测试异常!!")
    except IOError:
        print ("Error: 没有找到文件或读取文件失败")
    else:
        print ("内容写入文件成功")
        fh.close()
    finally:
        print("Always to be excuted!")

A()
B()

try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
else:
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')

# 装饰器

def A(func):
    def check():
        print(1)
        func()
        print(2)
        return
    return check

def B(func):
    def check():
        print(3)
        func()
        print(4)
        return
    return check

@A
def test():
    print(5)
    return
# test()

@A
@B
def test():
    print(5)
    return
test()


# def decrator(*args,**kargs):
#     def wraper(func):
#         def sum(n):
#             print(n, kargs)
#             n = n + kargs["add_num"]
#             return func(n)
#         return sum
#     return wraper

def decrator(add_num):
    def wraper(func):
        def sum(n):
            n = n + add_num
            return func(n)
        return sum
    return wraper
    
@decrator(add_num=2)
def add(n):
    return n


num = add(3)
print(num)

nginx 负载均衡类型，轮询； 高可用

Django 中间件，
Django ORM 搜索
Django 跨站点攻击预防原理

redis 崩溃，缓存，协程；非字符串怎么存储
进程管理，mysql 分表，分库；
Vue

postman