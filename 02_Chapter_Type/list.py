#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list = ['abcd', 222, 2.23, 'Heikki', 21.2]
tinylist = ['Heikki', 123]

print(list)
print(list[0])
print(list[2:])
print(list[2:4])
print(list[3:-1])
print(tinylist*2)
print(tinylist + list)

#与字符串不同的是，list中的元素是可以改变的
print('change value of list')

list[0] = 9
print('list[0] = 9.', 'The list is :',list)
list[2:5] = [2,3,5]
print('list[2:5] = [].', 'The list is :',list)
#删除
list[2:5] = []
print('list[2:5] = [].', 'The list is :',list)

