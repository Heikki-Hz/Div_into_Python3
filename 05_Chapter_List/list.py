#!/usr/bin/python3
# -*- coding: utf-8 -*-

list1 = ['Google', 'Heikki', 2016, 50];
list2 = [1, 2, 3, 4, 5, 6, 7, 8];

print(list1)
print(list1[0])
print(list2[1:])

#更新列表
print('更新列表前', list1)
list1[2] = 200
print('更新列表后', list1)
print('=========================================')

#删除列表元素
print('删除列表前', list1)
del list1[2]
print('删除列表后', list1)

