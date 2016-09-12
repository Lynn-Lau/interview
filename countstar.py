# -*- coding:utf-8 -*-

# rerange the string from Alibaba
# Author: Lynn Lau
# Date: 2016/08/12

def countstar(data):
    datalst = list()
    starlst = list()
    charlst = list()
    for char in data:
        datalst.append(char)
    for i in range(0, len(datalst)):
        if datalst[i] == '*':
            starlst.append(datalst[i])
        else:
            charlst.append(datalst[i])
        i = i + 1
    stars = ''.join(starlst)
    chars = ''.join(charlst)
    string = stars + chars
    print len(starlst)
    print string

data = raw_input()
result = countstar(data)
