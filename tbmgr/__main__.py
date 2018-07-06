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

"""主程序入口

执行方式：

    cd py-tieba-manager
    python tbmgr/__main__.py
    或 python -m tbmgr

** 需要Python 3.6或更高版本 **
"""

import os
import sys
# 防止直接执行本文件时找不到模块
pardir = os.path.dirname(os.path.dirname(__file__))
if pardir not in sys.path:
    sys.path.insert(0, pardir)
from tbmgr import TiebaManager


if __name__ == '__main__':
    TiebaManager.get_instance().main()
