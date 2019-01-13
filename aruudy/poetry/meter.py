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

def get_ameter (text):
    res = text

    #Delete sukuun
    res = re.sub(u"\u0652", "", res)

    #Replace fatha, damma, kasra & madda with (V) for vowel
    res = re.sub(u"[^v\\s][\u064E\u064F\u0650\u0653]", "v", res)

    #Delete spaces
    res = re.sub(u"\\s+", u"", res)

    #Replace all what is left as it was a consonent
    res = re.sub(u"[^v\\s]+", "c", res)

    # add sukuun in the end
    res = re.sub(u"v$", "vc", res)

    return res

def get_emeter (ameter):
    res = ameter
    res = res.replace("vc", "-")
    res = res.replace("v", "u")
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
        return {
            "aname": self.aname,
            "ename": self.ename,
            "trans": self.trans
        }

    def test_property(self, key, value):
        val = self.get_value(key)
        return val == value

    def get_value(self, key):
        if not key in self.keys:
            raise BahrError(key)
        return getattr(self, key)

    def to_dict(self):
        dic = {}
        for key in self.keys:
            dic[key] = getattr(self, key)
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

    def compare(self, ameter):#use lavenstein distance
        return 0

# emeter from: https://en.wikipedia.org/wiki/Metre_(poetry)#The_Arabic_metres
# "–" for 1 long syllable (cv)
# "u" for 1 short syllable (c)
# "x" for a position that can contain 1 long or 1 short [-u]
# "w" for a position that can contain 1 long or 2 shorts (-|uu)
# "S" for a position that can contain 1 long, 2 shorts, or 1 long + 1 short (-uu|-u)

tawiil = Bahr({
    "aname": u"طويل",
    "ename": "long",
    "trans": u"ṭawīl",
    "meter": [
        [
        f.CCVCV([f.SALIM, f.QABDH]),
        f.CCVCVCV([f.SALIM, f.QABDH, f.KAFF]),
        f.CCVCV([f.SALIM, f.QABDH]),
        f.CCVCVCV([f.QABDH]),
        ]
    ],
    "key": u"طويلٌ له دون البحور فضائلٌ  فعولن مفاعيلن فعولن مفاعلن"
})

madiid = Bahr({
    "aname": u"مديد",
    "ename": "protracted",
    "trans": u"madīd",
    "meter": [
        [
        f.CVCCVCV([f.SALIM, f.KHABN]),
        f.CVCCV([f.SALIM, f.KHABN]),
        f.CVCCVCV([f.SALIM, f.KHABN])
        ]
    ],
    "key": u"لمديد الشعر عندي صفاتُ  فاعلاتن فاعلن فاعلاتن"
})

basiit = Bahr({
    "aname": u"بسيط",
    "ename": "spread-out",
    "trans": u"basīṭ",
    "meter": [
        [
        f.CVCVCCV([f.SALIM, f.KHABN, f.TAI]),
        f.CVCCV([f.SALIM, f.KHABN]),
        f.CVCVCCV([f.SALIM, f.KHABN, f.TAI]),
        f.CVCCV([f.KHABN, f.QATE]),
        ],
        [
        f.CVCVCCV([f.SALIM, f.KHABN, f.TAI]),
        f.CVCCV([f.SALIM, f.KHABN]),
        f.CVCVCCV([f.SALIM, f.KHABN, f.TAI, f.QATE, f.TADIIL]),
        ],
    ],
    "key": u"إن البسيط لديه يبسط الأملُ  مستفعلن فعلن مستفعلن فعلن"
})

wafir = Bahr({
    "aname": u"وافر",
    "ename": "abundant",
    "trans": u"wāfir",
    "meter": [
        [
        f.CCVCCCV([f.SALIM, f.ASAB]),
        f.CCVCCCV([f.SALIM, f.ASAB]),
        f.CCVCV([f.SALIM]),
        ]
    ],
    "key": u"بحور الشعر وافرها جميل  مفاعلتن مفاعلتن فعولن"
})

kaamil = Bahr({
    "aname": u"كامل",
    "ename": "complete",
    "trans": u"kāmil",
    "meter": [
        [
        f.CCCVCCV([f.SALIM, f.IDHMAR]),
        f.CCCVCCV([f.SALIM, f.IDHMAR]),
        f.CCCVCCV([f.SALIM, f.IDHMAR]),
        f.CCCVCCV([f.SALIM, f.IDHMAR]),
        ],
        [
        f.CCCVCCV([f.SALIM, f.IDHMAR]),
        f.CCCVCCV([f.SALIM, f.IDHMAR]),
        f.CCCVCCV([f.SALIM, f.IDHMAR]),
        ],
    ],
    "key": u"كمل الجمال من البحور الكامل متفاعلن متفاعلن متفاعلن"
})




"""
buhuur2 = [

    Bahr({
        "aname": u"هزج",
        "ename": "trilling",
        "trans": u"hazaj",
        "ameter": "ccvcvcv ccvcvcv",
        "emeter": "u--x u--x",
        "key": u"على الأهزاج تسهيل      مفاعيلن مفاعيلن"
    }),
    Bahr({
        "aname": u"رجز",
        "ename": "trembling",
        "trans": u"rajaz",
        "ameter": "cvcvccv cvcvccv cvcvccv",
        "emeter": "x-u- x-u- x-u-",
        "key": u"في أبحر الأرجاز بحرٌ يسهل   مستفعلن مستفعلن مستفعلن"
    }),
    Bahr({
        "aname": u"رمل",
        "ename": "trotting",
        "trans": u"ramal",
        "ameter": "cvccvcv cvccvcv cvccv",
        "emeter": "xu-- xu-- xu-",
        "key": u"رمل الأبحر ترويه الثقات فاعلاتن فاعلاتن فاعلاتن"
    }),
    Bahr({
        "aname": u"سريع",
        "ename": "swift",
        "trans": u"sarīʿ",
        "ameter": "cvcvccv cvcvccv cvccv",
        "emeter": "xxu- xxu- -u-",
        "key": u"بحرٌ سريع ماله ساحل مستفعلن مستفعلن فاعلن"
    }),
    Bahr({
        "aname": u"منسرح",
        "ename": "quick-paced",
        "trans": u"munsariħ",
        "ameter": "cvcvccv cvcvcv cvcccv", #TODO verify
        "emeter": "x-u- -x-u -uu-",
        "key": u"منسرح فيه يضرب المثل    مستفعلن مفعولات مفتعلن"
    }),
    Bahr({
        "aname": u"خفيف",
        "ename": "light",
        "trans": u"khafīf",
        "ameter": "cvccvcv cvcvccv cvccvcv",
        "emeter": "xu-x --u- xu-x",
        "key": u"يا خفيفاً خفّت به الحركات   فاعلاتن مستفعلن فاعلاتن"
    }),
    Bahr({
        "aname": u"مضارع",
        "ename": "similar",
        "trans": u"muḍāriʿ",
        "ameter": "u-xx -u--",
        "emeter": "ccvcvcv cvccvcv",
        "key": u"تعدّ المضارعات  مفاعيلُ فاعلاتن"
    }),
    Bahr({
        "aname": u"مقتضب",
        "ename": "untrained",
        "trans": u"muqtaḍab",
        "ameter": "cvccvc cvcccv",
        "emeter": "xu-u -uu-",
        "key": u"اقتضب كما سألوا مفعلات مفتعلن"
    }),
    Bahr({
        "aname": u"مجتث",
        "ename": "cut-off",
        "trans": u"mujtathth",
        "ameter": "cvcvccv cvccvcv",
        "emeter": "x-u- xu--",
        "key": u"أن جثت الحركات  مستفعلن فاعلاتن"
    }),
    Bahr({
        "aname": u"متقارب",
        "ename": "nearing",
        "trans": u"mutaqārib",
        "ameter": "ccvcv ccvcv ccvcv ccvcv",
        "emeter": "u-x u-x u-x u-x",
        "key": u"عن المتقارب قال الخليل      فعولن فعولن فعولن فعول"
    }),
    Bahr({
        "aname": u"متدارك",
        "ename": "overtaking",
        "trans": u"mutadārik",
        "ameter": "",
        "emeter": "S- S- S- S-", # - can be substituted for u u)
        "key": u"حركات المحدث تنتقل  فعلن فعلن فعلن فعل"
    })
]
"""

def name_type(name):
    if re.match("^[a-zA-Z]", name):
        return "ename"
    return "aname"

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

def _get_values(label):
    values = []
    for b in buhuur:
        values.append(b.get_value(label))
    return values

def arabic_names():
    return _get_values("aname")

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
