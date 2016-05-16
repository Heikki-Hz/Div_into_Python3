#!/usr/bin/python3
# -*- coding: utf-8 -*-

dict1 = {'Name': 'Hekikki', 'Age': '25', 'Class': 'First'}

print(dict1['Name'])
print(dict1['Age'])

#访问字典里没有的数据，会报错
#print(dict1['Tom'])

#修改字典
dict1['Age'] = 29
print('修改年龄后:', dict1['Age'])

#删除字典
