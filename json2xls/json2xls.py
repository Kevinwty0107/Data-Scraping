# -*- coding: utf-8 -*
import json
from importlib import reload

import xlwt
import os
import sys

reload(sys)
sys.getdefaultencoding()
path='/Users/wangtaiyi/Desktop/百度实习/merged'
os.chdir(path)
dir = os.getcwd()
dirList = os.listdir(dir)
print(dirList)


def readjson():
    s = []
    for file in dirList:
        if ".json" in file:
                fr = open(file, 'r+', encoding='utf-8')  # 用with打开文件
                data = json.load(fr)  # 用json中的load方法，将json串转换成字典
                s.append(data)  # 保存所有字典到列表中
    return s


def writeExcel(J):
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet', cell_overwrite_ok=True)
    rvalue = J
    # print rvalue
    title = []
    for k, v in enumerate(rvalue[0]):
        title.append(v)
        booksheet.write(0, k, v)
    print(title)

    for a in range(len(rvalue)):
        for b in range(len(title)):
            try:
                d = title[b]
                c = str(rvalue[a][d])
                # if c:
                booksheet.write(a + 1, b, c)
                # else:
                #     if c == '':
                #         booksheet.write(a + 1, b, '{}')
                #     else:
                #         booksheet.write(a + 1, b, '{}')
            except:
                booksheet.write(a + 1, b, '')
    workbook.save(u'Merge' + '.xls')


if __name__ == '__main__':
    qqq = json.dumps(readjson()[0], encoding="utf-8", ensure_ascii=False)
    writeExcel(readjson()[0])