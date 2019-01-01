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
        "ename": "long",
        "trans": "ṭawīl",
        "ameter": "ccvcv ccvcvcv ccvcv ccvccv",
        "emeter": "u-x u-x- u-x u-u-",
        "key": u"طويلٌ له دون البحور فضائلٌ  فعولن مفاعيلن فعولن مفاعلن"
    }),
    Bahr({
        "aname": u"مديد",
        "ename": "protracted",
        "trans": "madīd",
        "ametre": "cvccvcv cvccv cvccvcv",
        "emetre": "xu-- xu- xu--",
        "key": u"لمديد الشعر عندي صفاتُ  فاعلاتن فاعلن فاعلاتن"
    }),
    Bahr({
        "aname": u"بسيط",
        "ename": "spread-out",
        "trans": "basīṭ",
        "ametre": "cvcvccv cccv cvcvccv cccv",
        "emetre": "x-u- xu- --u- w-",
        "key": u"إن البسيط لديه يبسط الأملُ  مستفعلن فعلن مستفعلن فعلن"
    }),
    Bahr({
        "aname": u"وافر",
        "ename": "abundant",
        "trans": "wāfir",
        "ametre": "u-w- u-w- u--",
        "emetre": "ccvcccv ccvcccv ccvcv",
        "key": u"بحور الشعر وافرها جميل  مفاعلتن مفاعلتن فعولن"
    }),
    Bahr({
        "aname": u"كامل",
        "ename": "complete",
        "trans": "kāmil",
        "ametre": "cccvccv cccvccv cccvccv",
        "emetre": "w-u- w-u- w-u-",
        "key": u"كمل الجمال من البحور الكامل متفاعلن متفاعلن متفاعلن"
    }),
    Bahr({
        "aname": u"هزج",
        "ename": "trilling",
        "trans": "hazaj",
        "ametre": "ccvcvcv ccvcvcv",
        "emetre": "u--x u--x",
        "key": u"على الأهزاج تسهيل      مفاعيلن مفاعيلن"
    }),
    Bahr({
        "aname": u"رجز",
        "ename": "trembling",
        "trans": "rajaz",
        "ametre": "cvcvccv cvcvccv cvcvccv",
        "emetre": "x-u- x-u- x-u- x-u-",
        "key": u"في أبحر الأرجاز بحرٌ يسهل   مستفعلن مستفعلن مستفعلن"
    }),
    Bahr({
        "aname": u"رمل",
        "ename": "trotting",
        "trans": "ramal",
        "ametre": "cvccvcv cvccvcv cvccv",
        "emetre": "xu-- xu-- xu-",
        "key": u"رمل الأبحر ترويه الثقات فاعلاتن فاعلاتن فاعلاتن"
    }),
    Bahr({
        "aname": u"سريع",
        "ename": "swift",
        "trans": "sarīʿ",
        "ametre": "cvcvccv cvcvccv cvccv",
        "emetre": "xxu- xxu- -u-",
        "key": u"بحرٌ سريع ماله ساحل مستفعلن مستفعلن فاعلن"
    }),
    Bahr({
        "aname": u"منسرح",
        "ename": "quick-paced",
        "trans": "mnsariħ",
        "ametre": "cvcvccv cvcvcv cvcccv", #TODO verify
        "emetre": "x-u- -x-u -uu-",
        "key": u"منسرح فيه يضرب المثل    مستفعلن مفعولات مفتعلن"
    }),
    Bahr({
        "aname": u"خفيف",
        "ename": "light",
        "trans": "khafīf",
        "ametre": "cvccvcv cvcvccv cvccvcv",
        "emetre": "xu-x --u- xu-x",
        "key": u"يا خفيفاً خفّت به الحركات   فاعلاتن مستفعلن فاعلاتن"
    }),
    Bahr({
        "aname": u"مضارع",
        "ename": "similar",
        "trans": "muḍāriʿ",
        "ametre": "u-xx -u--",
        "emetre": "ccvcvcv cvccvcv",
        "key": u"تعدّ المضارعات  مفاعيلُ فاعلاتن"
    }),
    Bahr({
        "aname": u"مقتضب",
        "ename": "untrained",
        "trans": "muqtaḍab",
        "ametre": "cvccvc cvcccv",
        "emetre": "xu-u -uu-",
        "key": u"اقتضب كما سألوا مفعلات مفتعلن"
    }),
    Bahr({
        "aname": u"مجتث",
        "ename": "cut-off",
        "trans": "mujtathth",
        "ametre": "cvcvccv cvccvcv",
        "emetre": "x-u- xu--",
        "key": u"أن جثت الحركات  مستفعلن فاعلاتن"
    }),
    Bahr({
        "aname": u"متقارب",
        "ename": "nearing",
        "trans": "mutaqārib",
        "ametre": "ccvcv ccvcv ccvcv ccv",
        "emetre": "u-x u-x u-x u-",
        "key": u"عن المتقارب قال الخليل      فعولن فعولن فعولن فعول"
    }),
    Bahr({
        "aname": u"متدارك",
        "ename": "overtaking",
        "trans": "mutadārik",
        "ametre": "",
        "emetre": "xu- xu- xu- (xu-)", # - can be substituted for u u)
        "key": u"حركات المحدث تنتقل  فعلن فعلن فعلن فعل"
    })
]


def name_type(name):
    if re.match("^[a-zA-Z]", name):
        return "ename"
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

def _get_values(label):
	values = []
	for b in buhuur:
        values.append(b[label])
	return values

def arabic_names():
	return _get_values("aname")

def english_names():
	return _get_values("ename")

def trans_names():
	return _get_values("trans")
