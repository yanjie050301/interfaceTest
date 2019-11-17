#coding:utf-8
import os
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
    filename = filepath + '\\'+ iname
    # 获取文件的最终修改时间
    time = os.path.getatime(filename)
    fileTime.append(time)
    # 向filedict字典中添加key为time，value为iname
    filedict[time] = iname
#获取最大的时间戳
sendfilekey = max(fileTime)
# 从filedict字典中提取出时间戳最大的value
sendfile = filedict[sendfilekey]
# 再次拼接成文件路径
sendfile = filepath + '\\' +sendfile
print(sendfile)

