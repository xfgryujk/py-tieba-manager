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

"""处理数据的便利函数
"""

import html
import io
import logging
from enum import IntEnum
from functools import wraps
from typing import Sequence, Union

from .pyprotos.tbclient.Abstract_pb2 import Abstract
from .pyprotos.tbclient.Media_pb2 import Media
from .pyprotos.tbclient.PbContent_pb2 import PbContent

_logger = logging.getLogger(__name__)


def html_escape(text):
    return html.escape(text).replace('\n', '<br>')


class ContentType(IntEnum):
    TEXT = 0
    LINK = 1
    EMOTION = 2
    IMAGE = 3
    AT = 4
    VIDEO = 5
    VOICE = 10


# TODO 简化图片和视频的HTML代码

def pb_content_to_html(pb_content: Sequence[Union[PbContent, Abstract]]):
    buffer = io.StringIO()
    for content in pb_content:
        if content.type == ContentType.TEXT:
            buffer.write(html_escape(content.text))
        elif content.type == ContentType.LINK:
            buffer.write(f'<a href="{content.link}" target="_blank">{html_escape(content.text)}</a>')
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


def media_to_html(media: Sequence[Media]):
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


def cached(func):
    """缓存计算结果的装饰器，函数只会被调用一次，之后调用返回缓存结果

    只能用于无参数和状态的函数，如property
    """
    @wraps(func)
    def wrapper(*args):
        if args:
            assert len(args) == 1, f'{func.__name__}最多只能有一个参数，而且参数是可变对象'
            self = args[0]
            name = f'__{func.__name__}_result__'
            if not hasattr(self, name):
                setattr(self, name, func(self))
            return getattr(self, name)
        else:
            if not hasattr(wrapper, '__result__'):
                wrapper.__result__ = func()
            return wrapper.__result__

    return wrapper
