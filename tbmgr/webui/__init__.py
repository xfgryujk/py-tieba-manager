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

"""web UI模块
"""

import os

from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler

WEB_ROOT = os.path.join(os.path.dirname(__file__), 'tbmgr', 'dist')


# noinspection PyAbstractClass
class MainHandler(StaticFileHandler):
    """为了使用Vue Router的history模式，把所有请求转发到index.html
    """

    async def get(self, *args, **kwargs):
        await super().get('index.html', *args, **kwargs)


ROUTES = [
    ('/.*', MainHandler, {'path': WEB_ROOT})
]

SETTINGS = {
    'static_path': os.path.join(WEB_ROOT, 'static'),
    'cookie_secret': 'ywwuyi1145141919'
}


def serve_forever():
    app = Application(ROUTES, **SETTINGS)
    app.listen(8102)
    IOLoop.current().start()
