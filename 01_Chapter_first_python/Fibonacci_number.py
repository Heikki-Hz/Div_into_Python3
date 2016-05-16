#!/usr/bin/python3
# -*- coding: utf-8 -*-

a, b = 0, 1

print('Please input an int:')

len = 1000
while (b < len):
    print(b)
    a, b = b, a + b
