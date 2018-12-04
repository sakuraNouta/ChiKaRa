import os
import sys
import re

'''
扫描文件夹下所有.md文件(包括子文件夹下的)
以关键字(包括英文大小写)查找md文件内容,
'''

def findFile(path):
    f = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.find('.md') != -1:
                f.append(os.path.join(root,file))
                # print(os.path.join(root,file))
    return f
            

def findstr(file, str):
    s = "";
    i = 4 # line index
    for line in open(file,encoding='UTF-8'):
        # 返回包含span位置的对象
        o = re.search(str, line, re.I)
        if  o != None:
            index = o.span()[0]
            start = index-10 if index-10>0 else 0
            s = file.split('\\')[-1] + "----->line:%d" % (i) + "---->" + line[start:index+10]
            print(s)
        i = i + 1
    return s

path = r'..'
while(True):
    key = input("请输入关键字:")
    files = findFile(path)
    for file in files:
        findstr(file,key)


