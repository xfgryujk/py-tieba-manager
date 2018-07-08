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

"""扫描帖子模块
"""

import logging
import time
from asyncio import ensure_future, CancelledError, sleep

from .users import UserPool

_logger = logging.getLogger(__name__)


class Scanner:
    pass


class ThreadScanner(Scanner):
    pass


class ForumScanner(Scanner):
    pass


class ScanningTask:

    def __init__(self, interval=None):
        """
        :param interval: 最小扫描间隔时间（秒），None表示自动计算
        """
        self.interval = interval
        self._future = None
        # 本次扫描出现的新帖数，用来计算间隔时间
        self._n_new_posts = 0

    @property
    def is_running(self):
        return self._future is not None

    def start(self):
        if self._future is None:
            self._future = ensure_future(self._scan_forever())
            self._future.add_done_callback(self.__on_done)

    def __on_done(self):
        self._future = None

    def stop(self):
        if self._future is not None:
            self._future.cancel()

    async def _scan_forever(self):
        try:
            while True:
                start_time = time.time()
                self._n_new_posts = 0
                await self._scan_once()
                cost_time = time.time() - start_time

                if self.interval is None:
                    # 平均间隔时间 = 扫描时间 / 新帖数，最多1分钟
                    min_seconds_to_wait = 60 if self._n_new_posts == 0 else max(60., cost_time / self._n_new_posts)
                else:
                    min_seconds_to_wait = self.interval - cost_time
                await sleep(max(0, min_seconds_to_wait))
        except CancelledError:
            pass

    async def _scan_once(self):
        raise NotImplementedError


class ThreadScanningTask(ScanningTask):
    """负责扫描一个主题
    """

    def __init__(self, fid, tid, min_page=None, max_page=None, interval=None):
        """
        :param fid: 贴吧ID
        :param tid: 主题ID
        :param min_page: 最小页数，None表示1
        :param max_page: 最大页数，None表示扫描到最后一页
        :param interval: 最小扫描间隔时间（秒），None表示自动计算
        """
        super().__init__(interval)

    async def _scan_once(self):
        # TODO 扫描主题
        client = UserPool.get_instance().get_user_for_crawling()


class ForumScanningTask(ScanningTask):
    """负责扫描一个贴吧，可以有多个扫描任务扫描同一个贴吧
    """

    def __init__(self, forum_name, min_page=None, max_page=None, interval=None):
        """
        :param forum_name: 贴吧名
        :param min_page: 最小页数，None表示1
        :param max_page: 最大页数，None表示扫描到最后一页
        :param interval: 最小扫描间隔时间（秒），None表示自动计算
        """
        super().__init__(interval)

    async def _scan_once(self):
        # TODO 扫描贴吧
        client = UserPool.get_instance().get_user_for_crawling()
