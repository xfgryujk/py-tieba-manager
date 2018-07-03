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

"""配置模块
"""

import json
from functools import partial
from typing import Union, List

import trafaret as t

OptionalKey = partial(t.Key, optional=True)


class Config:
    """表示一个配置文件，可以以属性方式访问配置

    以'_'开头的属性不会被当做配置的一部分
    可以继承
    可以嵌套，如：

        STRUCT = t.Dict({
            OptionalKey('nested_config', {}): Config
        })

    或者

        STRUCT = t.Dict({
            OptionalKey('nested_config', {}): t.Dict >> Config
        })

    配置类型最好都是JSON支持的类型，如要使用其他类型可以用property
    """

    # 配置结构，见trafaret文档
    STRUCT = t.Dict()
    # 子类必须在此声明配置key
    __slots__ = ('_fields',)

    def __init__(self, raw: dict):
        # 此配置所有已知key
        self._fields = set()
        for cls in type(self).__mro__:
            self._fields.update(
                filter(lambda field: not field.startswith('_'),
                       getattr(cls, '__slots__', ()))
            )

        # 移除未知的key，防止check()出错
        for key in list(raw.keys()):
            if key not in self._fields:
                del raw[key]

        raw = self.STRUCT.check(raw)
        for name in self._fields:
            setattr(self, name, raw[name])

    def __repr__(self):
        return repr(self.to_dict())

    @classmethod
    def from_file(cls, filename):
        """如果文件不存在则使用默认配置
        """
        try:
            with open(filename, encoding='utf-8') as f:
                return cls(json.load(f))
        except FileNotFoundError:
            return cls({})

    @classmethod
    def from_str(cls, s):
        return cls(json.loads(s))

    def to_dict(self):
        res = {name: getattr(self, name) for name in self._fields}
        # 遍历dict和list组成的树，把Config转为dict
        queue: List[Union[dict, list]] = [res]
        while queue:
            node = queue.pop(0)
            for index, value in (node.items() if isinstance(node, dict)
                                 else enumerate(node)):
                if isinstance(value, Config):
                    node[index] = value.to_dict()
                elif isinstance(value, (dict, list)):
                    queue.append(value)
        return res

    def save(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
