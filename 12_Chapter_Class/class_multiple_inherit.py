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

class Student(People):
    grade = ' '
    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print('%s 说：我 %d岁了,我在读%d年级.' % (self.name,  
            self.age, self.grade))

class Speaker():
    topic = ' '
    name  = ' '
    
    def __init__(self, n, t):
        self.name  = n
        self.topic = t
    
    def speaker(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,
            self.topic))

class sample(Speaker, Student):
    a = ' '
    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)

test = sample("Heikki", 25, 70, 4, "Python3")
test.speak()
test.speaker()

