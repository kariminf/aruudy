#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ar_metre.py
#  processing and detecting the metre of arabic poetery
#
#  Copyright 2019 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
#  2019  Abdelkrime Aries <kariminfo0@gmail.com>
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

sun = u"[\u062A\u062B\u062F\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0644\u0646]"


def normalize(text):
    res = test #result

    # Filtering
    # ===========
    #delete tatweel
    res = re.sub(u"\u0640", "", res)

    # Tashkiil
    # ===========
    # add Fatha to first al-
    res = re.sub(u"^\\s*\u0627\u0644", "\u0627\u064E\u0644", res)
    # add Fatha to any non diacretized char preceeding alif
    res = re.sub(u"([^\u064E\u064F\u0650\u0652\\s])\u0627([^\u064E\u064F\u0650\u0652])", "\\1\u064E\u0627\\2", res)
    #add Damma to any non diacretized char preceeding waw
    res = re.sub(u"([^\u064E\u064F\u0650\u0652\\s])\u0648([^\u064E\u064F\u0650\u0652])", u"\\1\u064F\u0648\\2", res)
    #add Kasra to any non diacretized char preceeding yaa
    res = re.sub(u"([^\u064E\u064F\u0650\u0652\\s])\u064A([^\u064E\u064F\u0650\u0652])", u"\\1\u0650\u064A\\2", res)

    return res


def fix_al(text):
    """Short summary.

    Parameters
    ----------
    text : string
        Arabic text .

    Returns
    -------
    type
        Description of returned object.

    """

    nwtext = text


    #Replace al- with sun character (it can be preceded by prepositions bi- li-)
    nwtext = re.sub(ur'([^\s]\s+|(?:\u0644|\u0628)[\u0650]?)\u0627\u0644(' + sun + ')', ur'\1\2', nwtext)

    #Replace al- with l otherwise
    nwtext = re.sub(ur'([^\s]\s+|(?:\u0644|\u0628).?)\u0627\u0644', ur'\1\u0644', nwtext)
    return nwtext

def fix_awy(text):
    nwtext = text

    return nwtext

def get_cv (text):
    nwtext = text

    #Delete sukuun
    nwtext = re.sub(ur'\u0652', '', nwtext)

    #Shadda replace (no need, it will be considered as a consonent)
    #nwtext = re.sub(ur'(.)\u0651', ur'\1\1', nwtext)

    #space + lam + consonent + shadda
    #nwtext = re.sub(ur'\s\u0644[^\u064B\u064C\u064D]\u0651', u'\u0651', nwtext)

    #Replace fatha, damma & kasra with (V) for vowel
    nwtext = re.sub(ur'[^CV][\u064E\u064F\u0650]', 'V', nwtext)

    #delete fathatayn over alif
    nwtext = re.sub(ur'\u0627\u064B', u'\u0627', nwtext)

    #Replace fathatayn, dammatayn, kasratayn with Vowel follewed by Consonent
    nwtext = re.sub(ur'[^CV][\u064B\u064C\u064D]', 'VC', nwtext)

    #return nwtext
    #alif-alifmaqsora + space + consonent => delete madd
    nwtext = re.sub(ur'[\u0627\u0649]\s+[^V]', 'C', nwtext)

    #Delete space
    nwtext = re.sub(ur'\s', '', nwtext)

    #Replace all what is left as it was a consonent
    nwtext = re.sub(ur'[^CV]', 'C', nwtext)

    nwtext = re.sub(ur'V$', 'VC', nwtext)

    return nwtext

def get_metre (cv):
    metre = cv
    metre = metre.replace("VC", "-")
    metre = metre.replace("V", "u")
    return metre

def get_metre_name(metre):
    for reg in metres:
        match = re.search(r'^'+reg+'$', metre)
        if match:
            return metres.get(reg)
    return "not found"


class Shatr(object):
    def __init__(self, text):
        self.orig = text
        self.norm = text
        self.prosody = text
        self.meter = ""
        self.syllables = ""
        self.bahr = None


class Bayt(object):
    def __init__(self, text, sep="\t"):
        self.original = text
