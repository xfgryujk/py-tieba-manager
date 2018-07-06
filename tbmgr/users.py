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
from typing import Dict, List

import trafaret as t

from .tbapi import TbClient, TbError
from .utils.config import Config, OptionalKey
from .utils.singleton import Singleton

_logger = logging.getLogger(__name__)

USER_DIR = os.path.join('data', 'configs', 'users')
os.makedirs(USER_DIR, exist_ok=True)


class CookieConfig(Config):
    cookie = {OptionalKey(''): t.String}


class UserPool(Singleton):
    """用来管理多账号
    """

    def __init__(self):
        # user_name -> TbClient
        self._clients: Dict[str, TbClient] = {}
        self._clients_for_crawling: List[TbClient] = []

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

    async def uninit(self):
        """保存账号，关闭client
        """
        for client in self._clients.values():
            os.makedirs(os.path.join(USER_DIR, client.user_name), exist_ok=True)
            CookieConfig(cookie=client.cookie_str
                         ).save(os.path.join(USER_DIR, client.user_name, 'cookie.json'))
            await client.close()
        self._clients.clear()
        self._clients_for_crawling.clear()

    async def add_user(self, cookie):
        """添加账号

        :param cookie: cookie字符串或dict或SimpleCookie
        :raise TbError: 添加失败
        """
        client = TbClient(cookie)
        await client.init_user_info()
        self._clients[client.user_name] = client
        self._clients_for_crawling.append(client)

    def remove_user(self, user_name):
        """删除账号
        """
        try:
            client = self._clients[user_name]
            del self._clients[user_name]
            self._clients_for_crawling.remove(client)
        except (KeyError, ValueError):
            pass

    def get_user_for_crawling(self):
        """
        :return: 用来爬数据的账号
        """
        client = self._clients_for_crawling.pop(0)
        self._clients_for_crawling.append(client)
        return client

    # TODO get_user_for_operating
