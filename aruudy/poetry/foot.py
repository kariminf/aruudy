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
    def __init__(self, id, ar):
        self.id = id
        self.ar = ar
    def __repr__(self):
        return self.id
    def __html__(self):
        return self.ar

class TafiilaType(object):
    """A class with different anomalies (Zuhaf and Illa) happening to the Foot.

    This class can be considered as an enum
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

class TafiilaComp(object):
    def __init__(self, comp):
        self.type = comp["type"]
        self.mnemonic = comp["mnemonic"]
        self.emeter = comp["emeter"]
    def copy(self):
        return TafiilaComp(self.__dict__)

class Tafiila(object):

    def _init(self, var):
        self.aforms = [] # allowed feet
        for form in self.forms:
            if form.type in var:
                self.aforms.append(form)

    def process(self, text_emeter):
        for form in self.aforms:
            if text_emeter.startswith(form.emeter):
                text_foot = form.copy()
                return text_foot, text_emeter[len(form.emeter):]
        return None, None

    def get_form(self, used=True):
        if used:
            return self.aforms[0].copy()
        return self.forms[0].copy()

    def to_dict(used=False):
        if used:
            return self.aforms[0]
        return self.forms[0]


# https://sites.google.com/site/mihfadha/aroudh/14

# فَاعِلُنْ
class WSWWS(Tafiila):
    #varation
    def __init__(self, var=[TafiilaType.SALIM]):
        self.forms = [
        TafiilaComp({
            "type": TafiilaType.SALIM,
            "mnemonic": u"فَاعِلُنْ",
            "emeter": "-u-"
        }),
        TafiilaComp({
            "type": TafiilaType.KHABN,
            "mnemonic": u"فَعِلُنْ",
            "emeter": "uu-"
        }),
        TafiilaComp({
            "type": TafiilaType.TARFIIL,
            "mnemonic": u"فَاعِلَاتُنْ",
            "emeter": "-u--"
        }),
        TafiilaComp({
            "type": TafiilaType.TADIIL,
            "mnemonic": u"فَاعِلَانْ",
            "emeter": "-u-:"
        }),
        TafiilaComp({
            "type": TafiilaType.QATE,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        })
        ]
        self._init(var)

# فَعُولُنْ
class WWSWS(Tafiila):
    #varation
    def __init__(self, var=[TafiilaType.SALIM]):
        self.forms = [
        TafiilaComp({
            "type": TafiilaType.SALIM,
            "mnemonic": u"فَعُولُنْ",
            "emeter": "u--"
        }),
        TafiilaComp({
            "type": TafiilaType.QABDH,
            "mnemonic": u"فَعُولُ",
            "emeter": "u-u"
        }),
        TafiilaComp({
            "type": TafiilaType.HADF,
            "mnemonic": u"فِعَلْ",
            "emeter": "u-"
        }),
        TafiilaComp({
            "type": TafiilaType.BATR,
            "mnemonic": u"فِعْ",
            "emeter": "-"
        }),
        TafiilaComp({
            "type": TafiilaType.QASR,
            "mnemonic": u"فَعُولْ",
            "emeter": "u-:"
        })
        ]
        self._init(var)

# مَفَاعِيلُنْ
class WWSWSWS(Tafiila):
    #varation
    def __init__(self, var=[TafiilaType.SALIM]):
        self.forms = [
        TafiilaComp({
            "type": TafiilaType.SALIM,
            "mnemonic": u"مَفَاعِيلُنْ",
            "emeter": "u---"
        }),
        TafiilaComp({
            "type": TafiilaType.QABDH,
            "mnemonic": u"مَفَاعِلُنْ",
            "emeter": "u-u-"
        }),
        TafiilaComp({
            "type": TafiilaType.KAFF,
            "mnemonic": u"مَفَاعِيلُ",
            "emeter": "u--u"
        }),
        TafiilaComp({
            "type": TafiilaType.HADF,
            "mnemonic": u"فَعُولُنْ",
            "emeter": "u--"
        })
        ]
        self._init(var)

# مُسْتَفْعِلُنْ
class WSWSWWS(Tafiila):
    #varation
    def __init__(self, var=[TafiilaType.SALIM]):
        self.forms = [
        TafiilaComp({
            "type": TafiilaType.SALIM,
            "mnemonic": u"مُسْتَفْعِلُنْ",
            "emeter": "--u-"
        }),
        TafiilaComp({
            "type": TafiilaType.KHABN,
            "mnemonic": u"مُتَفْعِلُنْ",
            "emeter": "u-u-"
        }),
        TafiilaComp({
            "type": TafiilaType.TAI,
            "mnemonic": u"مُسْتَعِلُنْ",
            "emeter": "-uu-"
        }),
        TafiilaComp({
            "type": TafiilaType.KHABL,
            "mnemonic": u"مُتَعِلُنْ",
            "emeter": "uuu-"
        }),
        TafiilaComp({
            "type": TafiilaType.TADIIL,
            "mnemonic": u"مُسْتَفْعِلَانْ",
            "emeter": "--u-:"
        }),
        TafiilaComp({
            "type": TafiilaType.QATE,
            "mnemonic": u"مَفْعُولُنْ",
            "emeter": "---"
        })
        ]
        self._init(var)

# مُتَفَاعِلُنْ
class WWWSWWS(Tafiila):
    #varation
    def __init__(self, var=[TafiilaType.SALIM]):
        self.forms = [
        TafiilaComp({
            "type": TafiilaType.SALIM,
            "mnemonic": u"مُتَفَاعِلُنْ",
            "emeter": "uu-u-"
        }),
        TafiilaComp({
            "type": TafiilaType.IDHMAR,
            "mnemonic": u"مُتْفَاعِلُنْ",
            "emeter": "--u-"
        }),
        TafiilaComp({
            "type": TafiilaType.WAQS,
            "mnemonic": u"مُفَاعِلُنْ",
            "emeter": "u-u-"
        }),
        TafiilaComp({
            "type": TafiilaType.KHAZL,
            "mnemonic": u"مُتْفَعِلُنْ",
            "emeter": "u--"
        }),
        TafiilaComp({
            "type": TafiilaType.TARFIIL,
            "mnemonic": u"مُتَفَاعِلَاتُنْ",
            "emeter": "uu-u--"
        }),
        TafiilaComp({
            "type": TafiilaType.TADIIL,
            "mnemonic": u"مُتَفَاعِلَانْ",
            "emeter": "uu-u-:"
        }),
        TafiilaComp({
            "type": TafiilaType.QATE,
            "mnemonic": u"مُتَفَاعِلْ",
            "emeter": "uu--:"
        }),
        TafiilaComp({
            "type": TafiilaType.HADAD,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        })
        ]
        self._init(var)

# مُفَاعَلَتُنْ
class WWSWWWS(Tafiila):
    #varation
    def __init__(self, var=[TafiilaType.SALIM]):
        self.forms = [
        TafiilaComp({
            "type": TafiilaType.SALIM,
            "mnemonic": u"مُفَاعَلَتُنْ",
            "emeter": "u-uu-"
        }),
        TafiilaComp({
            "type": TafiilaType.ASAB,
            "mnemonic": u"مُفَاعَلْتُنْ",
            "emeter": "u---"
        }),
        TafiilaComp({
            "type": TafiilaType.AQL,
            "mnemonic": u"مُفَاعَتُنْ",
            "emeter": "u-u-"
        }),
        TafiilaComp({
            "type": TafiilaType.NAQS,
            "mnemonic": u"مُفَاعَلْتُ",
            "emeter": "u--u"
        }),
        TafiilaComp({
            "type": TafiilaType.QATF,
            "mnemonic": u"فَعُولُنْ",
            "emeter": "u--"
        })
        ]
        self._init(var)

# فَاعِلَاتُنْ
class WSWWSWS(Tafiila):
    #varation
    def __init__(self, var=[TafiilaType.SALIM]):
        self.forms = [
        TafiilaComp({
            "type": TafiilaType.SALIM,
            "mnemonic": u"فَاعِلَاتُنْ",
            "emeter": "-u--"
        }),
        TafiilaComp({
            "type": TafiilaType.KHABN,
            "mnemonic": u"فَعِلَاتُنْ",
            "emeter": "uu--"
        }),
        TafiilaComp({
            "type": TafiilaType.KAFF,
            "mnemonic": u"فَاعِلَاتُ",
            "emeter": "-u-u"
        }),
        TafiilaComp({
            "type": TafiilaType.ISBAGH,
            "mnemonic": u"فَاعِلَاتَانْ",
            "emeter": "-u--:"
        }),
        TafiilaComp({
            "type": TafiilaType.HADF,
            "mnemonic": u"فَاعِلُنْ",
            "emeter": "-u-"
        }),
        TafiilaComp({
            "type": TafiilaType.SHAKL,
            "mnemonic": u"فَعِلَاتُ",
            "emeter": "uu-u"
        }),
        TafiilaComp({
            "type": TafiilaType.BATR,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        }),
        TafiilaComp({
            "type": TafiilaType.QASR,
            "mnemonic": u"فَاعِلَانْ",
            "emeter": "-u-:"
        })
        ]
        self._init(var)

# مَفْعُولَاتُ
class WSWSWSW(Tafiila):
    #varation
    def __init__(self, var=[TafiilaType.SALIM]):
        self.forms = [
        TafiilaComp({
            "type": TafiilaType.SALIM,
            "mnemonic": u"مَفْعُولَاتُ",
            "emeter": "---u"
        }),
        TafiilaComp({
            "type": TafiilaType.KHABN,
            "mnemonic": u"مَعُولَاتُ",
            "emeter": "u--u"
        }),
        TafiilaComp({
            "type": TafiilaType.TAI,
            "mnemonic": u"مَفْعُلَاتُ",
            "emeter": "-u-u"
        }),
        TafiilaComp({
            "type": TafiilaType.KHABL,
            "mnemonic": u"مَعُلَاتُ",
            "emeter": "-u-u"
        }),
        TafiilaComp({
            "type": TafiilaType.SALAM,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        }),
        TafiilaComp({
            "type": TafiilaType.KASHF,
            "mnemonic": u"مَفْعُولُنْ",
            "emeter": "---"
        })

        ]
        self._init(var)
