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

"""登录贴吧，获取cookie
"""

import logging
import os
import subprocess
import tempfile

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait

_logger = logging.getLogger('tblogin')

WEB_DRIVER_DIR = os.path.dirname(__file__)


def main():
    try:
        driver = webdriver.Chrome(os.path.join(WEB_DRIVER_DIR, 'chromedriver.exe'))
    except WebDriverException:
        try:
            driver = webdriver.Edge(os.path.join(WEB_DRIVER_DIR, 'MicrosoftWebDriver.exe'))
        except WebDriverException:
            _logger.exception('创建WebDriver失败：')
            return

    driver.get('https://passport.baidu.com/v2/?login')
    WebDriverWait(driver, 999999999).until(lambda driver_: driver_.get_cookie('BDUSS'))
    cookie = driver.get_cookie('BDUSS')
    driver.close()

    filename = tempfile.mktemp('.txt')
    with open(filename, 'w') as f:
        f.write('你的Cookie为：\n')
        f.write(f'BDUSS={cookie["value"]}\n')
    subprocess.run(['start', filename], shell=True)


if __name__ == '__main__':
    main()
