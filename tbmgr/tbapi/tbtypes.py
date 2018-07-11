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

import logging
from abc import abstractmethod
from datetime import datetime

from .pyprotos.tbclient.Post_pb2 import Post as RawPost
from .pyprotos.tbclient.SubPostList_pb2 import SubPostList as RawSubPost
from .pyprotos.tbclient.ThreadInfo_pb2 import ThreadInfo as RawThread
from .pyprotos.tbclient.User_pb2 import User
from .utils import html_escape, pb_content_to_html, media_to_html, cached

_logger = logging.getLogger(__name__)


class AbstractPost:
    """抽象帖子，可代表主题、帖子、评论
    """

    PORTRAIT_URL_PREFIX = 'http://tb.himg.baidu.com/sys/portrait/item/'

    @property
    @abstractmethod
    def tid(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def author_id(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def author_name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def author_show_name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def author_portrait_url(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def create_time(self) -> datetime:
        raise NotImplementedError

    @property
    @abstractmethod
    def html_content(self):
        raise NotImplementedError


class IThread(AbstractPost):
    """主题，在贴吧首页能看到的那些东西，包括标题、摘要等
    """

    def __repr__(self):
        return f'<{type(self).__name__} id={self.tid} {self.author_show_name} {self.html_content}>'

    @property
    @cached
    def html_content(self):
        return '<br>'.join((
            self.title,
            self.abstract
        ))

    @property
    @abstractmethod
    def title(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def abstract(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def last_responder_id(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def last_responder_name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def last_responder_show_name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def n_reply(self):
        raise NotImplementedError


class IPost(AbstractPost):
    """帖子，对主题的回复
    """

    def __repr__(self):
        return f'<{type(self).__name__} id={self.pid} floor={self.floor} {self.author_show_name} {self.html_content}>'

    @property
    @abstractmethod
    def pid(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def floor(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def author_level(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def n_sub_posts(self):
        raise NotImplementedError


class ISubPost(AbstractPost):
    """评论，对帖子的回复，以前叫楼中楼
    """

    def __repr__(self):
        return f'<{type(self).__name__} id={self.cid} {self.author_show_name} {self.html_content}>'

    @property
    @abstractmethod
    def cid(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def pid(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def post_floor(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def author_level(self):
        raise NotImplementedError


class Thread(IThread):
    """主题，在贴吧首页能看到的那些东西，包括标题、摘要等
    """

    def __init__(self, raw: RawThread):
        self._raw = raw

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
    @cached
    def title(self):
        return html_escape(self._raw.title)

    @property
    @cached
    def abstract(self):
        result = pb_content_to_html(self._raw._abstract)  # 我也不知道为什么百度要在前面加个下划线
        # 多媒体
        if self._raw.media:
            result = '<br>'.join((
                result,
                media_to_html(self._raw.media)
            ))
        # 新版视频摘要
        if self._raw.video_info.video_url:
            result = '<br>'.join((
                result,
                f'<img src="{self._raw.video_info.thumbnail_url}" class="threadlist_btn_play j_m_flash " />'
            ))
        return result

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


class Post(IPost):
    """帖子，对主题的回复
    """

    def __init__(self, raw: RawPost, tid, author: User):
        self._raw = raw
        self._tid = tid
        self._author = author

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
    @cached
    def html_content(self):
        result = pb_content_to_html(self._raw.content)
        # 小尾巴
        if self._raw.signature.content:
            result = '<hr>'.join((
                result,
                pb_content_to_html(self._raw.signature.content)
            ))
        return result

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
    @cached
    def html_content(self):
        return pb_content_to_html(self._raw.content)

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
