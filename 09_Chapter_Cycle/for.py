#!/usr/bin/python3
# -*- coding: utf-8 -*-

sites = ['Tom', 'Heikki', 'Google', 'Baidu']

for site in sites:
    if site == 'Google':
        print("菜鸟教程")
        break
    print("循环数据" + site)
else:
    print("没有循环数据")

print('完成循环')

