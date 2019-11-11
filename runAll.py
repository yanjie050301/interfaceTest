#coding:utf-8
import unittest
import time
import HTMLTestRunner
start_dir = 'F:\\test\\interfaceTest\\testCase'
def run_case():
    discover = unittest.defaultTestLoader.discover(start_dir,pattern='test_case.py',top_level_dir=None)
    return discover
# def run_report():
if __name__ == '__main__':
    report_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    filename = 'F:\\test\\interfaceTest\\testCase\\'+ report_time + '.html'
    print('报告路径',filename)
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'闫洁的测试报告',
        description=u'用例执行情况'
    )
    runner.run(run_case())
    fp.close()