#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  arudquery.py
#  Used to build a query for words search, using the pattern, the word's
#  ending, etc.
#  
#  Copyright 2014 DzCoding group <dzcoding@googlegroups.com>
#  
#  ---- AUTHORS ----
#  2014	Abdelkrime Aries <kariminfo0@gmail.com>
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

import pattern

WORD = u'word'
PATTERN = u'pattern'

class ArQuery(object):
	def __init__(self):
		self.initiate()

	def initiate(self):
		self.__end = u''
		self.__pattern = None
	
	def setPattern(self, thepattern):
		if not isinstance(thepattern, pattern.Pattern):
			return
		self.__pattern = thepattern
	
	def setEnd(self, ending):
		self.__end = ending
	
	def getResult(self):
		result = []
		if self.__pattern:
			patterncode = self.__pattern.getPatternCode()
			tmp = u"(pattern='%s'" % patterncode
			pos = self.__pattern.getPos3in()
			patterncode = patterncode[0:pos] + u'0' + patterncode[pos+1:]
			tmp += u" OR pattern='%s')" % patterncode
			result.append(tmp)
			start = self.__pattern.getStart()
			beginlen = len(start)
			if beginlen>0:
				tmp = u"substr(%s,1,%s)='%s'" % (WORD, str(beginlen), start)
				result.append(tmp)
			
		if len(self.__end) > 0:
			endlen = len(self.__end)
			tmp = u"substr(%s,length(%s) - %s,%s)='%s'" % (WORD, WORD, str(endlen-1), str(endlen), self.__end)
			result.append(tmp)
		return result


if __name__ == '__main__':
	import arudquery
	import wazn
	q = ArQuery()
	q.setPattern(pattern.Pattern(u'مٌسْتَفْعَل'))
	t = q.getResult()
	print t
	
