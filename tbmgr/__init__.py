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

"""主程序
"""

import logging
import signal
import sys
from asyncio import get_event_loop, ensure_future

from . import configs
from . import webui
from .events import TbmExitingEvent
from .utils import logging as tbmlogging
from .utils.event import async_post_event, event_handler

_logger = logging.getLogger(__name__)

_is_exiting = False


def main():
    # 初始化异常处理
    sys.excepthook = _except_hook
    # 初始化日志模块
    tbmlogging.init()
    # 初始化配置
    configs.init()

    # 初始化信号处理
    loop = get_event_loop()
    try:
        loop.add_signal_handler(signal.SIGINT, exit_)
        loop.add_signal_handler(signal.SIGTERM, exit_)
    except NotImplementedError:
        # Windows中loop.add_signal_handler()未实现
        signal.signal(signal.SIGINT, lambda signum, frame: loop.call_soon(exit_))
        signal.signal(signal.SIGTERM, lambda signum, frame: loop.call_soon(exit_))

    # 启动web UI服务器
    webui.serve_forever()


def is_exiting():
    """已收到退出信号，正在进行退出前清理
    """
    return _is_exiting


def exit_():
    """退出本程序

    一般在用户按下Ctrl + C（收到SIGINT）或收到SIGTERM时调用
    在Windows中事件循环会阻塞在select()，直到有新的事件（比如网络传输）才会收到信号
    """
    _logger.warning('收到退出信号')
    global _is_exiting
    if _is_exiting:
        return
    _is_exiting = True
    ensure_future(_cleanup())


async def _cleanup():
    """退出前清理
    """
    _logger.warning('正在进行退出前清理')
    await async_post_event(TbmExitingEvent())
    # 停止事件循环
    loop = get_event_loop()
    loop.call_soon(loop.stop)


def _except_hook(type_, value, traceback):
    """异常处理hook，见sys.excepthook
    """
    _logger.exception('遇到未处理的异常，请将以下信息发到xfgryujk@126.com帮助调试：', exc_info=value)
    sys.__excepthook__(type_, value, traceback)
