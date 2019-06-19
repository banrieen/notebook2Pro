# from requests_html import HTMLSession
# import re
# from matplotlib import pyplot as plt

# salary_element = re.compile('<p.*>(\d+)K-(\d+)K</p>')
# salary = []
# disabled_button_element = re.compile('<button class="btn soupager__btn soupager__btn--disable" disabled="disabled">下一页</button>')
# disabled_button = None
# p = 1

# while not disabled_button and p <= 5:
#     print('正在爬取第' + str(p) + '页')
#     url = 'https://sou.zhaopin.com/?p=' + str(p) + '&jl=530&kw=爬虫工程师&kt=3'
#     session = HTMLSession()
#     page = session.get(url)
#     page.html.render(sleep=3)
#     # 提取出薪资，保存为形如 [[10,20], [15,20], [12, 15]] 的数组
#     salary += salary_element.findall(page.html.html)
#     # 判断页面中下一页按钮还能不能点击
#     disabled_button = disabled_button_element.findall(page.html.html)
#     p = p + 1
#     session.close()

# # 求出每家公司的平均薪资，比如 [12, 15] 的平均值为 13
# salary = [(int(s[0]) + int(s[1])) / 2 for s in salary]
# # 划定薪资范围，便于展示，你也可以尝试其它展示方案
# low_salary, middle_salary, high_salary = [0, 0, 0]
# for s in salary:
#     if s <= 15:
#         low_salary += 1
#     elif s > 15 and s <= 30:
#         middle_salary += 1
#     else:
#         high_salary += 1
# # 调节图形大小，宽，高
# plt.figure(figsize=(6, 9))
# # 定义饼状图的标签，标签是列表
# labels = [u'<15K', u'15K-30K', u'>30K']
# data = [low_salary, middle_salary, high_salary]
# plt.pie(data, labels=labels)
# # 设置x，y轴刻度一致，这样饼图才能是圆的
# plt.axis('equal')
# plt.legend()
# plt.show()


# <button class="btn soupager__btn soupager__btn--disable" disabled="disabled">下一页</button>
# -*- coding: utf-8 -*-

import re
from requests_html import HTMLSession
from localCsv import SimpleCSV
from matplotlib import pyplot as plt

class Python123Pachong():
    def __init__(self):
        self.session = HTMLSession()
        pass
    
    def get_html(self,links):
        try:
            rsp = self.session.get(links)
            rsp.html.render(sleep=5)
            return rsp
        except IOError:
            return 0 
        # finally:
        #     self.session.close()

    def get_contents(self, rsp="", selectors={}, **kargvs):
        rsts = {}
        for target, selector in selectors.items():
            tmpRst = rsp.html.find(selector,first=True)
            rstText = tmpRst.text
            rsts[target] = rstText.encode('utf-8')
        return rsts


    def pachong(self,taskLink):
        if taskLink and len(taskLink)<=0:
            return 0
        salary_element = re.compile('<p.*>(\d+)K-(\d+)</p*')
        disabled_button_element = re.compile('<button.* disabled="disabled">下一页</button>')
        p = 1
        salary = []
        disable_button = False
        while not disable_button and p <= 25:
            print("爬取第 {} 页".format(str(p)))
            taskLink = 'https://sou.zhaopin.com/?p={}&jl=765&kw=python&kt=3'.format(str(p))
            session = HTMLSession()
            rsp = session.get(taskLink)
            rsp.html.render(sleep=5)
            tmpSalary = salary_element.findall(rsp.html.html)
            salary.append(tmpSalary)
            disabled_button = disabled_button_element.findall(rsp.html.html)
            p += 1
            self.session.close()
        return rst
    
    def draw_salary(self, rst):
        salary = [(int(s[0]) + int(s[1])) / 2 for s in rst]
        low_salary, middle_salary, high_salary = [0, 0, 0]
        for s in salary:
            if s <= 15:
                low_salary += 1
            elif s > 15 and s <= 30:
                middle_salary += 1
            else:
                high_salary += 1

        # 调节图形大小，宽，高
        plt.figure(figsize=(6, 9))
        # 定义饼状图的标签，标签是列表
        labels = [u'<15K', u'15K-30K', u'>30K']
        data = [low_salary, middle_salary, high_salary]
        plt.pie(data, labels=labels)
        # 设置x，y轴刻度一致，这样饼图才能是圆的
        plt.axis('equal')
        plt.legend()
        plt.show()

    def save_rst(self, filePath, fileName, rst):
        newCsv = SimpleCSV(filePath, fileName, rst)
        newCsv.write_datas()
            

if __name__ == "__main__":
    taskList = ['python','java']
    taskLink = 'https://sou.zhaopin.com/?p=1&jl=765&sf=0&st=0&kw=python&kt=3'
    # taskLink = 'https://sou.zhaopin.com/?p={page}&jl=765&sf=0&st=0&kw={language}&kt=3'.format(page=1,language='python'),
    selectors = {'language':'python','salary':'#listContent > div:nth-child(88) > div > a > div.contentpile__content__wrapper__item__info__box.contentpile__content__wrapper__item__info--desc.itemBox.descBox > div.contentpile__content__wrapper__item__info__box__job.jobDesc > p','regin':'#listContent > div:nth-child(83) > div > a > div.contentpile__content__wrapper__item__info__box.contentpile__content__wrapper__item__info--desc.itemBox.descBox > div.contentpile__content__wrapper__item__info__box__job.jobDesc > ul > li:nth-child(1)'}
    
    finishTag = '#pagination_content > div > button.btn.soupager__btn.soupager__btn--disable'
    saveFile = r"C:\Users\Lizhen\eclipse-workspace\exercise-notebook\flask_bigData\pachong\results"
    saveFileName = "pachong123.csv"
    pc = Python123Pachong()
    rst = pc.pachong(taskLink)
    pc.draw_salary(rst)
    # pc.save_rst(saveFile,saveFileName,rst)
