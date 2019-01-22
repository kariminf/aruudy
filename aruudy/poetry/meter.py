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
from aruudy.poetry import foot
from aruudy.poetry.foot import TafiilaType as FT
from aruudy.poetry.foot import TafiilaComp

re_haraka = re.compile(u"[\u064E\u064F\u0650\u0653]")

def get_ameter (text):
    """Get the Arabic meter of a given text.
    Produces the Arabic meter of a given text in prosody form.
    The Arabic meter is composed of two letters:

    - "w" watad (peg) which are vocalized letters
    - "s" sabab (cord) which are vowels and unvocalized letters

    Parameters
    ----------
    text : str
        Arabic text in prosody form.

    Returns
    -------
    str
        Arabic meter of the input text.
        A string composed of "w" and "s".

    """
    ameter = ""
    parts = []
    buf = ""
    for c in text:
        buf += c
        if re_haraka.search(c):
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
    """Transforms an Arabic meter to an English one.
    The Arabic meter uses vocalization as a basis:

    - "w" watad (peg) which are vocalized letters
    - "s" sabab (cord) which are vowels and unvocalized letters

    While English meter uses syllables:

    - "-" for long syllables, equivalent to "ws" in the Arabic one
    - "u" for short syllables, equivalent to "w" in the Arabic one.

    Parameters
    ----------
    ameter : str
        The Arabic meter using the two letters: "w" and "s".

    Returns
    -------
    str
        The English meter using the two characters: "-" and "u".

    """
    res = ameter
    res = res.replace("ws", "-")
    res = res.replace("w", "u")
    return res

def e2a_meter (emeter):
    """Transforms an English meter to an Arabic one.
    The English meter uses syllables as a basis:

    - "-" for long syllables, equivalent to "ws" in the Arabic one
    - "u" for short syllables, equivalent to "w" in the Arabic one.

    While the Arabic meter uses vocalization:

    - "w" watad (peg) which are vocalized letters
    - "s" sabab (cord) which are vowels and unvocalized letters

    Parameters
    ----------
    emeter : str
        The English meter using the two characters: "-" and "u".

    Returns
    -------
    str
        The Arabic meter using the two letters: "w" and "s".

    """
    res = emeter
    res = res.replace("-", "ws")
    res = res.replace("u", "w")
    return res


buhuur = []

"""
class BahrError (Exception):
    def __init__(self, name):
        Exception.__init__(self, "Bahr does not have an attribute called: " + name)
"""

class Part(TafiilaComp):
    def __init__(self, tafiila_comp):
        TafiilaComp.__init__(self, tafiila_comp.__dict__)
        self.ameter = e2a_meter(self.emeter)
        self.text = ""

    def extract(self, units=[]):
        l = len(self.emeter)
        if not units or len(units) < l:
            return None
        self.text = "".join(units[:l])
        return units[l:]

    def to_dict(self):
        return {
            "type": self.type,
            "emeter": self.emeter,
            "ameter": self.ameter,
            "mnemonic": self.mnemonic,
            "text": self.text
        }

class BahrForm(object):

    def __init__(self, feet):
        self.feet = feet

    def validate(self, emeter, units=[]):
        parts = []
        text_emeter = emeter
        units_cp = list(units)
        for foot in self.feet: # diffeennt feet of the variant
            text_foot, text_emeter = foot.process(text_emeter)
            if not text_foot:
                return None
            part = Part(text_foot)
            units_cp = part.extract(units_cp)
            parts.append(part)
        return parts

def extract_meter(bahrForm, used=True):
    """Extract the meter description from a list of :class:`~aruudy.poetry.foot.Tafiila` objects.

    Parameters
    ----------
    bahrForm : BahrForm
        An object describing the meter's form.
    used : bool
        Meters, in Arabic, can have used forms different than standard ones.
        if True: the result is used form.
        Otherwise, it is standard form

    Returns
    -------
    dict
        A dictionary object describing the meter represented by the feet.
        The dictionary contains these elements:

        - type: a string describing the type of each foot (tafiila)
        - mnemonic: a string describing the mnemonic of each foot.
        - emeter: a string describing the English meter of each foot.
        - ameter: a string describing the Arabic meter of each foot.

    """
    res = {
        "type": "",
        "mnemonic": "",
        "emeter": "",
        "ameter": ""
    }

    sep = ""
    for foot in bahrForm.feet:
        meter = foot.get_form(used)
        res["type"] += sep + meter.type.ar
        res["mnemonic"] += sep + meter.mnemonic
        res["emeter"] += sep + meter.emeter
        res["ameter"] += sep + e2a_meter(meter.emeter)
        if not sep:
            sep = " "
    return res

class Bahr(object):
    """Representation of the Arabic meter.

    Parameters
    ----------
    info : dict
        Description of parameter `info`.

    Attributes
    ----------
    name : dict
        Bahr's name, which is composed of:

        - arabic: its name in Arabic
        - english: its name in English
        - trans: its Arabic name's transliteration.
    used_scansion : dict
        Description of attribute `used_scansion`.
    meter : list(list(Tafiila))
        Description of attribute `meter`.


    std_scansion : dict
        Description of attribute `std_scansion`.

    """
    def __init__(self, info):
        buhuur.append(self)
        self.name = info["name"]
        self.meter = info["meter"]
        self.key = info["key"]

        self.used_scansion = extract_meter(self.meter[0])
        self.std_scansion = extract_meter(self.meter[0], used=False)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return str(self.get_names())

    def get_names(self):
        return self.get_value("name")

    def test_name(self, key, value):
        return value == self.name[key]

    def to_dict(self):
        dic = {
            "name": self.name,
            "used_scansion": self.used_scansion,
            "std_scansion": self.std_scansion
        }

        return dic

    def validate(self, emeter, units=[]):
        for form in self.meter: # different forms
            parts = form.validate(emeter, units)
            if parts:
                return parts
        return None

tawiil = Bahr({
    "name": {
        "arabic": u"طويل",
        "english": "long",
        "trans": u"ṭawīl"
    },
    "meter": [
        BahrForm([
        foot.WWSWS([FT.SALIM, FT.QABDH]),
        foot.WWSWSWS([FT.SALIM, FT.QABDH, FT.KAFF]),
        foot.WWSWS([FT.SALIM, FT.QABDH]),
        foot.WWSWSWS([FT.QABDH]),
        ])
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
        BahrForm([
        foot.WSWWSWS([FT.SALIM, FT.KHABN]),
        foot.WSWWS([FT.SALIM, FT.KHABN]),
        foot.WSWWSWS([FT.SALIM, FT.KHABN])
        ])
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
        BahrForm([
        foot.WSWSWWS([FT.SALIM, FT.KHABN, FT.TAI]),
        foot.WSWWS([FT.SALIM, FT.KHABN]),
        foot.WSWSWWS([FT.SALIM, FT.KHABN, FT.TAI]),
        foot.WSWWS([FT.KHABN, FT.QATE]),
        ]),
        BahrForm([
        foot.WSWSWWS([FT.SALIM, FT.KHABN, FT.TAI]),
        foot.WSWWS([FT.SALIM, FT.KHABN]),
        foot.WSWSWWS([FT.SALIM, FT.KHABN, FT.TAI, FT.QATE, FT.TADIIL]),
        ])
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
        BahrForm([
        foot.WWSWWWS([FT.SALIM, FT.ASAB]),
        foot.WWSWWWS([FT.SALIM, FT.ASAB]),
        foot.WWSWS([FT.SALIM]),
        ])
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
        BahrForm([
        foot.WWWSWWS([FT.SALIM, FT.IDHMAR]),
        foot.WWWSWWS([FT.SALIM, FT.IDHMAR]),
        foot.WWWSWWS([FT.SALIM, FT.IDHMAR])
        ]),
        BahrForm([
        foot.WWWSWWS([FT.SALIM, FT.IDHMAR]),
        foot.WWWSWWS([FT.SALIM, FT.IDHMAR])
        ])
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
        BahrForm([
        foot.WWSWSWS([FT.SALIM, FT.KAFF]),
        foot.WWSWSWS([FT.SALIM, FT.KAFF])
        ])
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
        BahrForm([
        foot.WSWSWWS([FT.SALIM, FT.KHABN]),
        foot.WSWSWWS([FT.SALIM, FT.KHABN]),
        foot.WSWSWWS([FT.SALIM, FT.KHABN])
        ])
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
        BahrForm([
        foot.WSWWSWS([FT.SALIM, FT.KHABN]),
        foot.WSWWSWS([FT.SALIM, FT.KHABN]),
        foot.WSWWSWS([FT.SALIM, FT.KHABN])
        ])
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
        BahrForm([
        foot.WSWSWWS([FT.SALIM, FT.KHABN, FT.TAI, FT.KHABL]),
        foot.WSWSWWS([FT.SALIM, FT.KHABN, FT.TAI, FT.KHABL]),
        foot.WSWWS([FT.SALIM])
        ])
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
        BahrForm([
        foot.WSWSWWS([FT.SALIM, FT.KHABN]),
        foot.WSWSWSW([FT.SALIM, FT.TAI]),
        foot.WSWSWWS([FT.TAI])
        ])
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
        BahrForm([
        foot.WSWWSWS([FT.SALIM, FT.KHABN, FT.KAFF]),
        foot.WSWSWWS([FT.SALIM]),
        foot.WSWWSWS([FT.SALIM, FT.KHABN, FT.SHAKL])
        ])
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
        BahrForm([
        foot.WWSWSWS([FT.SALIM, FT.QABDH,FT.KAFF]),
        foot.WSWWSWS([FT.SALIM])
        ])
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
        BahrForm([
        foot.WSWSWSW([FT.SALIM, FT.KHABN]),
        foot.WSWSWWS([FT.TAI])
        ])
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
        BahrForm([
        foot.WSWSWWS([FT.SALIM, FT.KHABN]),
        foot.WSWWSWS([FT.SALIM, FT.KHABN])
        ])
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
        BahrForm([
        foot.WWSWS([FT.SALIM, FT.QABDH]),
        foot.WWSWS([FT.SALIM, FT.QABDH]),
        foot.WWSWS([FT.SALIM, FT.QABDH]),
        foot.WWSWS([FT.SALIM, FT.QABDH])
        ])
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
        BahrForm([
        foot.WSWWS([FT.SALIM, FT.KHABN, FT.QATE]),
        foot.WSWWS([FT.SALIM, FT.KHABN, FT.QATE]),
        foot.WSWWS([FT.SALIM, FT.KHABN, FT.QATE]),
        foot.WSWWS([FT.SALIM, FT.KHABN, FT.QATE])
        ])
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
    name : str
        name of the poetry Bahr (meter).
    dic : bool
        True(default): it returns a dict object with all information.
        If False, it returns an object of type Bahr

    Returns
    -------
    dict
        dict: containing the information.
        or a Bahr object.
        or None

    """
    label = name_type(name)
    for b in buhuur:
        if b.test_name(label, name):
            if dic:
                return b.to_dict()
            return b
    return None


def get_names(lang=None):
    names = []
    for bahr in buhuur:
        if lang:
            names.append(bahr.name[lang])
        else:
            names.append(bahr.name)
    return names

def search_bahr(emeter, units=[]):
    for b in buhuur:
        res = b.validate(emeter, units)
        if res:
            return b, res

    return None, None
