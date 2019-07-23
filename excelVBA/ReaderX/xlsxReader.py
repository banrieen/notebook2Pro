""" Excel data reader """

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


def reader(filepath,sheetName):
    df = pd.read_excel(filepath, sheetName)
    print("Column headings:")
    print(df.columns)
    print(df['工单号'],df['编码'],df['单价'])

def get_datas(filter):
    pass


if __name__ == "__main__":
    filepath = r"C:\Users\Lizhen\workspace\notebook\excelVBA\ReaderX\数据源.xlsx"
    sheetName = "数据源 (2)"
    reader(filepath,sheetName)