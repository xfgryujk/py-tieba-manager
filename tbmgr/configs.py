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

"""定义配置
"""

import os

import trafaret as t

from .utils.config import Config, OptionalKey

CONFIG_DIR = os.path.join('data', 'configs')
os.makedirs(CONFIG_DIR, exist_ok=True)
GLOBAL_CFG_PATH = os.path.join(CONFIG_DIR, 'global.json')


class GlobalConfig(Config):
    """全局配置
    """

    STRUCT = t.Dict({
        OptionalKey('is_first_run', True): t.Bool,           # 第一次启动
        OptionalKey('web_ui_port', 8102): t.Int,             # web UI端口
        OptionalKey('allow_remote_connect', False): t.Bool,  # 允许远程连接web UI
    })
    __slots__ = ('is_first_run', 'web_ui_port', 'allow_remote_connect')


_global_config: GlobalConfig = None
_is_first_run = False


def get_global_config():
    return _global_config


def is_first_run():
    return _is_first_run


def init():
    """读取各种配置
    """
    global _global_config, _is_first_run
    _global_config = GlobalConfig.from_file(GLOBAL_CFG_PATH)
    if _global_config.is_first_run:
        _is_first_run = True
        _global_config.is_first_run = False
        _global_config.save(GLOBAL_CFG_PATH)
