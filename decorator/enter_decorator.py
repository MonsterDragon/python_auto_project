#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import time

def timing(func):
    def wrapped_func(*args):
        while True:
            func(*args)
            time.sleep(1200)
    return wrapped_func

@timing
def fun(a):
    print(a)

if __name__ == "__main__":
    fun(1)
