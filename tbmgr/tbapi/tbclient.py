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

from aiohttp import ClientSession, MultipartWriter
from aiohttp.payload import get_payload

from .pyprotos.tbclient.FrsPage.FrsPageReqIdl_pb2 import FrsPageReqIdl
from .pyprotos.tbclient.FrsPage.FrsPageResIdl_pb2 import FrsPageResIdl
from .pyprotos.tbclient.PbPage.PbPageReqIdl_pb2 import PbPageReqIdl
from .pyprotos.tbclient.PbPage.PbPageResIdl_pb2 import PbPageResIdl


class TbClient:
    """一个TbClient代表一个账号
    """

    # 客户端居然不用HTTPS，差评
    URL_PREFIX = 'http://c.tieba.baidu.com'

    def __init__(self, cookies: dict, loop=None):
        self._session = ClientSession(loop=loop, cookies=cookies,
                                      headers={'User-Agent': 'bdtb for Android 9.4.8.4'})

    async def uninit(self):
        await self._session.close()

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

    def post_protobuf(self, url, protobuf_msg, data=None):
        """客户端POST请求protobuf版，会自动加上一些参数和头部
        :param url: URL
        :param protobuf_msg: protobuf message，一般是XXXReqIdl
        :param data: body其他参数
        :return: 同aiohttp的post
        """
        data = data.copy() if data is not None else {}
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

            return self._session.post(url, data=mp, headers={'x_bd_data_type': 'protobuf'})

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

    async def get_posts(self, fid, tid, page=1):
        """取帖子列表
        :param fid: 贴吧ID
        :param tid: 主题ID
        :param page: 页数
        :return: Post list
        """
        req = PbPageReqIdl()
        req.data.forum_id = fid
        req.data.kz = tid
        req.data.pn = page
        req.data.rn = 30
        # 带楼中楼
        req.data.with_floor = 1
        res = PbPageResIdl()
        async with self.post_protobuf(self.URL_PREFIX + '/c/f/pb/page?cmd=302001',
                                      req) as r:
            res.ParseFromString(await r.read())

        # TODO 解析帖子
        # print(res)
        for post in res.data.post_list:
            # print(post.content)
            print(post.floor, ''.join(content.text for content in post.content))

    # TODO 获取楼中楼
    # TODO 封号
    # TODO 拉黑
    # TODO 删主题
    # TODO 删帖子
    # TODO 删楼中楼


def test():
    from asyncio import get_event_loop

    loop = get_event_loop()
    client = TbClient({
        'BDUSS': ''
    }, loop)
    # loop.run_until_complete(client.get_threads('一个极其隐秘只有xfgryujk知道的地方', 1))
    loop.run_until_complete(client.get_posts(309740, 5010576625, 1))
    loop.run_until_complete(client.uninit())
