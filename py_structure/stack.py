#!/usr/bin/env python3
#-*- coding:utf-8 -*-


class Stack(object):
    """python to make stack"""

    def __init__(self):
        self.items = []

    def is_empty(sefl):
        return self.items == []

    def top(self):
        return self.items[len(self.items) - 1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
