#coding:utf-8
'''
功能：
    1.配置发送邮件属性
    2.读取邮件配置
    3.发送邮件
'''
import smtplib
# 导入编辑邮件正文的包
from email.mime.text import MIMEText
# 导入邮件附件包
from email.mime.multipart import MIMEMultipart
from common.readConfig import Readconfig
from email.header import Header
import os
email = Readconfig()
class ConfigEmail():
    login = email.get_email('login_user') #登录者账号
    password = email.get_email('login_pass') #登录的密码
    sender = email.get_email('sender')  #发件人邮箱
    receivers = email.get_email('receiver') #收件人邮箱
    host = email.get_email('mail_host')    #设置服务器
    emailport = email.get_email('mail_port') #邮箱配置端口号
    # 创建一个附件实例
    message = MIMEMultipart()
    def config_file(self):
        file = self.getfile()
        openf = open(file, 'rb').read()
        # 配置附件
        att = MIMEText(openf, 'plain', 'utf-8')
        att['Content=Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename = report.html'  # 给发送的附件命名
        self.message.attach(att)
        self.message['From'] =self.sender# 发件人的名称
        self.message['To'] = self.receivers #收件人的名称
        # Cc = ['1353037583@qq.com']
        # self.message['Cc'] = ','.join(Cc) #抄送人的名称
        subject = email.get_email('subject')
        self.message['Subject'] = Header(subject,'utf-8')#发送邮件的标题
        # 邮件正文内容
        self.message.attach(MIMEText('测试报告正文显示','plain','utf-8'))

    def getfile(self):   # 构造附件，获取最新的文件名
        # 获取当前文件的绝对路径+文件名
        abspath = os.path.abspath(__file__)
        # 获取文件所在路径，不加文件名,相当于获取上一个路径
        path = os.path.dirname(abspath)
        # 拼接文件路径
        filepath = os.path.dirname(path) + '\\' + 'report'
        filelist = os.listdir(filepath)
        filedict = {}
        fileTime = []

        # print(filedict)
        for iname in filelist:
            # 拼接文件的路径，
            filename = filepath + '\\' + iname
            # 获取文件的最终修改时间
            time = os.path.getatime(filename)
            fileTime.append(time)
            # 向filedict字典中添加key为time，value为iname
            filedict[time] = iname
        # 获取最大的时间戳
        sendfilekey = max(fileTime)
        # 从filedict字典中提取出时间戳最大的value
        sendfile1 = filedict[sendfilekey]
        # 再次拼接成文件路径
        sendfile = filepath + '\\' + sendfile1
        return sendfile
    #配置邮箱服务器
    def sendemail(self):
        self.config_file()
        try:
            smtpobj = smtplib.SMTP()
            smtpobj.connect(self.host,int(self.emailport))
            # 登录者的账密
            smtpobj.login(self.login,self.password)
            # smtpobj.login('18911032248@163.com','yanjie050301')
            # 发送邮件
            # smtpobj.sendmail('18911032248@163.com','18911032248@163.com',self.message.as_string()) #组成：发件人，收件人，邮件内容，其中发件人和登录人必去为同一个邮箱
            smtpobj.sendmail(self.sender,self.receivers,self.message.as_string())
            print('邮件发送成功')
        except Exception as msg:
            print(msg)
if __name__ =='__main__':
    a = ConfigEmail()
    a.sendemail()

