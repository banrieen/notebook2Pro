# -*- cooding: utf-8 -*-

import csv
import os


class SimpleCSV():
    def __init__(self, filePath, fileName, datas):
        self.datas = datas
        if os.path.isdir(filePath):
            if '.csv' == os.path.splitext(fileName)[1]:
                newFile = os.path.join(filePath,fileName)
                self.filePath = newFile
            else:
                raise IOError("文件类型错误")
        else:
            raise IOError("文件路径错误")
    
    def write_datas(self):
        titles = self.datas[0].keys()   
        with open(self.filePath, 'w',newline='') as csvfile:
            fieldnames = self.datas[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for iLine in self.datas:
                    writer.writerow(iLine)