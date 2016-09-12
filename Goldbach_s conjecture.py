# -*- coding:utf-8 -*-

# Goldbach's Conjecture from Tencent's Interview
# Author:Lynn Lau
# Date: 2016/09/12
'''
任何一个大于2的正整数都可以写成两个质数之和,
通过Python验证这一猜想。
'''

import math


def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

primelist = list()
for j in range(2, 1000):
    if isprime(j):
        primelist.append(j)
#print primelist

def sum(data):
    count = 0
    for m in range(0, len(primelist)):
        for n in range(m, len(primelist)):
            if primelist[m] + primelist[n] == data:
                count = count + 1
                print "%d = %d + %d" %(data, primelist[m], primelist[n])


    return count

result = sum(int(raw_input()))
print result
