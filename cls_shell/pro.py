#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os


class UseShell(object):
    # sh_file = "/home/shuzhan/tt/timeout.sh"
    sh_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/restart_ps/timeout.sh'
    print('sh_file {}'.format(sh_file))

    def __init__(self, name):
        self.name = name

    def __call__(self):
        os.system(UseShell.sh_file + ' {}'.format(self.name))
