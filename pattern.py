#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pattern.py
#  Used to manage Patterns
#  
#  Copyright 2015 Abdelkrime Aries <kariminfo0@gmail.com>
#  Copyright 2014 DzCoding group <dzcoding@googlegroups.com>
#  
#  ---- AUTHORS ----
#  2014-2015    Abdelkrime Aries <kariminfo0@gmail.com>
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

TASHKIIL	= [u'ِ', u'ُ', u'َ', u'ْ']
TANWIIN		= [u'ٍ', u'ٌ', u'ً']

class Pattern(object):
	def __init__(self, definition):
		self.__label = definition
		self.__unvocal = unvocalize(definition)
		self.__code = getPattern(definition)
		self.__start = extractAddition(self.__unvocal)
		self.__pos3in = self.__unvocal.index(u'ع')
	
			
	def getPatternCode(self):
		return self.__code
		
	def getPatternLabel(self):
		return self.__label
		
	def getUnvocalized(self):
		return self.__unvocal
	
	def getStart(self):
		return self.__start
	
	def getPos3in(self):
		return self.__pos3in

		
def getPattern(word):
	
	tmpPattern = u''
	
	for char in word:

		if char in TASHKIIL:
			tmpPattern += u'' + str(TASHKIIL.index(char)+1)
			
		elif char in TANWIIN:
			tmpPattern += u'0'
			
		elif char == u'ّ':
			tmpPattern += u'x'

		elif char == u'آ':
			if len(tmpPattern)>0 and tmpPattern[-1]== u'C':
				tmpPattern += u'3'
			tmpPattern += u'30'
		
		elif char == u'ا' or char == u'ى':
			if len(tmpPattern)>0 and tmpPattern[-1]== u'C':
				tmpPattern += u'3'
			tmpPattern += u'0'
			
		elif char == u'ﻻ':
			tmpPattern += u'30'
			
		else:
			tmpPattern += u'C'
				
	#~ tmp = u''
	#~ finalPattern = u''
	#~ for char in tmpPattern:
		#~ if char == u'C' and len(tmp)>0:
			#~ if tmp[0] == u'C':
				#~ if len(tmp)==1:
					#~ finalPattern += u'0'
				#~ else:
					#~ finalPattern += tmp[1:]
			#~ else:
				#~ finalPattern += tmp
			#~ tmp = u''
		#~ tmp += char
		#~ 
	#~ if tmp[0] == u'C':
		#~ if len(tmp)==1:
			#~ finalPattern += u'0'
		#~ else:
			#~ finalPattern += tmp[1:]
	#~ else:
		#~ finalPattern += tmp
	finalPattern = tmpPattern
	
	finalPattern = finalPattern.replace('CC', '0C')
	if finalPattern[-1]==u'C':
		finalPattern += u'0'
	finalPattern = finalPattern.replace('C', '')
	if finalPattern[-1]==u'x':
		finalPattern += u'0'
	finalPattern = finalPattern.replace('x', '4')

	return finalPattern


def unvocalize(word):
	diac = u'ّ'.join(TASHKIIL).join(TANWIIN)
	return re.sub(ur'[%s]' % diac, "", word)


def extractAddition(unvoclized):
	add = unvoclized.split(u'ف')
	return add[0]
	
if __name__ == '__main__':
	import pattern
	F3A3L = pattern.Pattern(u'انْفَعَل')
	print F3A3L.getPatternCode()
	print F3A3L.getUnvocalized()
	print F3A3L.getStart()
	
