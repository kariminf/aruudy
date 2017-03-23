#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0,'../')

from poetry import ar_metre

r = u'أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ'
print("original: " + r)

r = ar_metre.ar_filter(r)
r = ar_metre.fix_al(r)
print("filtered: " + r)

r = ar_metre.fix_awy(r)
print("awy fixed: " + r)

r = ar_metre.get_cv(r)
print("metre desc: " + r)

r = ar_metre.get_metre(r)
print("metre: " + r)

r = ar_metre.get_metre_name(r)
print("metre name: " + r)
