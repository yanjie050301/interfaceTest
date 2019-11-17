#coding:utf-8
import unittest,json
import requests
from ddt import ddt,data,unpack
from common.readexcle import Openexcle
from common.configHttp import ConfigHttp
from common.readConfig import Readconfig
from common.writeExcel import WriteExcel
a = Openexcle()
testda = a.zzvaleu()
b = ConfigHttp()
c = Readconfig()
ur = c.get_url('url')
# print(ur)
d = WriteExcel()
@ddt
#继承unittest.TestCase类，作用为：
class MyTestCase1(unittest.TestCase):
    @data(*testda)
    @unpack
    def test_normal(self,id,url,method,param,expect):
        # 拼接最终的url
        u = ur + str(url)
        result = b.getrequest(u,param,method)
        real = result['errorCode']
        try:
            self.assertEqual(real,int(expect))
            status ='success'
        except Exception as msg:
            print(msg)
            status = 'fail'
            print('用例失败,实际结果为：',real,'预期结果为：',expect)
        d.write(int(id),real,status)
if __name__ == '__main__':
    unittest.main()

