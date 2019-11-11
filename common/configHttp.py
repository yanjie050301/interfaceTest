#coding:utf-8
# 判断请求接口方式，已达到运行相关代码
import configparser
import requests
import json
class ConfigHttp():
    def get(self,url,data = 'none'):
        try:
            request = requests.get(url = url,params = data)
            return request.json()
        except Exception as msg:
            print(msg)
            return None
    def post(self,url,data):
        try:
            request = requests.post(url = url,data = data)
            return request.json()
        except Exception as msg:
            print(msg)
    def getrequest(self,url,data,method):
        if method=='get':
            return self.get(url,data)
        elif method=='post':
            return self.post(url,data)


if __name__ == '__main__':
    a = ConfigHttp()
    c = 'https://www.wanandroid.com/user/register'
    b = a.getrequest(c,{'username':'liangchao03','password':'123456','repassword':'123456'},'post')
    print(b)