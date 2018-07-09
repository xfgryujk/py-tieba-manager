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

"""数据库迁移
"""

import os

from alembic.command import upgrade
from alembic.config import Config

from ...configs import get_global_config

SCRIPT_LOCATION = os.path.dirname(__file__)


def upgrade_to_latest():
    config = Config()
    config.set_main_option('script_location', SCRIPT_LOCATION)
    config.set_main_option('sqlalchemy.url', get_global_config().database_url)
    upgrade(config, 'head')
