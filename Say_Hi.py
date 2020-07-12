#!/usr/bin/env python
# -*- coding:utf-8 -*-

def say_hi(name, age):
    return "Hi. My name is {} and I'm {} years old".format(name, age)
    #return "Hi. My name is " + name + " and I'm " + str(age) + " years old"
    #return f"Hi. My name is {name} and I'm {age} years old"

if __name__ == '__main__':
    print(say_hi("Alex", 34))

