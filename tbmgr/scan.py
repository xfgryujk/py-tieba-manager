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
from asyncio import ensure_future, CancelledError, sleep
from datetime import datetime

from .users import UserPool

_logger = logging.getLogger(__name__)


class TiebaScanner:
    """负责扫描一个贴吧
    """

    def __init__(self, forum_name, min_page, max_page, interval):
        """
        :param forum_name: 贴吧名
        :param min_page: 最小页数
        :param max_page: 最大页数
        :param interval: 最小扫描间隔时间（秒）
        """
        self._forum_name = forum_name
        self.min_page = min_page
        self.max_page = max_page
        self.interval = interval
        self._future = None

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
                start_time = datetime.now()
                await self._scan_once()
                await sleep(max(0, self.interval - (datetime.now() - start_time).seconds))
        except CancelledError:
            pass

    async def _scan_once(self):
        # TODO 扫描贴吧
        client = UserPool.get_instance().get_user_for_crawling()
