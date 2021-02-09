#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import logging, sys, os
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_formatter = logging.Formatter("[%(levelname)s:%(asctime)s %(process)s %(filename)s:%(lineno)d]: %(message)s", "%Y-%m-%d %H:%M:%S")

# 创建日志文件
# if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/socket_server.log"):
#     os.remove(os.path.dirname(os.path.abspath(__file__)) + "/socket_server.log")
# else:
#     os.mknod(os.path.dirname(os.path.abspath(__file__)) + "/socket_server.log")

file_handler = RotatingFileHandler(os.path.dirname(os.path.abspath(__file__)) + "/check.log", "a", 1024 * 1024 * 20, 5)
file_handler.setFormatter(log_formatter)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
