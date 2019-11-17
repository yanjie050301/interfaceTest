#coding:utf-8
# 获取config中的配置信息
import configparser
configPath = 'F:\\test\\interfaceTest\\config.ini'
class Readconfig():
    def __init__(self):
        # 实例化configparser对象
        self.config = configparser.ConfigParser()
        # 调用read方法读取config.ini文件
        self.config.read(configPath,encoding='utf-8')
    def get_email(self,name):
        value = self.config.get('EMAIL',name)
        return value
    def get_url(self,name):
        value = self.config.get('HTTP', name)
        return value
    def get_db(self,name):
        value = self.config.get('MYSQL',name)
        return value
if __name__ == '__main__':
    b =Readconfig()
    print(b.get_db('testuser'))