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

TASHKIIL = [u"ِ", u"ُ", u"َ", u"ْ"]
TANWIIN = [u"ٍ", u"ٌ", u"ً"]
SHADDA = u"ّ"
# unknown diacretic (haraka)
UHARAKA = u"\u0653"

# Add shdda and madda
# Madda, in our case, is used to indicate an unknown haraka
DIAC = UHARAKA.join(SHADDA).join(TASHKIIL).join(TANWIIN)

# sun letters in arabic
SUN = u"[تثدذرزسشصضطظلن]"

# Sticky prepositions (bi-, li-)kasra? or (ka-, fa-, wa-)fatha?
# kasra and fatha can be madda in case there is no tashkiil
SPREP = "[\u0644\u0628][\u0650%s]?|[\u0643\u0641\u0648][\u064E%s]?" % (UHARAKA, UHARAKA)

# alif in the middle of sentence
# DORJ = spaces or (bi-, li-)kasra? or (ka-, fa-, wa-)fatha?
DORJ = u"[^\\s]\\s+|%s" % SPREP

# ahruf al3illa: alif, alif maqsura, waw, yaa
ILLA = u"[اىوي]"

TATWEEL = {
    u"\u064E": u"\u064E\u0627",
    u"\u064F": u"\u064F\u0648",
    u"\u0650": u"\u0650\u064A",
}
