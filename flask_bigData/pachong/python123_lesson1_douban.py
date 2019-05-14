# -*- coding: utf-8 -*-

import re
from requests_html import HTMLSession
from localCsv import SimpleCSV


class Python123Pachong():
    def __init__(self):
        self.session = HTMLSession()
    
    def get_html(self,links):
        try:
            rsp = self.session.get(links)
            # rsp.html.render()
            return rsp
        except IOError:
            return 0 

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
        rst = []
        for iLink in taskLink:
            rsp = self.get_html(iLink["url"])
            tempRst = self.get_contents(rsp,iLink["selectors"])
            rst.append(tempRst)
        return rst
    
    def save_rst(self, filePath, fileName, rst):
        newCsv = SimpleCSV(filePath, fileName, rst)
        newCsv.write_datas()
            


if __name__ == "__main__":
    taskLink = [
                {'url':'https://movie.douban.com/subject/1292052/','selectors':{'title':'#content > h1 > span:nth-child(1)','date':'#info > span:nth-child(16)'}},
                {'url':'https://movie.douban.com/subject/1962665/','selectors':{'title':'#content > h1 > span:nth-child(1)','date':'#info > span:nth-child(19)'}},
                {'url':'https://movie.douban.com/subject/26752088/','selectors':{'title':'#content > h1 > span:nth-child(1)','date':'#info > span:nth-child(16)'}},
                # {'url':'http://stock.finance.sina.com.cn/usstock/quotes/aapl.html','selectors':{'storePrice':'#hqSummary','storeName':'.block_hq > div:nth-child(1) > h1:nth-child(1)'}},
                # {'url':'http://stock.finance.sina.com.cn/usstock/quotes/bidu.html','selectors':{'storePrice':'#hqSummary','storeName':'.block_hq > div:nth-child(1) > h1:nth-child(1)'}},
                # {'url':'http://stock.finance.sina.com.cn/usstock/quotes/msft.html','selectors':{'storePrice':'#hqSummary','storeName':'.block_hq > div:nth-child(1) > h1:nth-child(1)'}},
    ]
    
    saveFile = r"C:\Users\Lizhen\eclipse-workspace\exercise-notebook\flask_bigData\pachong\results"
    saveFileName = "pachong123.csv"
    pc = Python123Pachong()
    rst = pc.pachong(taskLink)
    pc.save_rst(saveFile,saveFileName,rst)