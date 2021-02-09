#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import subprocess
import os
import re

from py_structure.stack import Stack
from Moudle_log import logger


datepattern = re.compile(r'(?P<hour>\d+h)?(?P<min>\d+m)?(?P<sec>\d+.?\d+s)')

def get_timeout(stack):
    runlist = []
    timeout_list = []
    for i in range(len(stack.items)):
        if "running" in stack.top():
            runlist.append(stack.pop().split())
    for ele in runlist:
        if datepattern.match(ele[len(ele)-1]).group('min'):
            timeout_list.append(ele)
    timeout_list = [ele for ele in timeout_list if int(datepattern.match(ele[len(ele)-1]).group('min')[:-1]) > 25]
    print(timeout_list)
    return timeout_list


def check_sealer():
    res = subprocess.check_output('source /etc/profile && lotus-sealer  sealing jobs | grep  PC2', shell=True)
    res_list = res.decode('utf-8').split('\n')
    sealer_stack = Stack()
    for i in res_list:
        sealer_stack.push(i)
    sealer_stack.items.reverse()
    return sealer_stack


def main():
    res_stack = check_sealer()
    get_timeout(res_stack)


if __name__ == "__main__":
    main()
