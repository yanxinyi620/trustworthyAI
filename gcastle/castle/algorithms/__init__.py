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

from .ttpm import TTPM
from .lingam import DirectLiNGAM
from .lingam import ICALiNGAM
from .pc import PC
from .anm import ANMNonlinear
from .gradient.notears import Notears
from .gradient.notears import NotearsLowRank

from ..backend import backend, backend_logger

if backend == 'pytorch':
    from ..backend.pytorch import *
elif backend == 'mindspore':
    from ..backend.mindspore import *

backend_logger.warning(f"You are using ``{backend}`` as backend for Castle.")
