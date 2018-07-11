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

"""数据库基本定义
"""

from typing import Type, Union

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, Session as _Session

from .migration import upgrade_to_latest
from ...configs import get_global_config

__all__ = ['OrmBase', 'Session', 'init']

OrmBase = declarative_base()
Session: Union[scoped_session, Type[_Session]] = scoped_session(sessionmaker())


def init():
    """配置Session类，升级数据库
    """
    engine = create_engine(get_global_config().database_url)
    Session.configure(bind=engine)
    # upgrade_to_latest()
    # TODO 等结构稳定后改用升级数据库
    OrmBase.metadata.create_all(engine)
