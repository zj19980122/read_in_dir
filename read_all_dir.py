#coding:utf-8
import os
import codecs

#读取文件夹下所有txt文件并且合并成一个txt
def read_dir_all(path):
    dir_list = os.listdir(path)
    content = []  # 用content存储合并结果
    for i in dir_list:
        data=open('\\'.join([path, i]),'rb').read()
        content.append(data.decode('utf-8'))
    str='\n'.join(content)
    f=open('fin.txt','w')
    f.write(str)
read_dir_all("C:/Users/17965/Desktop/RUBBISH/python/data")