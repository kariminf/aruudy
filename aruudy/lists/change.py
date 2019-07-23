#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2019 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
# 2019	Abdelkrime Aries <kariminfo0@gmail.com>
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

import re
from aruudy.lists import const

CHANGE_LST = {
    u"هذا": u"هَاذَا",
    u"هذه": u"هَاذِه",
    u"هذان": u"هَاذَان",
    u"هذين": u"هَاذَين",
    u"ذلك": u"ذَالِك",
    u"ذلكما": u"ذَالِكُمَا",
    u"ذلكم": u"ذَالِكُم",
    u"الله": u"أَللَاه",
    u"إله": u"إِلَاه",
    u"الإله": u"الإِلَاه",
}

def modify(word):
    m = re.match(u"((?:%s)?)(.*)([%s]?)" % (const.SPREP, const.DIAC), word)
    begining = m.group(1)
    nodiac = re.sub(u"[%s]" % const.DIAC , "", m.group(2))
    ending = m.group(3)
    res = CHANGE_LST.get(nodiac, "")
    if res:
        return begining + res + ending

    return word
