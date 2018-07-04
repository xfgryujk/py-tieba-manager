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
from typing import Union, List, Dict, Any, Tuple

import trafaret as t


class OptionalKey(t.Key):
    def __init__(self, default, name=None):
        super().__init__(name, default, True)


class ConfigMeta(type):
    """用来创建Config类的__struct__
    """

    def __new__(mcs, name, bases: Tuple[type, ...], namespace: Dict[str, Any]):
        # 添加此类的配置
        fields = set()
        cls_struct = {}
        for key, value in list(namespace.items()):
            if type(value) is dict and len(value) == 1:
                field_key, field_checker = list(value.items())[0]
                if isinstance(field_key, t.Key):
                    del namespace[key]

                    field_key: t.Key
                    # 默认name和类属性名一样
                    if field_key.name is None:
                        field_key.name = key
                    # 统一设置to_name，以后就不用判断to_name是否为None了
                    if field_key.to_name is None:
                        field_key.to_name = key
                    assert field_key.to_name == key, f'{field_key.to_name} != {key} 配置key.to_name必须和类属性名一样'

                    fields.add(field_key.to_name)
                    cls_struct[field_key] = field_checker

        # 添加基类的配置
        base_keys: List[t.Key] = []
        for base in bases:
            if issubclass(base, Config):
                for key in base.__struct__.keys:
                    # 基类有，此类没有的配置
                    if key.to_name not in fields:
                        base_keys.append(key)
                        fields.update(key.to_name)

        cls = type.__new__(mcs, name, bases, namespace)
        cls.__struct__ = t.Dict(cls_struct, *base_keys)
        return cls


class Config(metaclass=ConfigMeta):
    """表示一个配置文件，可以以属性方式访问配置，支持继承

    配置类型最好都是JSON支持的类型，如要使用其他类型可以用property
    配置以类属性的方式声明，如：

        name = {OptionalKey(0): t.Int}

    支持嵌套，如：

        nested_config = {OptionalKey({}): Config}

    或者

        nested_config = {OptionalKey({}): t.Dict >> Config}

    """

    # 配置结构，见trafaret文档
    __struct__: t.Dict

    def __init__(self, raw: dict=None, **kwargs):
        # 支持传入dict或用关键字参数
        if raw is None:
            raw = {}
        raw = dict(raw, **kwargs)

        # 移除未知的key，防止check()出错
        known_keys = {key.name for key in self.__struct__.keys}
        for key in list(raw.keys()):
            if key not in known_keys:
                del raw[key]

        raw = self.__struct__.check(raw)
        for key, value in raw.items():
            setattr(self, key, value)

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
            return cls()

    @classmethod
    def from_str(cls, s):
        return cls(json.loads(s))

    def to_dict(self):
        res = {key.to_name: getattr(self, key.to_name) for key in self.__struct__.keys}
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
