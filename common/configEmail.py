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
sender = '18911032248@163.com' #发送邮箱
receivers = 'rainshine1190@126.com,18911032248@163.com' #接收邮箱
# 创建一个附件实例
message = MIMEMultipart()
message['From'] = Header('附件','utf-8')# 发送者
message['To'] = Header('测试','utf-8') #接收者
subject = '自动化测试报告'
message['Subject'] = Header(subject,'utf-8')#发送邮件的标题
# 邮件正文内容
message.attach(MIMEText('测试报告正文显示','plain','utf-8'))
# 构造附件，
# 文件的路径
filepath = 'F:\\test\\code\\interfaceTest\\testCase\\2019-11-10-16-29-52.html'
openf = open(filepath,'rb').read()
# 配置附件
att = MIMEText((openf),'plain','utf-8')
att['Content=Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment;filename = "2019-11-10-16-29-52.html"'# 给发送的附件命名
message.attach(att)
#配置邮箱服务器
smtpobj = smtplib.SMTP()
smtpobj.connect('smtp.163.com',25)
# 发件人的账密
smtpobj.login('18911032248@163.com','yanjie050301')
# 发送邮件
smtpobj.sendmail(sender,receivers,message.as_string())
print('邮件发送成功')


