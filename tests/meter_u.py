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

import os, sys
import pytest
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aruudy.poetry import meter
from aruudy.poetry.meter import Shatr
from aruudy.poetry.bahr import Bahr


def test_normalize():
    assert meter.normalize(u"تَطْوِيـــــــــــــــــــــل") == u"تَطْوِيل"
    assert meter.normalize(u"الأَول الشمس القمر") == u"اَلأَول الشّٓمس القٓمر"
    assert meter.normalize(u"ساح يسيح يسوح") == u"سَاح يٓسِيح يٓسُوح"

#private function
def test_prosody_del():
    assert meter._prosody_del(u"وَالشمس") == u"وَشمس"
    assert meter._prosody_del(u"فَالعلم") == u"فَلعلم"
    assert meter._prosody_del(u"فاستمعَ") == u"فستمعَ"
    assert meter._prosody_del(u"أَتَى المَظلوم إلَى القَاضِي فَأَنصفه قَاضِي العَدل") == u"أَتَ لمَظلوم إلَ لقَاضِي فَأَنصفه قَاضِ لعَدل"
    assert meter._prosody_del(u"رجعوا") == u"رجعُوْ"

#private function
#def test_prosody_add():
#    assert meter._prosody_add(u"") == u""

def test_process_shatr ():
    text = u"أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ"
    ameter = "vvcvcvvcvcvcvvcvvvcvvc"

    s = meter.process_shatr(text)
    assert type(s) == Shatr

    d = s.to_dict()
    assert type(d) == dict
    assert type(d["bahr"]) == Bahr

    d = s.to_dict(bahr=True)
    assert type(d["bahr"]) == dict
    assert d["ameter"] == ameter

    s = meter.process_shatr("aaa")
    assert not s.bahr

try:
    UNICODE_EXISTS = bool(type(unicode))
except NameError:
    unicode = lambda s: str(s)

def test_bahr_detection ():
    with open("exp.json") as f:
        exps = json.load(f)["exp"]

    for exp in exps:
        try:
            txt = exp["shatr"].encode()
            out = exp["bahr"].encode()
        except:
            txt = exp["shatr"]
            out = exp["bahr"]
        #print (txt)
        s = meter.process_shatr(txt)
        assert s.bahr.aname == out
