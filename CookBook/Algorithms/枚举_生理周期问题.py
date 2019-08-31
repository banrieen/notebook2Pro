""" 生理周期
人的体力，情商，之上的高峰日子，分别在每隔23天，28天和33天出现一次。对于每个人想知道3个高峰落在
同一天。
给定3个高峰出现的日子p,e,i，再给定一个指定的日子d，任务是输出日子d之后，下一次3个高峰落在同一天的日志，
用距离d的天数表示；输入4个整数，p,e,i和d，分别表示体力，情感和智力高峰出现的日子，d是给定的日子
，可能小于p,e,i，所有给定的日子非负且小于等于365，所求的日子小于或等于21252
 """

def find_luck_date(p,e,i,d):
    k = d
    while True:
        k += 1
        if (k-p)%23 == 0 and k <= 21252:
            break
    while True:
        k += 23
        if (k-e)%28 == 0  and k <= 21252:
            break
    while True:
        k += 23*28
        if (k-i)%33 == 0  and k <= 21252:
            break
    date = k - d
    return date

if __name__ == "__main__":
    luckyDate = find_luck_date(p=35,e=44,i=90,d=120)
    print(luckyDate)

