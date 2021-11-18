# coding=utf-8
# Copyright (C) 2021. Huawei Technologies Co., Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
from colorama import Fore, Style


class Logger(object):
    """
    An object to print logs

    Examples
    --------
    If you want to print to ``file``, you can instantiation like ``Logger(file)``.
    >>> logger = Logger()
    >>> logger.debug('this is debug.')
    >>> logger.info('this is info')
    >>> logger.warning('this is warning')
    >>> logger.error('this is error')
    >>> logger.critical('this is critical')
    """

    DATETIME_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    def __init__(self, file=None, stream_level=logging.DEBUG,
                 file_level=logging.DEBUG) -> None:
        self.logger = logging.getLogger(file)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter(self.DATETIME_FORMAT)

        # remove default handler to Avoid repeated printing
        if len(self.logger.handlers) == 1:
            self.logger.handlers.pop()

        sh = logging.StreamHandler()
        sh.setFormatter(fmt=fmt)
        sh.setLevel(stream_level)
        self.logger.addHandler(sh)
        if file:
            fh = logging.FileHandler(file)
            fh.setFormatter(fmt=fmt)
            fh.setLevel(file_level)
            self.logger.addHandler(fh)

    def debug(self, msg: str) -> None:
        self.logger.debug(Fore.BLUE + msg + Style.RESET_ALL)

    def info(self, msg: str) -> None:
        self.logger.info(Fore.BLUE + msg + Style.RESET_ALL)

    def warning(self, msg: str) -> None:
        self.logger.warning(Fore.RED + msg + Style.RESET_ALL)

    def error(self, msg: str) -> None:
        self.logger.error(Fore.RED + msg + Style.RESET_ALL)

    def critical(self, msg: str) -> None:
        self.logger.critical(Fore.RED + msg + Style.RESET_ALL)

