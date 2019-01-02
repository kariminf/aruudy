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

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aruudy.poetry import meter


def test_normalize():
    assert meter.normalize(u"تَطْوِيـــــــــــــــــــــل") == u"تَطْوِيل"
    assert meter.normalize(u"الأَول الشمس القمر") == u"اَلأَول الشمس القمر"
    assert meter.normalize(u"ساح يسيح يسوح") == u"سَاح يسِيح يسُوح"

#private function
def test_prosody_del():
    assert meter._prosody_del(u"وَالشمس") == u"وَشمس"
    assert meter._prosody_del(u"فَالعلم") == u"فَلعلم"
    assert meter._prosody_del(u"فاستمعَ") == u"فستمعَ"
    assert meter._prosody_del(u"أَتَى المَظلوم إلَى القَاضِي فَأَنصفه قَاضِي العَدل") == u"أَتَ لمَظلوم إلَ لقَاضِي فَأَنصفه قَاضِ لعَدل"
    assert meter._prosody_del(u"رجعوا") == u"رجعو"

#private function
def test_prosody_add():
    assert meter._prosody_add(u"") == u""
    assert meter._prosody_add(u"") == u""
    assert meter._prosody_add(u"") == u""
    assert meter._prosody_add(u"") == u""

def _get_cv ():
    orig = u"أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ"
    dest = "VVCVCVVCVCVCVVCVVVCVVC"
    orig = armetre.fix_al(orig)
    orig = armetre.fix_awy(orig)
    assert armetre.get_cv(orig) == dest
