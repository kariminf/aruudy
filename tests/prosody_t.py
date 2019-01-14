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
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aruudy.poetry import prosody

orig = u"أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ"

s = prosody.process_shatr(orig).to_dict()
print (s["bahr"].name["arabic"])
print (s["bahr"].name["english"])
print (s["bahr"].name["trans"])

with open("exp.json") as f:
    exps = json.load(f)["exp"]

for exp in exps:
    s = prosody.process_shatr(unicode(exp["shatr"]))
    print(unicode(exp["bahr"]) + " " + str(s.bahr))
