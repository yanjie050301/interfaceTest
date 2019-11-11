#coding:utf-8
from xlutils.copy import copy
import xlrd
# rb = xlrd.open_workbook('F:\\test\\code\\interfaceTest\\testData\\data.xls')
# wb = copy(rb)
# ws = wb.get_sheet(3)
# ws.write(0,0,'111')
# wb.save('F:\\test\\code\\interfaceTest\\testData\\data.xls')
class WriteExcel():
    def __init__(self):
        self.rb = xlrd.open_workbook('F:\\test\\interfaceTest\\testData\\data.xls')
        self.wb = copy(self.rb)
        self.ws = self.wb.get_sheet(2)
    def write(self,id,real,status):
        try:
            self.ws.write(id,2,real)
            self.ws.write(id,3,status)
            self.wb.save('F:\\test\\interfaceTest\\testData\\data.xls')
            print('保存成功')
        except Exception as msg:
            print(msg)
if __name__ == '__main__':
    a = WriteExcel()
    a.write(1,'real','status')
