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


import os

from castle.common.logger import Logger

backend_logger = Logger()

def get_backend_name() -> str:
    """Fetch backend from environment variable"""

    backend_name = os.getenv('CASTLE_BACKEND')
    if backend_name not in ['pytorch', 'mindspore', None]:
        raise TypeError("Please use ``os.environ[CASTLE_BACKEND] = backend`` "
                        "to set backend environment variable to `pytorch` or "
                        "`mindspore`.")
    if backend_name is None:
        backend_name = 'pytorch'
        backend_logger.warning(
            "The environment variable ``CASTLE_BACKEND`` is not set, will default "
            "setting to pytorch. You can set it by use `os.environ['CASTLE_BACKEND'] "
            "= backend`, the supported backend is `pytorch` or `mindspore`.")

    return backend_name

backend = get_backend_name()
