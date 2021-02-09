#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 2021/2/9 by shuzhan


"""
statement:
    This is the entrance file for all the program
    Do everything by the prompt
"""

import sys
import os
from multiprocessing import Pool


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from decorator import enter_decorator
from restart_ps.Moudle_log import logger
from restart_ps import middle
from restart_ps import ssh_route


usage_str = """
Usage:
    execute single process by p1 or p2 or c2 -- ./enter.py p1|p2|c2
    execute all of processes by p1 and p2 and c2 -- ./enter.py p1 p2 c2
"""


process_str = "./enter.py p1 p2 c2"


# create log file
# if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/check.log"):
#     os.remove(os.path.dirname(os.path.abspath(__file__)) + "/check.log")
# else:
#     os.mknod(os.path.dirname(os.path.abspath(__file__)) + "/check.log")


def main_single(param):
    logger.info("start execute {}".format(param))
    middle.func(param)
    target_dict = middle.iplist(param)
    pool = Pool(processes = 5)
    logger.info("remote machines {}".format(target_dict))
    for i in target_dict:
        pool.apply_async(ssh_route.transfer, (i, target_dict[i], ))
    pool.close()
    pool.join()


@enter_decorator.timing
def main_triple(*args):
    for i in args:
        main_single(i)
    logger.info("all processes finished, executed successfully!")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] in process_str:
        logger.info("single process ready to start {}".format(sys.argv[1]))
        main_triple(sys.argv[1])
    elif len(sys.argv) == 4 and any(ele in process_str for ele in sys.argv):
        logger.info("trible process ready to start {} {} {}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
        main_triple(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        logger.error("wrong parameters! Please use one parameter or three parameters!")
        print(usage_str)

