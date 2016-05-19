#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

list = [1, 2, 3, 4]
it = iter(list)

for n in it:
    print(n)

print("--------------")

iteration = iter(list)

while True:
    try:
        print(next(iteration))
    except StopIteration:
        sys.exit()

