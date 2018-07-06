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

"""单例模块
"""


class SingletonMeta(type):

    def __new__(mcs, name, bases, namespace, **kwargs):
        """用来支持关键字参数
        """
        return type.__new__(mcs, name, bases, namespace)

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__init_params = kwargs
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        raise NotImplementedError(f'请使用{cls.__name__}.get_instance()')

    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = super().__call__(**cls.__init_params)
            del cls.__init_params
        return cls.__instance


class Singleton(metaclass=SingletonMeta):
    """单例，实例只能用get_instance()获取，不能通过调用类来构造

    使用方法：

        class MySingleton(Singleton, init_param1=..., init_param2=..., ...):
            ...

        instance = MySingleton.get_instance()

    其中init_param为构造实例的参数
    """
