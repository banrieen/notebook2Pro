# -*- coding: utf-8 -*-
# /usr/local/bin env python3
''' Excel 数据读取
    # 读取本地的 excel 2013 版本以上的，以xlxs后缀的文件
    # Author： lizhen
    # Date： 2018-08-11
 '''

import os, sys
import xlrd, xlwt
# import collection

def read_excel(filepath):
    book = None
    sheet = None
    datas = {}
    if not os.path.isfile(filepath):
        raise OSError("Excel 文件不存在！")
    else:
        book = xlrd.open_workbook(filepath)
    # python2.7 Need to decode str to utf-8 
    # print("Excel 共有工作表 {} 个，工作表的名称为：{}".format(book.nsheets, ", ".join([iName.encode("utf-8") for iName in book.sheet_names()])))
    
    # Pythn3 
    print("Excel 共有工作表 {} 个，工作表的名称为：{}".format(book.nsheets, ", ".join([iName for iName in book.sheet_names()])))

    # datas = {book.sheet_by_index[i].name:(book.sheet_by_index[i].ncols,book.sheet_by_index[i].nrows) for i in range(book.nsheets) if book.sheet_by_index[i]}
    # print(datas)
    return book

def get_sheet_datas(sheet, col,row):
    r, c = 0, 0
    while c < col and c < sheet.ncols:
        while r < row and r < sheet.nrows:
            print(sheet.cell_value(row,col))
            r += 1 
        c += 1


book = read_excel("./智慧城职能部门联络人清单-2018年12月v2.xlsx")
for sh in range(book.nsheets):
    get_sheet_datas(book.sheet_by_index(sh),2,3)