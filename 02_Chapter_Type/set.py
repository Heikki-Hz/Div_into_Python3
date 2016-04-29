#!/usr/bin/env python3
# -*- coding: utf-8 -*-

student = {'Tom', 'Heikki', 'Jam', 'Jack', 'Tom', 'Rose'}

print(student) #输出集合，重复的元素会被过滤掉

if ('Rose' in student) :
    print('Rose 在集合')
else :
    print('Rose 不在集合')

#set可以进行集合运算
a = set('abcabcabc')
b = set('cdecdecde')
print(a)
print(b)
print(a - b) #差集
print(a | b) #并集
print(a & b) #交集  
print(a ^ b) #两个集合中不同时存在的元素
