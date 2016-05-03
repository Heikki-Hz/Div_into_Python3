#!/usr/bin/python3
# -*- coding: utf-8 -*-

a = 'Heikki'
b = 'Python'

print('a + b 的输出结果:', a + b)
print('a * 2 的输出结果:', a * 2 )

if ('H' in a):
    print('H在a中')
else:
    print('H不在a中')

if ('M' in a):
    print('M在a中')
else:
    print('M不在a中')

print(r'\n')
print(R'\n')

#String format
print('Pleaset input your name:')
name = input()
print('Pleaset input your age:')
age = input()
print('我叫%s, 今年%d岁.' % (name, int(age)))

