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

"""贴吧数据类型的封装
"""

from datetime import datetime

from .pyprotos.tbclient.Post_pb2 import Post as RawPost
from .pyprotos.tbclient.SubPostList_pb2 import SubPostList as RawSubPost
from .pyprotos.tbclient.ThreadInfo_pb2 import ThreadInfo as RawThread
from .pyprotos.tbclient.User_pb2 import User


class AbstractPost:
    """抽象帖子，可代表主题、帖子、评论
    """

    PORTRAIT_URL_PREFIX = 'http://tb.himg.baidu.com/sys/portrait/item/'

    @property
    def tid(self):
        raise NotImplemented

    @property
    def author_id(self):
        raise NotImplemented

    @property
    def author_name(self):
        raise NotImplemented

    @property
    def author_show_name(self):
        raise NotImplemented

    @property
    def author_portrait_url(self):
        raise NotImplemented

    @property
    def create_time(self) -> datetime:
        raise NotImplemented

    @property
    def html_content(self):
        raise NotImplemented


class Thread(AbstractPost):
    """主题，在贴吧首页能看到的那些东西，包括标题、摘要等
    """

    def __init__(self, raw: RawThread):
        self._raw = raw

    def __repr__(self):
        return f'<Thread id={self.tid} {self.author_show_name} - {self.title}>'

    @property
    def raw(self):
        return self._raw

    @property
    def tid(self):
        return self._raw.id

    @property
    def author_id(self):
        return self._raw.author.id

    @property
    def author_name(self):
        return self._raw.author.name

    @property
    def author_show_name(self):
        return self._raw.author.name_show

    @property
    def author_portrait_url(self):
        return self.PORTRAIT_URL_PREFIX + self._raw.author.portrait

    @property
    def create_time(self) -> datetime:
        return datetime.fromtimestamp(self._raw.create_time)

    @property
    def html_content(self):
        # TODO 解析内容
        raise NotImplemented

    @property
    def title(self):
        return self._raw.title

    @property
    def abstract(self):
        # TODO 解析摘要
        raise NotImplemented

    @property
    def last_responder_id(self):
        return self._raw.last_replyer.id

    @property
    def last_responder_name(self):
        return self._raw.last_replyer.name

    @property
    def last_responder_show_name(self):
        return self._raw.last_replyer.name_show

    @property
    def n_reply(self):
        return self._raw.reply_num


class Post(AbstractPost):
    """帖子，对主题的回复
    """

    def __init__(self, raw: RawPost, tid, author: User):
        self._raw = raw
        self._tid = tid
        self._author = author

    def __repr__(self):
        # TODO 添加内容
        return f'<Post id={self.pid} floor={self.floor} {self.author_show_name}>'

    @property
    def raw(self):
        return self._raw

    @property
    def tid(self):
        return self._tid

    @property
    def author_id(self):
        return self._author.id

    @property
    def author_name(self):
        return self._author.name

    @property
    def author_show_name(self):
        return self._author.name_show

    @property
    def author_portrait_url(self):
        return self.PORTRAIT_URL_PREFIX + self._author.portrait

    @property
    def create_time(self) -> datetime:
        return datetime.fromtimestamp(self._raw.time)

    @property
    def html_content(self):
        # TODO 解析内容
        raise NotImplemented

    @property
    def pid(self):
        return self._raw.id

    @property
    def floor(self):
        return self._raw.floor

    @property
    def author_level(self):
        return self._author.level_id

    @property
    def n_sub_posts(self):
        return self._raw.sub_post_number


class SubPost(AbstractPost):
    """评论，对帖子的回复，以前叫楼中楼
    """

    def __init__(self, raw: RawSubPost, tid, pid, post_floor, author: User):
        self._raw = raw
        self._tid = tid
        self._pid = pid
        self._post_floor = post_floor
        self._author = author

    def __repr__(self):
        # TODO 添加内容
        return f'<SubPost id={self.cid} {self.author_show_name}>'

    @property
    def raw(self):
        return self._raw

    @property
    def tid(self):
        return self._tid

    @property
    def author_id(self):
        return self._author.id

    @property
    def author_name(self):
        return self._author.name

    @property
    def author_show_name(self):
        return self._author.name_show

    @property
    def author_portrait_url(self):
        return self.PORTRAIT_URL_PREFIX + self._author.portrait

    @property
    def create_time(self) -> datetime:
        return datetime.fromtimestamp(self._raw.time)

    @property
    def html_content(self):
        # TODO 解析内容
        raise NotImplemented

    @property
    def cid(self):
        return self._raw.id

    @property
    def pid(self):
        return self._pid

    @property
    def post_floor(self):
        return self._post_floor

    @property
    def author_level(self):
        return self._author.level_id
