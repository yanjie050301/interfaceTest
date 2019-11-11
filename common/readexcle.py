#coding:utf-8
import xlrd
# 找到excle，并打开
# data = xlrd.open_workbook(r'F:\test\code\vip3test\data.xls')
# sheet = data.sheet_by_index(0)
# value = sheet.cell(0,0)
# print(value)
class Openexcle():
    def __init__(self):
        self.data = xlrd.open_workbook(r'F:\test\interfaceTest\testData\data.xls')
    def geturlSheet(self):
        # 定位到sheet页
        sheet0 = self.data.sheet_by_index(0)
        urlSheet=[]
        nrows = sheet0.nrows
        n = 1
        while n<nrows:
            row_value = sheet0.row_values(n)
            urlSheet.append(row_value)
            n = n+1
        return urlSheet
    def getparamSheet(self):
        sheet1 = self.data.sheet_by_name('paramSheet')
        paramSheet = []
        nrows = sheet1.nrows
        # 将sheet里面的数据读取出来
        n = 1
        while n < nrows:
            row_value = sheet1.row_values(n)
            paramSheet.append(row_value)
            n = n + 1
        return paramSheet
    def getassertSheet(self):
        sheet2 = self.data.sheet_by_name('assertSheet')
        assertSheet = []
        nrows = sheet2.nrows
        n = 1
        while n < nrows:
            row_value = sheet2.row_values(n)
            assertSheet.append(row_value)
            n = n + 1
        return assertSheet
    def zzvaleu(self):
        # 组装成测试数据
        urlSheet = self.geturlSheet()
        paramSheet = self.getparamSheet()
        assertSheet = self.getassertSheet()
        datelist =[]
        data1=[]
        m =0
        while m<3:
            a = urlSheet[m][0]
            b = urlSheet[m][1]
            c = urlSheet[m][3]
            d = paramSheet[m][1]
            e = assertSheet[m][1]
            datelist.append(a)
            datelist.append(b)
            datelist.append(c)
            datelist.append(d)
            datelist.append(e)
            # print("//",datelist,m)
            data1.append(datelist)
            # print(type(datelist[3]),datelist[3])
            datelist = []
            m = m+1
        return data1

if __name__ == '__main__':
    a = Openexcle()
    print(a.zzvaleu())







