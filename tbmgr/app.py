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
from .events import AskExitEvent, CleanupEvent, BeforeExitEvent
from .users import UserPool
from .utils import database
from .utils import logging as tbmlogging
from .utils.event import post_event, async_post_event
from .utils.singleton import Singleton

_logger = logging.getLogger(__name__)


class TiebaManager(Singleton):
    """贴吧管理器主程序
    """

    def __init__(self):
        self._is_exiting = False

    def main(self):
        """初始化顺序很重要，不能乱改
        """
        # 初始化异常处理
        sys.excepthook = self._except_hook
        # 初始化日志模块
        tbmlogging.init()
        # 初始化配置
        configs.init()
        # 初始化数据库
        database.init()
        # 初始化账号
        ensure_future(UserPool.get_instance().init())
        # 初始化信号处理
        loop = get_event_loop()
        try:
            loop.add_signal_handler(signal.SIGINT, self.exit)
            loop.add_signal_handler(signal.SIGTERM, self.exit)
        except NotImplementedError:
            # Windows中loop.add_signal_handler()未实现
            signal.signal(signal.SIGINT, lambda signum, frame: loop.call_soon(self.exit))
            signal.signal(signal.SIGTERM, lambda signum, frame: loop.call_soon(self.exit))
        # 启动web UI服务器和事件循环
        webui.serve_forever()

        # 退出
        post_event(BeforeExitEvent())
        sys.exit()

    @property
    def is_exiting(self):
        """已收到退出信号，正在进行退出前清理
        """
        return self._is_exiting

    def exit(self):
        """退出本程序

        一般在用户按下Ctrl + C（收到SIGINT）或收到SIGTERM时调用
        在Windows中事件循环会阻塞在select()，直到有新的事件（比如网络传输）才会收到信号
        """
        _logger.warning('收到退出信号')
        if self._is_exiting:
            return
        if not post_event(AskExitEvent()):
            _logger.warning('退出请求被取消')
            return
        self._is_exiting = True
        ensure_future(self._cleanup())

    @staticmethod
    async def _cleanup():
        """退出前清理
        """
        _logger.warning('正在进行退出前清理')
        await async_post_event(CleanupEvent())
        # 保存账号
        await UserPool.get_instance().uninit()
        # 停止事件循环
        loop = get_event_loop()
        loop.call_soon(loop.stop)

    @staticmethod
    def _except_hook(type_, value, traceback):
        """异常处理hook，见sys.excepthook
        """
        _logger.exception('遇到未处理的异常，请将以下信息发到xfgryujk@126.com帮助调试：', exc_info=value)
        sys.__excepthook__(type_, value, traceback)
