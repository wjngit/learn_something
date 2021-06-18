# -*- coding: utf-8 -*-

"""
@Time    : 2021/4/23 4:58 下午
@Author  : Garner
@File    : decorator.py
"""
from functools import wraps


def b(num):
    def a(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print(123 + i)
            func(*args, **kwargs)

        return wrapper

    return a


@b(3)
def c(aaa):
    print(aaa)


c(666)


def my_decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)

    return wrapper


def my_decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)

    return wrapper


@my_decorator1
@my_decorator2
def greet(message):
    print(message)


greet(666)


def a(func):
    def b(*args, **kwargs):
        print(123)
        func(*args, **kwargs)

    return b


@a
def aaa(a=1, b=2):
    print(f'{a}-{b}')


aaa(3, 4)
