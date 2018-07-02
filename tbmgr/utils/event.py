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

"""事件机制模块

监听事件：

    @event.event_handler(EventType)  # 或者event.add_handler(handler, EventType)
    def handler(evt: EventType):
        ...  # 处理事件
        evt.cancel()  # （可选）取消事件，有些事件不可被取消

取消监听事件：

    event.remove_handler(handler)

发送事件：

    evt = EventType(...)
    if event.post_event(evt):
        ...  # 事件没被取消
    else:
        ...  # 事件被取消

** 不要假设事件被处理的顺序 **
"""

from asyncio import gather, iscoroutinefunction
from typing import Dict, Type, Set, Callable, Union, Coroutine


class Event:
    """事件类，类型代表要监听的事件，可用来传递事件参数
    """

    # 此事件能被取消
    IS_CANCELLABLE = True
    # 此事件的处理器是协程函数
    IS_HANDLERS_COROUTINE = False

    def __init__(self):
        self._is_cancelled = False

    @property
    def is_cancelled(self):
        return self._is_cancelled

    def cancel(self):
        """取消事件，实际是否被取消要看发送者的处理

        :raise NotImplementedError: 此事件不可取消
        """
        if self.IS_CANCELLABLE:
            self._is_cancelled = True
        else:
            raise NotImplementedError


# 类型别名
Handler = Callable[[Event], Union[None, Coroutine]]


class EventBus:
    """事件总线，负责管理事件处理器、发送事件
    """

    def __init__(self):
        # 事件类 -> 处理器set
        self._handlers: Dict[Type[Event], Set[Handler]] = {}

    def add_handler(self, handler: Handler, event_class: Type[Event]):
        """添加事件处理器

        :param handler: 处理器，接收一个事件参数，可以是任何可调用的对象，包括协程函数
        :param event_class: 要监听的事件类
        """
        if event_class.IS_HANDLERS_COROUTINE:
            assert iscoroutinefunction(handler), f'事件"{event_class.__qualname__}"的处理器必须是协程函数'
        else:
            assert not iscoroutinefunction(handler), f'事件"{event_class.__qualname__}"的处理器必须不是协程函数'
        self._handlers.setdefault(event_class, set())
        self._handlers[event_class].add(handler)

    def remove_handler(self, handler: Handler, event_class: Type[Event]=None):
        """移除事件处理器

        :param handler: 处理器
        :param event_class: 监听的事件类，如果为None则移除所有事件类的处理器
        """
        if event_class is None:
            for handlers in self._handlers.values():
                handlers.remove(handler)
        else:
            handlers = self._handlers.get(event_class, set())
            handlers.remove(handler)

    def post_event(self, event: Event):
        """发送事件，调用事件类对应的所有处理器，事件子类的处理器不会被调用

        ** 不要假设事件被处理的顺序 **

        :param event: 事件
        :return: 如果事件没被取消则返回True，否则返回False
        """
        assert not event.IS_HANDLERS_COROUTINE, f'对事件"{type(event).__qualname__}"，请使用async_post_event()'
        handlers = self._handlers.get(type(event), set())
        for handler in handlers:
            handler(event)
        return not event.is_cancelled

    async def async_post_event(self, event: Event, loop=None):
        """发送事件，调用事件类对应的所有处理器，事件子类的处理器不会被调用

        ** 不要假设事件被处理的顺序 **

        :param event: 事件
        :param loop: 执行协程的事件循环
        :return: 如果事件没被取消则返回True，否则返回False
        """
        assert event.IS_HANDLERS_COROUTINE, f'对事件"{type(event).__qualname__}"，请使用post_event()'
        handlers = self._handlers.get(type(event), None)
        if handlers is not None:
            await gather(*(handler(event) for handler in handlers), loop=loop)
        return not event.is_cancelled


# 全局事件总线，一般不需要其他事件总线
_global_event_bus = EventBus()

add_handler = _global_event_bus.add_handler
remove_handler = _global_event_bus.remove_handler
post_event = _global_event_bus.post_event
async_post_event = _global_event_bus.async_post_event


def event_handler(event_class: Type[Event]):
    """方便添加事件处理器的装饰器

    :param event_class: 要监听的事件类
    """
    def decorator(func):
        add_handler(func, event_class)
        return func
    return decorator
