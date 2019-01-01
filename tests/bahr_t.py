#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2019 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
#  2019	Abdelkrime Aries <kariminfo0@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aruudy.poetry import bahr
from aruudy.poetry.bahr import Bahr, BahrError

print bahr.name_type(u"كامل") == "aname"
print bahr.name_type(u"complete") == "ename"

mutadarik = {
        "aname": u"متدارك",
        "ename": "overtaking",
        "trans": "mutadārik",
        "ameter": "",
        "emeter": "S- S- S- S-", # - can be substituted for u u)
        "key": u"حركات المحدث تنتقل  فعلن فعلن فعلن فعل"
}
print bahr.get_bahr("overtaking") == mutadarik
print type(bahr.get_bahr("overtaking"))
print bahr.get_bahr("overtaking", dic=False) == Bahr(mutadarik)
print type(bahr.get_bahr("overtaking", dic=False))

print bahr.arabic_names()
