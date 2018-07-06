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

"""定义事件类
"""

from .utils.event import Event


class AskExitEvent(Event):
    """TiebaManager.exit()被调用时触发，可以取消
    """


class CleanupEvent(Event):
    """做退出前清理，不可取消

    这是异步事件，可以在这个事件内停止协程
    """

    IS_CANCELLABLE = False
    IS_HANDLERS_COROUTINE = True


class BeforeExitEvent(Event):
    """TiebaManager.main()返回前触发，此时事件循环已停止
    """

    IS_CANCELLABLE = False
