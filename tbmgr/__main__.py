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

    python tbmgr/__main__.py
    python -m tbmgr
"""

import os
import sys
# 防止直接执行本文件时找不到模块
pardir = os.path.dirname(os.path.dirname(__file__))
if pardir not in sys.path:
    sys.path.insert(0, pardir)
from tbmgr import main


if __name__ == '__main__':
    main()
