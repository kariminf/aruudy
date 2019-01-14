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
#

import re
from aruudy.poetry import foot as f

is_haraka = re.compile(u"[\u064E\u064F\u0650\u0653]").search

def get_ameter (text):
    ameter = ""
    parts = []
    buf = ""
    for c in text:
        buf += c
        if is_haraka(c):
            if buf[: -2].strip():
                ameter += "s" #sabab
                parts.append(buf[: -2])
                buf = buf[-2:]
            ameter += "w" #watad
            parts.append(buf)
            buf = ""
    if buf.strip():
        ameter += "s"
        parts.append(buf)

    return ameter, parts

def a2e_meter (ameter):
    res = ameter
    res = res.replace("ws", "-")
    res = res.replace("w", "u")
    return res

def e2a_meter (emeter):
    res = emeter
    res = res.replace("-", "ws")
    res = res.replace("u", "w")
    return res

buhuur = []

class BahrError (Exception):
    def __init__(self, name):
        Exception.__init__(self, "Bahr does not have an attribute called: " + name)

class Bahr(object):
    def __init__(self, info):
        self.keys = []
        for key in info:
            setattr(self, key, info[key])
            self.keys.append(key)
        buhuur.append(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return str(self.get_names())

    def get_names(self):
        return self.get_value("name")

    def test_property(self, key, value):
        val = self.get_value(key)
        return val == value

    def get_value(self, key, key2=None):
        if not key in self.keys:
            raise BahrError(key)
        res = getattr(self, key)
        if key2:
            return res[key2]
        return res

    def to_dict(self):
        dic = {}
        for key in self.keys:
            dic[key] = getattr(self, key)
        del dic["meter"]
        """
        m = []
        for aruud in self.meter:
            a = {}
            for foot in aruud:
        """

        return dic

    def validate(self, emeter):

        for var in self.meter: # different variants
            res = []
            text_emeter = emeter
            for foot in var: # diffent feet of the variant
                text_foot, text_emeter = foot.process(text_emeter)
                if not text_foot:
                    res = None
                    break
                res.append(text_foot)
            if res:
                return res
        return None


tawiil = Bahr({
    "name": {
        "arabic": u"طويل",
        "english": "long",
        "trans": u"ṭawīl"
    },
    "meter": [
        [
        f.WWSWS([f.SALIM, f.QABDH]),
        f.WWSWSWS([f.SALIM, f.QABDH, f.KAFF]),
        f.WWSWS([f.SALIM, f.QABDH]),
        f.WWSWSWS([f.QABDH]),
        ]
    ],
    "key": u"طويلٌ له دون البحور فضائلٌ  فعولن مفاعيلن فعولن مفاعلن"
})

madiid = Bahr({
    "name": {
        "arabic": u"مديد",
        "english": "protracted",
        "trans": u"madīd"
    },
    "meter": [
        [
        f.WSWWSWS([f.SALIM, f.KHABN]),
        f.WSWWS([f.SALIM, f.KHABN]),
        f.WSWWSWS([f.SALIM, f.KHABN])
        ]
    ],
    "key": u"لمديد الشعر عندي صفاتُ  فاعلاتن فاعلن فاعلاتن"
})

basiit = Bahr({
    "name": {
        "arabic": u"بسيط",
        "english": "spread-out",
        "trans": u"basīṭ"
    },
    "meter": [
        [
        f.WSWSWWS([f.SALIM, f.KHABN, f.TAI]),
        f.WSWWS([f.SALIM, f.KHABN]),
        f.WSWSWWS([f.SALIM, f.KHABN, f.TAI]),
        f.WSWWS([f.KHABN, f.QATE]),
        ],
        [
        f.WSWSWWS([f.SALIM, f.KHABN, f.TAI]),
        f.WSWWS([f.SALIM, f.KHABN]),
        f.WSWSWWS([f.SALIM, f.KHABN, f.TAI, f.QATE, f.TADIIL]),
        ],
    ],
    "key": u"إن البسيط لديه يبسط الأملُ  مستفعلن فعلن مستفعلن فعلن"
})

wafir = Bahr({
    "name": {
        "arabic": u"وافر",
        "english": "abundant",
        "trans": u"wāfir"
    },
    "meter": [
        [
        f.WWSWWWS([f.SALIM, f.ASAB]),
        f.WWSWWWS([f.SALIM, f.ASAB]),
        f.WWSWS([f.SALIM]),
        ]
    ],
    "key": u"بحور الشعر وافرها جميل  مفاعلتن مفاعلتن فعولن"
})

kaamil = Bahr({
    "name": {
        "arabic": u"كامل",
        "english": "complete",
        "trans": u"kāmil"
    },
    "meter": [
        [
        f.WWWSWWS([f.SALIM, f.IDHMAR]),
        f.WWWSWWS([f.SALIM, f.IDHMAR]),
        f.WWWSWWS([f.SALIM, f.IDHMAR])
        ],
        [
        f.WWWSWWS([f.SALIM, f.IDHMAR]),
        f.WWWSWWS([f.SALIM, f.IDHMAR])
        ],
    ],
    "key": u"كمل الجمال من البحور الكامل متفاعلن متفاعلن متفاعلن"
})

hazj = Bahr({
    "name": {
        "arabic": u"هزج",
        "english": "trilling",
        "trans": u"hazaj",
    },
    "meter": [
        [
        f.WWSWSWS([f.SALIM, f.KAFF]),
        f.WWSWSWS([f.SALIM, f.KAFF])
        ]
    ],
    "key": u"على الأهزاج تسهيل      مفاعيلن مفاعيلن"
})

rajz = Bahr({
    "name": {
        "arabic": u"رجز",
        "english": "trembling",
        "trans": u"rajaz"
    },
    "meter": [
        [
        f.WSWSWWS([f.SALIM, f.KHABN]),
        f.WSWSWWS([f.SALIM, f.KHABN]),
        f.WSWSWWS([f.SALIM, f.KHABN])
        ]
    ],
    "key": u"في أبحر الأرجاز بحرٌ يسهل   مستفعلن مستفعلن مستفعلن"
})

raml = Bahr({
    "name": {
        "arabic": u"رمل",
        "english": "trotting",
        "trans": u"ramal",
    },
    "meter": [
        [
        f.WSWWSWS([f.SALIM, f.KHABN]),
        f.WSWWSWS([f.SALIM, f.KHABN]),
        f.WSWWSWS([f.SALIM, f.KHABN])
        ]
    ],
    "key": u"رمل الأبحر ترويه الثقات فاعلاتن فاعلاتن فاعلاتن"
})

sariie = Bahr({
    "name": {
        "arabic": u"سريع",
        "english": "swift",
        "trans": u"sarīʿ",
    },
    "meter": [
        [
        f.WSWSWWS([f.SALIM, f.KHABN, f.TAI, f.KHABL]),
        f.WSWSWWS([f.SALIM, f.KHABN, f.TAI, f.KHABL]),
        f.WSWWS([f.SALIM])
        ]
    ],
    "key": u"بحرٌ سريع ماله ساحل مستفعلن مستفعلن فاعلن"
})

munsarih = Bahr({
    "name": {
        "arabic": u"منسرح",
        "english": "quick-paced",
        "trans": u"munsariħ"
    },
    "meter": [
        [
        f.WSWSWWS([f.SALIM, f.KHABN]),
        f.WSWSWSW([f.SALIM, f.TAI]),
        f.WSWSWWS([f.TAI])
        ]
    ],
    "key": u"منسرح فيه يضرب المثل    مستفعلن مفعولات مفتعلن"
})

khafiif = Bahr({
    "name": {
        "arabic": u"خفيف",
        "english": "light",
        "trans": u"khafīf"
    },
    "meter": [
        [
        f.WSWWSWS([f.SALIM, f.KHABN, f.KAFF]),
        f.WSWSWWS([f.SALIM]),
        f.WSWWSWS([f.SALIM, f.KHABN, f.SHAKL])
        ]
    ],
    "key": u"يا خفيفاً خفّت به الحركات   فاعلاتن مستفعلن فاعلاتن"
})

mudharie = Bahr({
    "name": {
        "arabic": u"مضارع",
        "english": "similar",
        "trans": u"muḍāriʿ"
    },
    "meter": [
        [
        f.WWSWSWS([f.SALIM, f.QABDH,f.KAFF]),
        f.WSWWSWS([f.SALIM])
        ]
    ],
    "key": u"تعدّ المضارعات  مفاعيلُ فاعلاتن"
})

muqtadhib = Bahr({
    "name": {
        "arabic": u"مقتضب",
        "english": "untrained",
        "trans": u"muqtaḍab"
    },
    "meter": [
        [
        f.WSWSWSW([f.SALIM, f.KHABN]),
        f.WSWSWWS([f.TAI])
        ]
    ],
    "key": u"اقتضب كما سألوا مفعلات مفتعلن"
})

mujdath = Bahr({
    "name": {
        "arabic": u"مجتث",
        "english": "cut-off",
        "trans": u"mujtathth"
    },
    "meter": [
        [
        f.WSWSWWS([f.SALIM, f.KHABN]),
        f.WSWWSWS([f.SALIM, f.KHABN])
        ]
    ],
    "key": u"أن جثت الحركات  مستفعلن فاعلاتن"
})

mutaqaarib = Bahr({
    "name": {
        "arabic": u"متقارب",
        "english": "nearing",
        "trans": u"mutaqārib"
    },
    "meter": [
        [
        f.WWSWS([f.SALIM, f.QABDH]),
        f.WWSWS([f.SALIM, f.QABDH]),
        f.WWSWS([f.SALIM, f.QABDH]),
        f.WWSWS([f.SALIM, f.QABDH])
        ]
    ],
    "key": u"عن المتقارب قال الخليل      فعولن فعولن فعولن فعول"
})

mutadaarik = Bahr({
    "name": {
        "arabic": u"متدارك",
        "english": "overtaking",
        "trans": u"mutadārik"
    },
    "meter": [
        [
        f.WSWWS([f.SALIM, f.KHABN, f.QATE]),
        f.WSWWS([f.SALIM, f.KHABN, f.QATE]),
        f.WSWWS([f.SALIM, f.KHABN, f.QATE]),
        f.WSWWS([f.SALIM, f.KHABN, f.QATE])
        ]
    ],
    "key": u"حركات المحدث تنتقل  فعلن فعلن فعلن فعل"
})

def name_type(name):
    if re.match("^[a-zA-Z]", name):
        return "english"
    return "arabic"

def get_bahr(name, dic=True):
    """Search for poetry Bahr by name.

    Parameters
    ----------
    name : string
        name of the poetry Bahr (meter).
    dic : bool
        True(default): it returns a dict object with all information.
        If False, it returns an object of type Bahr

    Returns
    -------
    type
        dict: containing the information.
        or a Bahr object.
        or None

    """
    label = name_type(name)
    for b in buhuur:
        if b.test_property(label, name):
            if dic:
                return b.to_dict()
            return b
    return None

def _get_values(attr1, attr2 = None):
    values = []
    for b in buhuur:
        values.append(b.get_value(attr1, attr2))
    return values

def arabic_names():
    return _get_values("name")

def english_names():
    return _get_values("ename")

def trans_names():
    return _get_values("trans")

def search_bahr(emeter, ameter=None, names=False):
    for b in buhuur:
        res = b.validate(emeter)
        if res:
            return b, res

    return None, None
