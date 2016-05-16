#!/usr/bin/python3
#-*- coding:utf-8 -*-

age = int(input("Please enter your dog's age:"))

if age < 0:
    print("Are you kiding me?")
elif age == 1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("相当于%d岁的人" % human)
