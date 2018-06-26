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

"""贴吧客户端API
"""

import hashlib
import logging
from enum import Enum

from aiohttp import ClientSession, MultipartWriter
from aiohttp.payload import get_payload

from .pyprotos.tbclient.FrsPage.FrsPageReqIdl_pb2 import FrsPageReqIdl
from .pyprotos.tbclient.FrsPage.FrsPageResIdl_pb2 import FrsPageResIdl
from .pyprotos.tbclient.PbFloor.PbFloorReqIdl_pb2 import PbFloorReqIdl
from .pyprotos.tbclient.PbFloor.PbFloorResIdl_pb2 import PbFloorResIdl
from .pyprotos.tbclient.PbPage.PbPageReqIdl_pb2 import PbPageReqIdl
from .pyprotos.tbclient.PbPage.PbPageResIdl_pb2 import PbPageResIdl

logger = logging.getLogger(__name__)


class TbError(Exception):
    """贴吧请求返回的错误
    """

    def __init__(self, code, msg):
        super().__init__(f'错误代码{code}：{msg}')
        self.code = int(code)
        self.msg = msg


class BanDuration(str, Enum):
    _1 = '1'
    _3 = '3'
    _10 = '10'


class TbClient:
    """一个TbClient代表一个账号
    """

    # 客户端居然不用HTTPS，差评
    URL_PREFIX = 'http://c.tieba.baidu.com'

    def __init__(self, cookies: dict, loop=None):
        self._session = ClientSession(loop=loop, cookies=cookies,
                                      headers={'User-Agent': 'bdtb for Android 9.4.8.4'})
        self._user_name = ''
        self._bduss = cookies.get('BDUSS', cookies.get('bduss', ''))
        if not self._bduss:
            logger.warning('Cookie中未指定BDUSS！')
        # 防CSRF用的口令号
        self._tbs = ''

    async def init(self):
        """获取用户信息
        :exception TbError: 获取失败
        """
        async with self.post(self.URL_PREFIX + '/c/s/login', {
            'bdusstoken': self._bduss,
        }) as r:
            res = await r.json(content_type=None)
            if res['error_code'] != '0':
                raise TbError(res['error_code'], res['error_msg'])

            self._user_name = res['user']['name']
            self._tbs = res['anti']['tbs']

    async def uninit(self):
        await self._session.close()

    @property
    def user_name(self):
        return self._user_name

    @property
    def bduss(self):
        return self._bduss

    @property
    def tbs(self):
        return self._tbs

    @staticmethod
    def __add_sign(data):
        """sign算法：除了protobuf部分以外的POST参数按key升序排列，组成'key=value'的形式连起来，
        最后加上'tiebaclient!!!'，UTF-8编码后计算MD5
        """
        buffer = ''.join('='.join((key, data[key]))
                         for key in sorted(data.keys())
                         if key != 'sign' and isinstance(data[key], str)
                         ) + 'tiebaclient!!!'
        data['sign'] = hashlib.md5(buffer.encode('utf-8')).hexdigest()

    def post(self, url, data=None, need_tbs=False, **kwargs):
        """客户端POST请求，会自动加上一些参数
        :param url: URL
        :param data: body参数
        :param need_tbs: 添加tbs
        :return: 同aiohttp的post
        """
        data = {key: value if isinstance(value, str) else str(value)
                for key, value in data.items()
                } if data is not None else {}
        if need_tbs:
            data['tbs'] = self._tbs
        self.__add_sign(data)

        return self._session.post(url, data=data, **kwargs)

    def post_protobuf(self, url, protobuf_msg, data=None, **kwargs):
        """客户端POST请求protobuf版，会自动加上一些参数和头部
        :param url: URL
        :param protobuf_msg: protobuf message，一般是XXXReqIdl
        :param data: body其他参数
        :return: 同aiohttp的post
        """
        data = {key: value if isinstance(value, str) else str(value)
                for key, value in data.items()
                } if data is not None else {}
        self.__add_sign(data)

        with MultipartWriter('form-data') as mp:
            # MultipartWriter好像有BUG，append之后header就不能改了...
            for key, value in data.items():
                part = get_payload(str(value), headers={})
                part.set_content_disposition('form-data', name=key)
                mp.append_payload(part)
            part = get_payload(protobuf_msg.SerializeToString(), headers={})
            part.set_content_disposition('form-data', name='data', filename='file')
            mp.append_payload(part)

            return self._session.post(url, data=mp, headers={'x_bd_data_type': 'protobuf'},
                                      **kwargs)

    async def get_threads(self, forum_name, page=1):
        """取主题列表
        :param forum_name: 贴吧名
        :param page: 页数
        :return: Thread list
        """
        req = FrsPageReqIdl()
        req.data.kw = forum_name
        req.data.pn = page
        # 每页最大主题数（可以小于这个值），这两个同时存在时好像取较小的那个，
        # 抓包得rn = 30, rn_need = 90，这里和网页版一样取50
        req.data.rn = 50
        req.data.rn_need = 50
        res = FrsPageResIdl()
        async with self.post_protobuf(self.URL_PREFIX + '/c/f/frs/page?cmd=301001',
                                      req) as r:
            res.ParseFromString(await r.read())

        # TODO 解析主题
        # print(res)
        for thread in res.data.thread_list:
            print(thread.title)
        print(len(res.data.thread_list))

    async def get_posts(self, fid, tid, page=1, with_sub_post=False):
        """取帖子列表
        :param fid: 贴吧ID
        :param tid: 主题ID
        :param page: 页数
        :param with_sub_post: 是否同时取楼中楼列表
        :return: Post list, SubPost list
        """
        req = PbPageReqIdl()
        req.data.forum_id = fid
        req.data.kz = tid
        req.data.pn = page
        req.data.rn = 30
        # 带楼中楼
        req.data.with_floor = 1 if with_sub_post else 0
        req.data.floor_rn = 5
        res = PbPageResIdl()
        async with self.post_protobuf(self.URL_PREFIX + '/c/f/pb/page?cmd=302001',
                                      req) as r:
            res.ParseFromString(await r.read())

        # TODO 解析帖子
        # print(res)
        for post in res.data.post_list:
            # print(post.content)
            print(post.floor, ''.join(content.text for content in post.content))

    async def get_sub_posts(self, tid, pid, page=1):
        """取楼中楼列表
        :param tid: 主题ID
        :param pid: 帖子ID
        :param page: 页数
        :return: SubPost list
        """
        req = PbFloorReqIdl()
        req.data.kz = tid
        req.data.pid = pid
        req.data.pn = page
        res = PbFloorResIdl()
        async with self.post_protobuf(self.URL_PREFIX + '/c/f/pb/floor?cmd=302002',
                                      req) as r:
            res.ParseFromString(await r.read())

        # TODO 解析楼中楼
        # print(res)
        for index, sub_post in enumerate(res.data.subpost_list):
            print(index + 1, ''.join(content.text for content in sub_post.content))

    async def ban_user(self, fid, forum_name, user_name, duration: BanDuration,
                       reason=''):
        """封号
        :param fid: 贴吧ID
        :param forum_name: 贴吧名
        :param user_name: 用户名
        :param duration: 封禁时长
        :param reason: 封禁原因
        """
        async with self.post(self.URL_PREFIX + '/c/c/bawu/commitprison', {
            'fid':     fid,
            'word':    forum_name,
            'un':      user_name,
            'day':     duration,
            'reason':  reason,
            'z':       '1111111111',  # 主题ID，可以乱取
            # 'post_id': pid,
            'ntn':     'banid'
        }, True) as r:
            res = await r.json(content_type=None)

            if res['error_code'] != '0':
                raise TbError(res['error_code'], res['error_msg'])

    async def add_black_list(self, forum_name, user_id):
        """拉黑
        :param forum_name: 贴吧名
        :param user_id: 用户ID
        :exception TbError: 获取失败
        """
        # 客户端没有拉黑API
        async with self.post('http://tieba.baidu.com/bawu2/platform/addBlack', {
            'word':    forum_name,
            'user_id': user_id,
            'ie':      'utf-8'
        }, True) as r:
            res = await r.json(content_type=None)

            if res['errno'] != 0:
                raise TbError(res['errno'], res['errmsg'])

    async def delete_thread(self, fid, forum_name, tid):
        """删除主题
        :param fid: 贴吧ID
        :param forum_name: 贴吧名
        :param tid: 主题ID
        :exception TbError: 获取失败
        """
        async with self.post(self.URL_PREFIX + '/c/c/bawu/delthread', {
            'fid':  fid,
            'word': forum_name,
            'z':    tid
        }, True) as r:
            res = await r.json(content_type=None)

            if res['error_code'] != '0':
                raise TbError(res['error_code'], res['error_msg'])

    async def delete_post(self, fid, forum_name, tid, pid):
        """删除帖子
        :param fid: 贴吧ID
        :param forum_name: 贴吧名
        :param tid: 主题ID
        :param pid: 帖子ID
        :exception TbError: 获取失败
        """
        async with self.post(self.URL_PREFIX + '/c/c/bawu/delpost', {
            'fid':  fid,
            'word': forum_name,
            'z':    tid,
            'pid':  pid
        }, True) as r:
            res = await r.json(content_type=None)

            if res['error_code'] != '0':
                raise TbError(res['error_code'], res['error_msg'])

    # TODO 删楼中楼


def test():
    from asyncio import get_event_loop

    loop = get_event_loop()
    client = TbClient({
        'BDUSS': ''
    }, loop)
    loop.run_until_complete(client.init())
    # loop.run_until_complete(client.get_threads('一个极其隐秘只有xfgryujk知道的地方', 1))
    # loop.run_until_complete(client.get_posts(309740, 5010576625, 1))
    # loop.run_until_complete(client.get_sub_posts(5010576625, 108473589139, 1))
    # loop.run_until_complete(client.ban_user(309740, '一个极其隐秘只有xfgryujk知道的地方',
    #                                         '和谐我的没J8', BanDuration._1))
    # loop.run_until_complete(client.add_black_list('一个极其隐秘只有xfgryujk知道的地方',
    #                                               81741779))
    # loop.run_until_complete(client.delete_thread(309740, '一个极其隐秘只有xfgryujk知道的地方',
    #                                              4426261107))
    loop.run_until_complete(client.delete_post(309740, '一个极其隐秘只有xfgryujk知道的地方',
                                               4426261107, 120456310061))
    loop.run_until_complete(client.uninit())
