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

import re, copy

class ZuhafIlla(object):
    def __init__(self, en, ar):
        self.en = en
        self.ar = ar
    def __repr__(self):
        return self.en

class FootType(object):
    """Short summary.
    """

    #: SALIM type
    SALIM = ZuhafIlla("SALIM", u"سالم")
    IDHMAR = ZuhafIlla("IDHMAR", u"إضمار")
    WAQS = ZuhafIlla("WAQS", u"وقص")
    KHABN = ZuhafIlla("KHABN", u"خبن")
    TAI = ZuhafIlla("TAI", u"طيّ")
    ASAB = ZuhafIlla("ASAB", u"عصب")
    AQL = ZuhafIlla("AQL", u"عقل")
    QABDH = ZuhafIlla("QABDH", u"قبض")
    KAFF = ZuhafIlla("KAFF", u"كفّ")
    KHABL = ZuhafIlla("KHABL", u"خبْل")
    KHAZL = ZuhafIlla("KHAZL", u"خزل")
    SHAKL = ZuhafIlla("SHAKL", u"شكل")
    NAQS = ZuhafIlla("NAQS", u"نقص")
    TARFIIL = ZuhafIlla("TARFIIL", u"ترفيل")
    TADIIL = ZuhafIlla("TADIIL", u"تذييل")
    ISBAGH = ZuhafIlla("ISBAGH", u"إسباغ")
    HADF = ZuhafIlla("HADF", u"حذف")
    QATE = ZuhafIlla("QATE", u"قطع")
    BATR = ZuhafIlla("BATR", u"بتر")
    QASR = ZuhafIlla("QASR", u"قصر")
    QATF = ZuhafIlla("QATF", u"قطف")
    HADAD = ZuhafIlla("HADAD", u"حذذ")
    SALAM = ZuhafIlla("SALAM", u"صلم")
    KASHF = ZuhafIlla("KASHF", u"كشف")


class Tafiila(object):

    def _init(self, var):
        self.afeet = [] # allowed feet
        for foot in self.feet:
            if foot["type"] in var:
                self.afeet.append(foot)

    def process(self, text_emeter):
        for foot in self.afeet:
            if text_emeter.startswith(foot["emeter"]):
                text_foot = copy.deepcopy(foot)
                return text_foot, text_emeter[len(foot["emeter"]):]
        return None, None

    def get_meter(self, used=True):
        if used:
            return self.afeet[0].copy()
        return self.feet[0].copy()

    def to_dict(used=False):
        if used:
            return self.afeet[0]
        return self.feet[0]


# https://sites.google.com/site/mihfadha/aroudh/14

# فَاعِلُنْ
class WSWWS(Tafiila):
    #varation
    def __init__(self, var=[FootType.SALIM]):
        self.feet = [
        {
            "type": FootType.SALIM,
            "mnemonic": u"فَاعِلُنْ",
            "emeter": "-u-"
        },
        {
            "type": FootType.KHABN,
            "mnemonic": u"فَعِلُنْ",
            "emeter": "uu-"
        },
        {
            "type": FootType.TARFIIL,
            "mnemonic": u"فَاعِلَاتُنْ",
            "emeter": "-u--"
        },
        {
            "type": FootType.TADIIL,
            "mnemonic": u"فَاعِلَانْ",
            "emeter": "-u-:"
        },
        {
            "type": FootType.QATE,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        }
        ]
        self._init(var)

# فَعُولُنْ
class WWSWS(Tafiila):
    #varation
    def __init__(self, var=[FootType.SALIM]):
        self.feet = [
        {
            "type": FootType.SALIM,
            "mnemonic": u"فَعُولُنْ",
            "emeter": "u--"
        },
        {
            "type": FootType.QABDH,
            "mnemonic": u"فَعُولُ",
            "emeter": "u-u"
        },
        {
            "type": FootType.HADF,
            "mnemonic": u"فِعَلْ",
            "emeter": "u-"
        },
        {
            "type": FootType.BATR,
            "mnemonic": u"فِعْ",
            "emeter": "-"
        },
        {
            "type": FootType.QASR,
            "mnemonic": u"فَعُولْ",
            "emeter": "u-:"
        }
        ]
        self._init(var)

# مَفَاعِيلُنْ
class WWSWSWS(Tafiila):
    #varation
    def __init__(self, var=[FootType.SALIM]):
        self.feet = [
        {
            "type": FootType.SALIM,
            "mnemonic": u"مَفَاعِيلُنْ",
            "emeter": "u---"
        },
        {
            "type": FootType.QABDH,
            "mnemonic": u"مَفَاعِلُنْ",
            "emeter": "u-u-"
        },
        {
            "type": FootType.KAFF,
            "mnemonic": u"مَفَاعِيلُ",
            "emeter": "u--u"
        },
        {
            "type": FootType.HADF,
            "mnemonic": u"فَعُولُنْ",
            "emeter": "u--"
        }
        ]
        self._init(var)

# مُسْتَفْعِلُنْ
class WSWSWWS(Tafiila):
    #varation
    def __init__(self, var=[FootType.SALIM]):
        self.feet = [
        {
            "type": FootType.SALIM,
            "mnemonic": u"مُسْتَفْعِلُنْ",
            "emeter": "--u-"
        },
        {
            "type": FootType.KHABN,
            "mnemonic": u"مُتَفْعِلُنْ",
            "emeter": "u-u-"
        },
        {
            "type": FootType.TAI,
            "mnemonic": u"مُسْتَعِلُنْ",
            "emeter": "-uu-"
        },
        {
            "type": FootType.KHABL,
            "mnemonic": u"مُتَعِلُنْ",
            "emeter": "uuu-"
        },
        {
            "type": FootType.TADIIL,
            "mnemonic": u"مُسْتَفْعِلَانْ",
            "emeter": "--u-:"
        },
        {
            "type": FootType.QATE,
            "mnemonic": u"مَفْعُولُنْ",
            "emeter": "---"
        }
        ]
        self._init(var)

# مُتَفَاعِلُنْ
class WWWSWWS(Tafiila):
    #varation
    def __init__(self, var=[FootType.SALIM]):
        self.feet = [
        {
            "type": FootType.SALIM,
            "mnemonic": u"مُتَفَاعِلُنْ",
            "emeter": "uu-u-"
        },
        {
            "type": FootType.IDHMAR,
            "mnemonic": u"مُتْفَاعِلُنْ",
            "emeter": "--u-"
        },
        {
            "type": FootType.WAQS,
            "mnemonic": u"مُفَاعِلُنْ",
            "emeter": "u-u-"
        },
        {
            "type": FootType.KHAZL,
            "mnemonic": u"مُتْفَعِلُنْ",
            "emeter": "u--"
        },
        {
            "type": FootType.TARFIIL,
            "mnemonic": u"مُتَفَاعِلَاتُنْ",
            "emeter": "uu-u--"
        },
        {
            "type": FootType.TADIIL,
            "mnemonic": u"مُتَفَاعِلَانْ",
            "emeter": "uu-u-:"
        },
        {
            "type": FootType.QATE,
            "mnemonic": u"مُتَفَاعِلْ",
            "emeter": "uu--:"
        },
        {
            "type": FootType.HADAD,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        }
        ]
        self._init(var)

# مُفَاعَلَتُنْ
class WWSWWWS(Tafiila):
    #varation
    def __init__(self, var=[FootType.SALIM]):
        self.feet = [
        {
            "type": FootType.SALIM,
            "mnemonic": u"مُفَاعَلَتُنْ",
            "emeter": "u-uu-"
        },
        {
            "type": FootType.ASAB,
            "mnemonic": u"مُفَاعَلْتُنْ",
            "emeter": "u---"
        },
        {
            "type": FootType.AQL,
            "mnemonic": u"مُفَاعَتُنْ",
            "emeter": "u-u-"
        },
        {
            "type": FootType.NAQS,
            "mnemonic": u"مُفَاعَلْتُ",
            "emeter": "u--u"
        },
        {
            "type": FootType.QATF,
            "mnemonic": u"فَعُولُنْ",
            "emeter": "u--"
        }
        ]
        self._init(var)

# فَاعِلَاتُنْ
class WSWWSWS(Tafiila):
    #varation
    def __init__(self, var=[FootType.SALIM]):
        self.feet = [
        {
            "type": FootType.SALIM,
            "mnemonic": u"فَاعِلَاتُنْ",
            "emeter": "-u--"
        },
        {
            "type": FootType.KHABN,
            "mnemonic": u"فَعِلَاتُنْ",
            "emeter": "uu--"
        },
        {
            "type": FootType.KAFF,
            "mnemonic": u"فَاعِلَاتُ",
            "emeter": "-u-u"
        },
        {
            "type": FootType.ISBAGH,
            "mnemonic": u"فَاعِلَاتَانْ",
            "emeter": "-u--:"
        },
        {
            "type": FootType.HADF,
            "mnemonic": u"فَاعِلُنْ",
            "emeter": "-u-"
        },
        {
            "type": FootType.SHAKL,
            "mnemonic": u"فَعِلَاتُ",
            "emeter": "uu-u"
        },
        {
            "type": FootType.BATR,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        },
        {
            "type": FootType.QASR,
            "mnemonic": u"فَاعِلَانْ",
            "emeter": "-u-:"
        }
        ]
        self._init(var)

# مَفْعُولَاتُ
class WSWSWSW(Tafiila):
    #varation
    def __init__(self, var=[FootType.SALIM]):
        self.feet = [
        {
            "type": FootType.SALIM,
            "mnemonic": u"مَفْعُولَاتُ",
            "emeter": "---u"
        },
        {
            "type": FootType.KHABN,
            "mnemonic": u"مَعُولَاتُ",
            "emeter": "u--u"
        },
        {
            "type": FootType.TAI,
            "mnemonic": u"مَفْعُلَاتُ",
            "emeter": "-u-u"
        },
        {
            "type": FootType.KHABL,
            "mnemonic": u"مَعُلَاتُ",
            "emeter": "-u-u"
        },
        {
            "type": FootType.SALAM,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        },
        {
            "type": FootType.KASHF,
            "mnemonic": u"مَفْعُولُنْ",
            "emeter": "---"
        }

        ]
        self._init(var)
