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
        # print("4444",id,url,method,param,expect)
        #         # if method == 'post':
        #         #     result = requests.post(url=url,data=eval(param))
        #         #     status = result.json()['errorCode']
        #         #     try:
        #         #         self.assertEqual(status,int(expect))
        #         #     except AssertionError:
        #         #         print('用例失败,实际结果为：',status,'预期结果为：',expect)
        #         # else:
        #         #     result = requests.get(url=url, params =param)
        #         #     status = result.json()['errorCode']
        #         #     try:
        #         #         self.assertEqual(status,int(expect))
        #         #     except:
        #         #         print('用例失败,实际结果为：',status,'预期结果为：',expect)
        u = ur + str(url)
        # print('2222',u)
        result = b.getrequest(u,param,method)
        print('3333',result)
        real = result['errorCode']
        try:
            print('ceshiceshi')
            self.assertEqual(real,int(expect))
            print('ceshicesh55555555i')
            status ='success'
        except:
            # print(msg)
            status = 'fail'
            print('用例失败,实际结果为：',real,'预期结果为：',expect)
        print('id为',type(id))
        print('real为',real)
        print('status为',status)
        d.write(int(id),real,status)
if __name__ == '__main__':
    unittest.main()

