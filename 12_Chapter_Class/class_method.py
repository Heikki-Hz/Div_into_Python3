#!/usr/bin/python3
# -*- coding: utf-8 -*-


class People():
    name = ' '
    age  = 0

    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age  = a

        self.__weight = w

    def speak(self):
        print('%s 说：我 %d岁了。' % (self.name, self.age))


p = People('Heikki', 10, 27);

p.speak()
