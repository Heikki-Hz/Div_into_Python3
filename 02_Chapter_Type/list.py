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

#���ַ�����ͬ���ǣ�list�е�Ԫ���ǿ��Ըı��
print('change value of list')

list[0] = 9
print('list[0] = 9.', 'The list is :',list)
list[2:5] = [2,3,5]
print('list[2:5] = [].', 'The list is :',list)
#ɾ��
list[2:5] = []
print('list[2:5] = [].', 'The list is :',list)

