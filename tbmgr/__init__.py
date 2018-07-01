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

"""主程序
"""

import tbmgr.utils.logging as tbmlogging
import tbmgr.webui as webui
# from tbmgr.tbapi.tbclient import test


def main():
    tbmlogging.init()
    import logging
    logger = logging.getLogger('test')
    logger.debug('debug msg')
    logger.info('info msg')
    logger.warning('warning msg')
    logger.error('error msg')
    # test()
    # webui.serve_forever()
