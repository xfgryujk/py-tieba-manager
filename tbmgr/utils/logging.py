# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 xfgryujk <xfgryujk@126.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""日志模块
"""

import logging
import os
import sys
from logging import getLogger, Formatter, Handler, StreamHandler, LogRecord
from logging.handlers import RotatingFileHandler
from time import strftime
from typing import List, Union

LOG_DIR = os.path.join('data', 'log')
os.makedirs(LOG_DIR, exist_ok=True)

# 最近的日志，新的日志索引小
_logs: List[LogRecord] = []


class _RotatingListHandler(Handler):
    """用list记录最近max_size条日志的Handler
    """

    def __init__(self, list_, max_size=1000):
        super().__init__()
        self._list = list_
        self.max_size = max_size

    def emit(self, record):
        if len(self._list) >= self.max_size:
            del self._list[self.max_size - 1:]
        self._list.insert(0, record)


class _ColoredConsoleHandler(StreamHandler):
    """根据等级记录彩色日志的Handler
    """

    if sys.platform == 'win32':
        # 让Windows控制台支持彩色
        os.system('color >nul 2>nul')

    def __init__(self):
        super().__init__(None)

    def emit(self, record):
        if record.levelno < logging.INFO:
            control_string = '\033[1m'     # 默认
        elif logging.INFO <= record.levelno < logging.WARNING:
            control_string = '\033[1;32m'  # 绿色
        elif logging.WARNING <= record.levelno < logging.ERROR:
            control_string = '\033[1;33m'  # 黄色
        else:
            control_string = '\033[1;31m'  # 红色
        self.stream.write(control_string)
        super().emit(record)
        self.stream.write('\033[0m')


def init():
    """设置根logger
    """
    root_logger = getLogger()
    root_logger.setLevel(logging.DEBUG)
    fmt = Formatter('{asctime} {levelname} [{name}]: {message}', '%Y-%m-%d %H:%M:%S', '{')
    stream_handler = _ColoredConsoleHandler()
    list_handler = _RotatingListHandler(_logs)
    file_handler = RotatingFileHandler(os.path.join(LOG_DIR, strftime('%Y-%m-%d %H.%M.%S') + '.log'),
                                       maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
    for handler, level in ((stream_handler, logging.DEBUG),
                           (list_handler, logging.INFO),
                           (file_handler, logging.INFO)):
        handler.setFormatter(fmt)
        handler.setLevel(level)
        root_logger.addHandler(handler)


def get_logs(index: Union[int, slice]):
    return _logs[index]
