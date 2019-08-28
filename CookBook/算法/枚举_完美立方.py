""" 形状如 a^3 = x^3 + y^3 + z^3 
对于任意给定的的N (N<=100),寻找所有的四员组，其中a,b,c,d大于1，小于等于N,且b<=c<=d
"""

def cube(n):
    for a in range(2,n):
        for x in range(2,a):
            for y in range(x,a):
                for z in range(y, a):
                    if a*a*a == x*x*x + y*y*y + z*z*z:
                        print(f"Cube={a}, Tiple = {x},{y},{z}")


# for n in range(2,100):
print(cube(100))