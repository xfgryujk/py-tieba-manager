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

"""管理登录的贴吧账号
"""

import logging
import os

import trafaret as t

from .tbapi import TbClient, TbError
from .utils.config import Config, OptionalKey
from .utils.singleton import Singleton

_logger = logging.getLogger(__name__)

USER_DIR = os.path.join('data', 'users')
os.makedirs(USER_DIR, exist_ok=True)


class CookieConfig(Config):
    cookie = {OptionalKey(''): t.String}


class UserPool(Singleton):
    """用来管理多账号
    """

    def __init__(self):
        # user_name -> TbClient
        self._clients = {}

    async def init(self):
        """载入保存的账号
        """
        for user_name in os.listdir(USER_DIR):
            if os.path.isdir(os.path.join(USER_DIR, user_name)):
                cookie_config = CookieConfig.from_file(os.path.join(USER_DIR, user_name, 'cookie.json'))
                if not cookie_config.cookie:
                    continue
                try:
                    await self.add_user(cookie_config.cookie)
                except TbError as e:
                    _logger.warning('载入账号"%s"失败，%s', user_name, e)

    async def add_user(self, cookie):
        """添加账号

        :param cookie: cookie字符串或dict或SimpleCookie
        :raise TbError: 添加失败
        """
        client = TbClient(cookie)
        await client.init_user_info()
        self._clients[client.user_name] = client

    def remove_user(self, user_name):
        """删除账号
        """
        try:
            del self._clients[user_name]
        except ValueError:
            pass

    # TODO get_user
