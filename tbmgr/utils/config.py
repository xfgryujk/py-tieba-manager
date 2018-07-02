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

import trafaret as t

OptionalKey = partial(t.Key, optional=True)


class Config:
    """表示一个配置文件，可以以属性方式访问配置
    """

    # 配置结构
    STRUCT = t.Dict()
    __slots__ = ()

    def __init__(self, value: dict):
        value = self.STRUCT.check(value)
        for cls in type(self).__mro__:
            for name in getattr(cls, '__slots__', ()):
                setattr(self, name, value[name])

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
        return {name: getattr(self, name) for name in self.__slots__}

    def save(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
