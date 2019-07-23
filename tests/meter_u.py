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

from aruudy.poetry import meter
from aruudy.poetry.meter import Bahr


def test_name_type():
    assert meter.name_type(u"كامل") == "arabic"
    assert meter.name_type(u"complete") == "english"

def test_get_bahr():
    assert meter.get_bahr("overtaking") == meter.mutadaarik.to_dict()
    assert type(meter.get_bahr("overtaking")) is dict
    assert meter.get_bahr("overtaking", dic=False) == meter.mutadaarik
    assert type(meter.get_bahr("overtaking", dic=False)) is Bahr
    assert meter.get_bahr("aaa") == None

def test_get_names():
    assert meter.get_names("arabic")[0] == u"طويل"
    assert meter.get_names("english")[0] == "long"
    assert meter.get_names("trans")[0] == u"ṭawīl"
    assert meter.get_names()[0]["trans"] == u"ṭawīl"

def test_bahr():
    b = meter.get_bahr("overtaking", dic=False)

    assert b.test_name("trans", u"mutadārik")
    assert not b.test_name("trans", u"kamil")
    #with pytest.raises(BahrError):
    #    b.test_property("transliterate", u"kamil")

    assert b.to_dict() == meter.mutadaarik.to_dict()
