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

"""提供高级的贴吧API
"""

from typing import List, Tuple

from .tbclient import BanDuration, TbClient
from .tbtypes import Thread, Post, SubPost
from ..utils.database import OrmBase


class OrmThread(Thread, OrmBase):
    pass


class OrmPost(Post, OrmBase):
    pass


class OrmSubPost(SubPost, OrmBase):
    pass


class TbClientWrapper(TbClient):
    """带缓存、错误处理、事件、白名单和日志等功能的贴吧API封装
    """

    async def get_threads(self, forum_name, page=1) -> List[Thread]:
        pass

    async def get_posts(self, fid, tid, page=1, with_sub_post=False
                        ) -> Tuple[List[Post], List[List[SubPost]]]:
        pass

    async def get_sub_posts(self, tid, pid, page=1) -> List[SubPost]:
        pass

    async def ban_user(self, fid, forum_name, user_name, duration: BanDuration,
                       reason=''):
        pass

    async def add_black_list(self, forum_name, user_id):
        pass

    async def delete_thread(self, fid, forum_name, tid):
        pass

    async def delete_post(self, fid, forum_name, tid, pid):
        pass

    async def delete_sub_post(self, fid, forum_name, tid, cid):
        pass
