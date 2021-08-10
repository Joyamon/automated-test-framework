# coding=utf-8


import xlrd, json


class Excels(object):
    '''构造 Excel 工具类'''

    def readExcelData(self, rowx):
        '''读取rowx行数'''
        book = xlrd.open_workbook(r'C:\Users\Administrator\PycharmProjects\接口测试框架\testAPI\Data\data.xls')
        table = book.sheet_by_index(0)
        return table.row_values(rowx)

    def readUrl(self, rowx):
        '''读取接口地址'''
        print(self.readExcelData(rowx)[0])
        return self.readExcelData(rowx)[0]

    def readData(self, rowx):
        '''读取请求参数'''
        print(self.readExcelData(rowx)[1])
        return json.loads(self.readExcelData(rowx)[1])

    def readToken(self, rowx):
        '''读取Token'''
        return json.loads(self.readExcelData(rowx)[2])


# 测试入口
if __name__ == '__main__':
    test = Excels()
    test.readData(2)
    test.readUrl(2)
