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

class BahrError (Exception):
	def __init__(self, name):
		Exception.__init__(self, "Bahr does not have an attribute called: " + name)

class Bahr(object):
    def __init__(self, info):
        self.keys = []
        for key in info:
            setattr(self, key, info[key])
            self.keys.append(key)

    def test_property(key, value):
        if not key in keys:
            raise BahrError(key)
        return (self[key] == value)

    def get_value(key):
        if not key in keys:
            raise BahrError(key)
        return self[key]

    def to_dict():
        dict = {}
        for key in self.keys:
            dict[key] = self[key]
        return dict

    def compare(ameter):#use lavenstein distance
        return 0

buhuur = [
    Bahr({
        "aname": u"طويل",
        "lname": "long",
        "trans": "ṭawīl",
        "ameter": "ccvcv ccvcvcv ccvcv ccvccv",
        "lmeter": "u-x u-x- u-x u-u-",
        "key": u"طويلٌ له دون البحور فضائلٌ  فعولن مفاعيلن فعولن مفاعلن"
    }),
    Bahr({
        "aname": u"مديد",
        "lname": "protracted",
        "trans": "madīd",
        "ametre": "cvccvcv cvccv cvccvcv",
        "lmetre": "xu-- xu- xu--",
        "key": u"لمديد الشعر عندي صفاتُ  فاعلاتن فاعلن فاعلاتن"
    }),
    Bahr({
        "aname": u"بسيط",
        "lname": "spread-out",
        "trans": "basīṭ",
        "ametre": "cvcvccv cccv cvcvccv cccv",
        "lmetre": "x-u- xu- --u- w-",
        "key": u"إن البسيط لديه يبسط الأملُ  مستفعلن فعلن مستفعلن فعلن"
    }),
    Bahr({
        "aname": u"",
        "lname": "",
        "trans": "",
        "ametre": "",
        "lmetre": "",
        "key": u""
    }),
    Bahr({
        "aname": u"",
        "lname": "",
        "trans": "",
        "ametre": "",
        "lmetre": "",
        "key": u""
    }),
    Bahr({
        "aname": u"",
        "lname": "",
        "trans": "",
        "ametre": "",
        "lmetre": "",
        "key": u""
    }),
    Bahr({
        "aname": u"",
        "lname": "",
        "trans": "",
        "ametre": "",
        "lmetre": "",
        "key": u""
    }),
    Bahr({
        "aname": u"",
        "lname": "",
        "trans": "",
        "ametre": "",
        "lmetre": "",
        "key": u""
    }),
    Bahr({
        "aname": u"",
        "lname": "",
        "trans": "",
        "ametre": "",
        "lmetre": "",
        "key": u""
    }),
]


def name_type(name):
    if re.match("^[a-zA-Z]", name):
        return "lname"
    else:
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
            else:
                return b
    return None
