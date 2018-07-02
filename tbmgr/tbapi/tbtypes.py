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

import html
import io
import logging
from datetime import datetime
from enum import IntEnum
from typing import Sequence, Union

from .pyprotos.tbclient.Abstract_pb2 import Abstract
from .pyprotos.tbclient.Media_pb2 import Media
from .pyprotos.tbclient.PbContent_pb2 import PbContent
from .pyprotos.tbclient.Post_pb2 import Post as RawPost
from .pyprotos.tbclient.SubPostList_pb2 import SubPostList as RawSubPost
from .pyprotos.tbclient.ThreadInfo_pb2 import ThreadInfo as RawThread
from .pyprotos.tbclient.User_pb2 import User

_logger = logging.getLogger(__name__)


class ContentType(IntEnum):
    TEXT = 0
    LINK = 1
    EMOTION = 2
    IMAGE = 3
    AT = 4
    VIDEO = 5
    VOICE = 10


class AbstractPost:
    """抽象帖子，可代表主题、帖子、评论
    """

    PORTRAIT_URL_PREFIX = 'http://tb.himg.baidu.com/sys/portrait/item/'

    @property
    def tid(self):
        raise NotImplementedError

    @property
    def author_id(self):
        raise NotImplementedError

    @property
    def author_name(self):
        raise NotImplementedError

    @property
    def author_show_name(self):
        raise NotImplementedError

    @property
    def author_portrait_url(self):
        raise NotImplementedError

    @property
    def create_time(self) -> datetime:
        raise NotImplementedError

    @property
    def html_content(self):
        raise NotImplementedError


def _html_escape(text):
    return html.escape(text).replace('\n', '<br>')


def _pb_content_to_html(pb_content: Sequence[Union[PbContent, Abstract]]):
    buffer = io.StringIO()
    for content in pb_content:
        if content.type == ContentType.TEXT:
            buffer.write(_html_escape(content.text))
        elif content.type == ContentType.LINK:
            buffer.write(f'<a href="{content.link}" target="_blank">{_html_escape(content.text)}</a>')
        elif content.type == ContentType.EMOTION:
            buffer.write(f'<img class="BDE_Smiley" width="30" height="30" changedsize="false" '
                         f'src="http://static.tieba.baidu.com/tb/editor/images/client/{content.text}.png" >')
        elif content.type == ContentType.IMAGE:
            if content.bsize:
                width, height = content.bsize.split(',')
            else:
                width, height = content.width, content.height
            buffer.write(f'<img class="BDE_Image" pic_type="0" width="{width}" height="{height}" '
                         f'src="{content.src}" >')
        elif content.type == ContentType.AT:
            buffer.write(f"""<a href=""  onclick="Stats.sendRequest('fr=tb0_forum&st_mod=pb&st_value=atlink');" """
                         f'onmouseover="showattip(this)" onmouseout="hideattip(this)" username='
                         f'"{content.text[1:]}" target="_blank" class="at">{content.text}</a>')
        elif content.type == ContentType.VIDEO:
            buffer.write(f'<embed class="BDE_Flash" type="application/x-shockwave-flash" pluginspage="'
                         f'http://www.macromedia.com/go/getflashplayer" wmode="transparent" play="true" '
                         f'loop="false" menu="false" src="{content.text}" width="500" height="450" '
                         f'allowscriptaccess="never" allowfullscreen="true" scale="noborder">')
        elif content.type == ContentType.VOICE:
            buffer.write(f'<div class="voice_player voice_player_pb"><a href="#" class="voice_player_inner">'
                         f'<span class="before">&nbsp;</span><span class="middle"><span class="speaker '
                         f'speaker_animate">&nbsp;</span><span class="time"><span class="second">'
                         f'{content.during_time}</span>&quot;</span></span><span class="after">&nbsp;</span></a>'
                         f'</div><img class="j_voice_ad_gif" src="http://tb2.bdstatic.com/tb/static-pb/img/voice_ad'
                         f'.gif" alt="下载贴吧客户端发语音！" /><br/>')
        else:
            _logger.warning('未知的PbContent类型：%d\n%s', content.type, content)
    return buffer.getvalue()


def _media_to_html(media: Sequence[Media]):
    buffer = io.StringIO()
    for content in media:
        if content.type == ContentType.IMAGE:
            buffer.write(f'<img src="{content.big_pic}" class="threadlist_pic j_m_pic " />')
        elif content.type == ContentType.VIDEO:
            # 旧版视频摘要，目前已无法获取信息
            buffer.write(f'<img src="" class="threadlist_btn_play j_m_flash " />')
        else:
            _logger.warning('未知的Media类型：%d\n%s', content.type, content)
    return buffer.getvalue()


class Thread(AbstractPost):
    """主题，在贴吧首页能看到的那些东西，包括标题、摘要等
    """

    def __init__(self, raw: RawThread):
        self._raw = raw
        self._abstract = None
        self._html_content = None

    def __repr__(self):
        return f'<Thread id={self.tid} {self.author_show_name} {self.html_content}>'

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
        if self._html_content is None:
            self._html_content = '<br>'.join((
                _html_escape(self._raw.title),
                self.abstract
            ))
        return self._html_content

    @property
    def title(self):
        return self._raw.title

    @property
    def abstract(self):
        if self._abstract is None:
            self._abstract = _pb_content_to_html(self._raw._abstract)
            # 多媒体
            if self._raw.media:
                self._abstract = '<br>'.join((
                    self._abstract,
                    _media_to_html(self._raw.media)
                ))
            # 新版视频摘要
            if self._raw.video_info.video_url:
                self._abstract = '<br>'.join((
                    self._abstract,
                    f'<img src="{self._raw.video_info.thumbnail_url}" class="threadlist_btn_play j_m_flash " />'
                ))
        return self._abstract

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
        self._html_content = None

    def __repr__(self):
        return f'<Post id={self.pid} floor={self.floor} {self.author_show_name} {self.html_content}>'

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
        if self._html_content is None:
            self._html_content = _pb_content_to_html(self._raw.content)
            # 小尾巴
            if self._raw.signature.content:
                self._html_content = '<hr>'.join((
                    self._html_content,
                    _pb_content_to_html(self._raw.signature.content)
                ))
        return self._html_content

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
        self._html_content = None

    def __repr__(self):
        return f'<SubPost id={self.cid} {self.author_show_name} {self.html_content}>'

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
        if self._html_content is None:
            self._html_content = _pb_content_to_html(self._raw.content)
        return self._html_content

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
