#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ar_metre.py
#  processing and detecting the metre of arabic poetery
#
#  Copyright 2016 Abdelkrime Aries <kariminfo0@gmail.com>
#  
#  ---- AUTHORS ----
#  2016	Abdelkrime Aries <kariminfo0@gmail.com>
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

def ar_filter(text):
	nwtext = text
	
	#delete tatweel
	nwtext = re.sub(ur'\u0640', '', nwtext)
	
	#delete a lot of chars
	#nwtext = re.sub(ur'[^\u0621-\u063A\u0641-\u0652]', '', nwtext)
	
	return nwtext
	
def fix_al(text):
	nwtext = text
	#al- in the first sentence: add fatha
	nwtext = re.sub(ur'^\s*\u0627\u0644', ur'\u0627\u064E\u0644', nwtext)
	
	#Replace al- with sun character (it can be preceded by prepositions bi- li-)
	nwtext = re.sub(ur'([^\s]\s+|(?:\u0644|\u0628)[\u0650]?)\u0627\u0644(' + sun + ')', ur'\1\2', nwtext)
	
	#Replace al- with l otherwise
	nwtext = re.sub(ur'([^\s]\s+|(?:\u0644|\u0628).?)\u0627\u0644', ur'\1\u0644', nwtext)
	return nwtext
	
def fix_awy(text):
	nwtext = text
	#alif
	nwtext = re.sub(ur'([^\u064E\u064F\u0650\u0652])\u0627([^\u064E\u064F\u0650\u0652])', ur'\g<1>\u064E\u0627\g<2>', nwtext) 
	
	#waw
	nwtext = re.sub(ur'([^\u064E\u064F\u0650\u0652])\u0648([^\u064E\u064F\u0650\u0652])', ur'\1\u064F\u0648\2', nwtext) 
	
	#yaa
	nwtext = re.sub(ur'([^\u064E\u064F\u0650\u0652])\u064A([^\u064E\u064F\u0650\u0652])', ur'\1\u0650\u064A\2', nwtext) 
	
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
		
if __name__ == '__main__':
	
	r = u'أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ'
	#r = u'الأُمُّ مَـدْرَسَــةٌ إِذَا أَعْـدَدْتَـهَـا'
	#r = u'لَيْـسَ يَرْقَـى الأَبْنَـاءُ فِـي أُمَّـةٍ مَـا' #pblm
	#r = u'العَيْـشُ مَاضٍ فَأَكْـرِمْ وَالِدَيْـكَ بِـهِ'
	#r = u'أَحِـنُّ إِلَى الكَـأْسِ التِي شَـرِبَتْ بِهَـا' #pblm
	#r = u'أَطِــعِ الإِلَــهَ كَـمَـا أَمَــرْ' #pblm
	#r = u'أَعْـطِ أَبَـاكَ النِّصْـفَ حَيًّـا وَمَيِّتـاً' #pblm
	#r = u'تَحَمَّـلْ عَـنْ أَبِيْـكَ الثِّقْـلَ يَوْمـاً'
	#r = u'إِذَا كَـانَ رَبُّ البَيْـتِ بِالطَّبْـلِ ضَـارِباً'
	print(r)
	
	r = ar_filter(r)
	
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
