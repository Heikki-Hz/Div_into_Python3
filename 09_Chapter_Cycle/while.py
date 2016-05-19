#!/usr/bin/python3
# -*- coding: utf-8 -*-

num  = 100
count = 1
sum = 0

while count <= num:
    sum = sum + count
    count += 1
print('1~%d = %d' %(num, sum))


count = 0
while count < 5:
    print(count, " < 5")
    count += 1
else:
    print(count, " >= 5")


