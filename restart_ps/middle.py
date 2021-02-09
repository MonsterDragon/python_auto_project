#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from cls_shell.pro import UseShell

# transfer shell to obtain ips
def func(param):
    print(os.path.abspath(__file__))
    exshell = UseShell(param)
    exshell()


def iplist(param):
    ipdict = {}
    log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/log/{}.log'.format(param)
    with open(log_path, 'r') as l:
        # iplist = [line.split(':')[0] for line in l if line.strip()]
        for line in l:
            if line.strip():
                print(line)
                ipdict[line.split(':')[0]] = line.split(':')[1].strip()
        return ipdict


if __name__ == "__main__":
    func('p1')
    iplist('p1')
