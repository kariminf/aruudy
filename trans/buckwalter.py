#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  buckwalter.py
#  A  class to handle buckwalter translateration
#  
#  Copyright 2015 Abdelkrime Aries <kariminfo0@gmail.com>
#  
#  ---- AUTHORS ----
#  2015	Abdelkrime Aries <kariminfo0@gmail.com>
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


trans =	{
		u"\u0627": "A", # alif
		u"\u0628": "b", # ba
		u"\u062A": "t", # ta
		u"\u062B": "v", # tha
		u"\u062C": "j", # jim
		u"\u062D": "H", # Ḥa
		u"\u062E": "x", # kha
		u"\u062F": "d", # dal
		u"\u0630": "*", # dhal
		u"\u0631": "r", # ra
		u"\u0632": "z", # zin
		u"\u0633": "s", # sin
		u"\u0634": "$", # shin
		u"\u0635": "S", # ṣad
		u"\u0636": "D", # Ḍad
		u"\u0637": "T", # Ṭa
		u"\u0638": "Z", # Ẓa
		u"\u0639": "E", # 'Ayn
		u"\u063A": "g", # ghayn
		u"\u0641": "f", # fa
		u"\u0642": "q", # qaf
		u"\u0643": "k", # kaf
		u"\u0644": "l", # lam
		u"\u0645": "m", # mim
		u"\u0646": "n", # nun
		u"\u0647": "h", # ha
		u"\u0648": "w", # waw
		u"\u064A": "y", # ya
		#hamza
		u"\u0621": "'", # lone hamza
		u"\u0623": ">", # hamza on alif
		u"\u0625": "<", # hamza below alif
		u"\u0624": "&", # hamza on waw
		u"\u0626": "}", # hamza on ya
		#alif
		u"\u0622": "|", # madda on alif
		u"\u0671": "{", # alif alwasla
		u"\u0670": "`", # dagger alif
		u"\u0649": "Y", # alif maqsura
		#harakat
		u"\u064E": "a", # fatha
		u"\u064F": "u", # Damma
		u"\u0650": "i", # kasra
		u"\u064B": "F", # fathatayn
		u"\u064C": "N", # dammatayn
		u"\u064D": "K", # kasratayn
		u"\u0651": "~", # shadda
		u"\u0640": "_", # tatwil
		#others
		u"\u0629": "p", # ta marbuta
		u"\u0652": "o", # sukun
}


class Buckwalter(object):
	def __init__(self, definition):
		this.yay = ''
	
	@staticmethod
	def translaterate(word):
		res = ""
		if len(word) < len(trans):
			for char in word:
				res += trans.get(char, char)
		else:
			res = word
			for k,v in trans.iteritems():
				res = res.replace(k, v)
				
		return res

	@staticmethod
	def untranslaterate(word):
		res = word
		for k,v in trans.iteritems():
			res = res.replace(v, k)
				
		return res
		
		
if __name__ == '__main__':
	from buckwalter import Buckwalter
	print Buckwalter.translaterate(u'هذا البرنامج يعطينا نطق الحروف')
	print Buckwalter.untranslaterate('h*A AlbrnAmj yETynA nTq AlHrwf')
