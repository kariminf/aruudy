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

SALIM = 0
# zuhaf 2nd
IDHMAR = 1
WAQS = 2
KHABN = 3
# zuhaf 4th
TAI = 4
# zuhaf 5th
ASAB = 5
AQL = 6
QABDH = 7
# zuhaf 7th
KAFF = 8
# zuhaf 2nd + 4th
KHABL = 9
# zuhaf 2nd + 4th
KHAZL = 10
# zuhaf 2nd + 7th
SHAKL = 11
# zuhaf 5th + 7th
NAQS = 12
#illa
TARFIIL = 13
IDALA = TADIIL = 14
ISBAGH = 15
HADF = 16
QATE = 17
BATR = 18
QASR = 19
QATF = 20
HADAD = 21
SALAM = 22
KASHF = 23

ZUHAF_ILLA = {
SALIM: u"سالم",
IDHMAR: u"إضمار",
WAQS: u"وقص",
KHABN: u"خبن",
TAI: u"طيّ",
ASAB: u"عصب",
AQL: u"عقل",
QABDH: u"قبض",
KAFF: u"كفّ",
KHABL: u"خبْل",
KHAZL: u"خزل",
SHAKL: u"شكل",
NAQS: u"نقص",
TARFIIL: u"ترفيل",
IDALA: u"تذييل",
ISBAGH: u"إسباغ",
HADF: u"حذف",
QATE: u"قطع",
BATR: u"بتر",
QASR: u"قصر",
QATF: u"قطف",
HADAD: u"حذذ",
SALAM: u"صلم",
KASHF: u"كشف"
}


class Tafiila(object):

    def init(self, var):
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

# https://sites.google.com/site/mihfadha/aroudh/14

# فَاعِلُنْ
class WSWWS(Tafiila):
    #varation
    def __init__(self, var=[SALIM]):
        self.feet = [
        {
            "type": SALIM,
            "mnemonic": u"فَاعِلُنْ",
            "emeter": "-u-"
        },
        {
            "type": KHABN,
            "mnemonic": u"فَعِلُنْ",
            "emeter": "uu-"
        },
        {
            "type": TARFIIL,
            "mnemonic": u"فَاعِلَاتُنْ",
            "emeter": "-u--"
        },
        {
            "type": IDALA,
            "mnemonic": u"فَاعِلَانْ",
            "emeter": "-u-:"
        },
        {
            "type": QATE,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        }
        ]
        self.init(var)

# فَعُولُنْ
class WWSWS(Tafiila):
    #varation
    def __init__(self, var=[SALIM]):
        self.feet = [
        {
            "type": SALIM,
            "mnemonic": u"فَعُولُنْ",
            "emeter": "u--"
        },
        {
            "type": QABDH,
            "mnemonic": u"فَعُولُ",
            "emeter": "u-u"
        },
        {
            "type": HADF,
            "mnemonic": u"فِعَلْ",
            "emeter": "u-"
        },
        {
            "type": BATR,
            "mnemonic": u"فِعْ",
            "emeter": "-"
        },
        {
            "type": QASR,
            "mnemonic": u"فَعُولْ",
            "emeter": "u-:"
        }
        ]
        self.init(var)

# مَفَاعِيلُنْ
class WWSWSWS(Tafiila):
    #varation
    def __init__(self, var=[SALIM]):
        self.feet = [
        {
            "type": SALIM,
            "mnemonic": u"مَفَاعِيلُنْ",
            "emeter": "u---"
        },
        {
            "type": QABDH,
            "mnemonic": u"مَفَاعِلُنْ",
            "emeter": "u-u-"
        },
        {
            "type": KAFF,
            "mnemonic": u"مَفَاعِيلُ",
            "emeter": "u--u"
        },
        {
            "type": HADF,
            "mnemonic": u"فَعُولُنْ",
            "emeter": "u--"
        }
        ]
        self.init(var)

# مُسْتَفْعِلُنْ
class WSWSWWS(Tafiila):
    #varation
    def __init__(self, var=[SALIM]):
        self.feet = [
        {
            "type": SALIM,
            "mnemonic": u"مُسْتَفْعِلُنْ",
            "emeter": "--u-"
        },
        {
            "type": KHABN,
            "mnemonic": u"مُتَفْعِلُنْ",
            "emeter": "u-u-"
        },
        {
            "type": TAI,
            "mnemonic": u"مُسْتَعِلُنْ",
            "emeter": "-uu-"
        },
        {
            "type": KHABL,
            "mnemonic": u"مُتَعِلُنْ",
            "emeter": "uuu-"
        },
        {
            "type": IDALA,
            "mnemonic": u"مُسْتَفْعِلَانْ",
            "emeter": "--u-:"
        },
        {
            "type": QATE,
            "mnemonic": u"مَفْعُولُنْ",
            "emeter": "---"
        }
        ]
        self.init(var)

# مُتَفَاعِلُنْ
class WWWSWWS(Tafiila):
    #varation
    def __init__(self, var=[SALIM]):
        self.feet = [
        {
            "type": SALIM,
            "mnemonic": u"مُتَفَاعِلُنْ",
            "emeter": "uu-u-"
        },
        {
            "type": IDHMAR,
            "mnemonic": u"مُتْفَاعِلُنْ",
            "emeter": "--u-"
        },
        {
            "type": WAQS,
            "mnemonic": u"مُفَاعِلُنْ",
            "emeter": "u-u-"
        },
        {
            "type": KHAZL,
            "mnemonic": u"مُتْفَعِلُنْ",
            "emeter": "u--"
        },
        {
            "type": TARFIIL,
            "mnemonic": u"مُتَفَاعِلَاتُنْ",
            "emeter": "uu-u--"
        },
        {
            "type": TADIIL,
            "mnemonic": u"مُتَفَاعِلَانْ",
            "emeter": "uu-u-:"
        },
        {
            "type": QATE,
            "mnemonic": u"مُتَفَاعِلْ",
            "emeter": "uu--:"
        },
        {
            "type": HADAD,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        }
        ]
        self.init(var)

# مُفَاعَلَتُنْ
class WWSWWWS(Tafiila):
    #varation
    def __init__(self, var=[SALIM]):
        self.feet = [
        {
            "type": SALIM,
            "mnemonic": u"مُفَاعَلَتُنْ",
            "emeter": "u-uu-"
        },
        {
            "type": ASAB,
            "mnemonic": u"مُفَاعَلْتُنْ",
            "emeter": "u---"
        },
        {
            "type": AQL,
            "mnemonic": u"مُفَاعَتُنْ",
            "emeter": "u-u-"
        },
        {
            "type": NAQS,
            "mnemonic": u"مُفَاعَلْتُ",
            "emeter": "u--u"
        },
        {
            "type": QATF,
            "mnemonic": u"فَعُولُنْ",
            "emeter": "u--"
        }
        ]
        self.init(var)

# فَاعِلَاتُنْ
class WSWWSWS(Tafiila):
    #varation
    def __init__(self, var=[SALIM]):
        self.feet = [
        {
            "type": SALIM,
            "mnemonic": u"فَاعِلَاتُنْ",
            "emeter": "-u--"
        },
        {
            "type": KHABN,
            "mnemonic": u"فَعِلَاتُنْ",
            "emeter": "uu--"
        },
        {
            "type": KAFF,
            "mnemonic": u"فَاعِلَاتُ",
            "emeter": "-u-u"
        },
        {
            "type": ISBAGH,
            "mnemonic": u"فَاعِلَاتَانْ",
            "emeter": "-u--:"
        },
        {
            "type": HADF,
            "mnemonic": u"فَاعِلُنْ",
            "emeter": "-u-"
        },
        {
            "type": SHAKL,
            "mnemonic": u"فَعِلَاتُ",
            "emeter": "uu-u"
        },
        {
            "type": BATR,
            "mnemonic": u"فِعْلُنْ",
            "emeter": "--"
        },
        {
            "type": QASR,
            "mnemonic": u"فَاعِلَانْ",
            "emeter": "-u-:"
        }
        ]
        self.init(var)

# مَفْعُولَاتْ
# normaly, it is used in sarii, but it is used as fa3ilun

if __name__ == '__main__':
    c = CVCCV([SALIM, KHABN, QATE])
    print c.process("--u--u--u")
