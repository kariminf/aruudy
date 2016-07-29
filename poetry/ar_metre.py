#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  Copyright 2016 Abdelkrime Aries <kariminfo0@gmail.com>
#  
#  ---- AUTHORS ----
#  2016	Abdelkrime Aries <kariminfo0@gmail.com>
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
# 
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   

import re

# x = [u-]
# 
metres =	{
    "u-[u-]u-[u-]-u-[u-]u-u-": "tawiil",
    "[u-]u-[u-]u-[u-]u-": "madiid",
    "[u-]-u-[u-]u-[u-]-u-uu-": "basiit",
    "(?:-|uu)-u-(?:-|uu)-u-(?:-|uu)-u-": "kamil",
    "u-(?:-|uu)-u-(?:-|uu)-u--": "wafir",
    "u--[u-]u--[u-]": "hazj",
    "[u-]-u-[u-]-u-[u-]-u-": "rajz",
    "[u-]u-[u-]u-[u-]u-": "raml",
    "[u-][u-]u-[u-][u-]u--u-": "sarii3",
    "[u-]-u--[u-]-u-uu-": "munsari7",
    "[u-]u-[u-]-u-[u-]u-": "khafiif",
    "u-[u-][u-]-u--": "mudhari3",
    "[u-]u-u-uu-": "muqtadib",
    "[u-]-u-[u-]u-": "mujtath",
    "-u?u--u?u--u?u-": "mutadaarik",
    "u-[u-]u-[u-]u-[u-]u-": "mutaqaarib"
}

def fix_al(text):
	nwtext = text
	#Replace al- with C if preceded by fatha, damma or kasra followed by space
	nwtext = re.sub(ur'([^\s]\s+)\u0627\u0644', ur'\1\u0644', nwtext)
	#Replace al- with VC if it is in the first line
	nwtext = re.sub(ur'^\s*\u0627\u0644', ur'\u0627\u064E\u0644', nwtext)
	return nwtext
	
def fix_awy(text):
	nwtext = text
	#alif
	nwtext = re.sub(ur'([^\u064E\u064F\u0650\u0652])\u0627([^\u064E\u064F\u0650\u0652])', ur'\1\u064E\u0627\2', nwtext) 
	
	#waw
	nwtext = re.sub(ur'([^\u064E\u064F\u0650\u0652])\u0648([^\u064E\u064F\u0650\u0652])', ur'\1\u064F\u0648\2', nwtext) 
	
	#yaa
	nwtext = re.sub(ur'([^\u064E\u064F\u0650\u0652])\u064A([^\u064E\u064F\u0650\u0652])', ur'\1\u0650\u064A\2', nwtext) 
	
	return nwtext
	
def get_cv (ar_word):
	new_word = ar_word
	
	#Delete sukuun and tatweel and spaces
	new_word = re.sub(ur'[\u0652\u0640\s]', '', new_word)
	
	#Shadda don't need to be replaced because it will be replaced after
	#Replace fatha, damma & kasra with (V) for vowel
	new_word = re.sub(ur'[^CV][\u064E\u064F\u0650]', 'V', new_word) 
	
	#Replace fathatayn, dammatayn, kasratayn with Vowel follewed by Consonent
	new_word = re.sub(ur'[^CV][\u064B\u064C\u064D]', 'VC', new_word)

	#Replace all what is left as it was a consonent
	new_word = re.sub(ur'[^CV]', 'C', new_word)
	
	new_word = re.sub(ur'V$', 'VC', new_word)
	
	return new_word
	
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
		
if __name__ == '__main__':
	
	r = u'أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ'
	#r = u'الأُمُّ مَـدْرَسَــةٌ إِذَا أَعْـدَدْتَـهَـا'
	r = u'لَيْـسَ يَرْقَـى الأَبْنَـاءُ فِـي أُمَّـةٍ مَـا'
	r = u'العَيْـشُ مَاضٍ فَأَكْـرِمْ وَالِدَيْـكَ بِـهِ'
	r = u'أَحِـنُّ إِلَى الكَـأْسِ التِي شَـرِبَتْ بِهَـا'
	r = u'أَطِــعِ الإِلَــهَ كَـمَـا أَمَــرْ'
	r = u'أَعْـطِ أَبَـاكَ النِّصْـفَ حَيًّـا وَمَيِّتـاً'
	r = u'تَحَمَّـلْ عَـنْ أَبِيْـكَ الثِّقْـلَ يَوْمـاً'
	r = u'إِذَا كَـانَ رَبُّ البَيْـتِ بِالطَّبْـلِ ضَـارِباً'
	print(r)
	
	r = fix_al(r)
	print(r)
	
	r = fix_awy(r)
	print(r)
	
	r = get_cv(r)
	print(r)
	
	r = get_metre(r)
	print(r)
	
	r = get_metre_name(r)
	print(r)
