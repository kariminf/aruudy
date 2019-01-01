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
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aruudy.poetry import bahr
from aruudy.poetry.bahr import Bahr, BahrError

mutadarik = {
        "aname": u"متدارك",
        "ename": "overtaking",
        "trans": u"mutadārik",
        "ameter": "",
        "emeter": "S- S- S- S-", # - can be substituted for u u)
        "key": u"حركات المحدث تنتقل  فعلن فعلن فعلن فعل"
}

def test_name_type():
    assert bahr.name_type(u"كامل") == "aname"
    assert bahr.name_type(u"complete") == "ename"

def test_get_bahr():
    assert bahr.get_bahr("overtaking") == mutadarik
    assert type(bahr.get_bahr("overtaking")) is dict
    assert bahr.get_bahr("overtaking", dic=False) == Bahr(mutadarik)
    assert type(bahr.get_bahr("overtaking", dic=False)) is Bahr
    assert bahr.get_bahr("aaa") == None

def test_get_names():
    assert bahr.arabic_names()[0] == u"طويل"
    assert bahr.english_names()[0] == "long"
    assert bahr.trans_names()[0] == u"ṭawīl"

def test_bahr():
    b = bahr.get_bahr("overtaking", dic=False)

    assert b.test_property("trans", u"mutadārik")
    assert not b.test_property("trans", u"kamil")
    with pytest.raises(BahrError):
        b.test_property("transliterate", u"kamil")

    assert b.get_value("trans") == u"mutadārik"
    with pytest.raises(BahrError):
        b.get_value("transliterate")

    assert b.to_dict() == mutadarik
