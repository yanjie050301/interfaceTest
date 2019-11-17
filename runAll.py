#coding:utf-8
import unittest
import time
import HTMLTestRunner
from common.configEmail import ConfigEmail
import os
email = ConfigEmail()
# 获取当前文件的绝对路径+文件名
abspath = os.path.abspath(__file__)
# 获取文件所在路径，不加文件名,相当于获取上一个路径
path = os.path.dirname(abspath)
# 拼接文件路径
start_dir = path + '\\' + 'report'
print(start_dir)
def run_case():
    discover = unittest.defaultTestLoader.discover(start_dir,pattern='test_case.py',top_level_dir=None)
    return discover
# def run_report():
if __name__ == '__main__':
    report_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    filename = start_dir + '\\'+ report_time + '.html'
    print('报告路径',filename)
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'闫洁的测试报告',
        description=u'用例执行情况'
    )
    runner.run(run_case())
    fp.close()
    email.sendemail()
