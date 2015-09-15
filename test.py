#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  after creating database, you can try this to test the program
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
import os
from db.litebase import liteBase
import pattern
import arudquery
#~ import wazn

if __name__ == '__main__':
	
	dbpath = os.path.realpath('test/arabicdict.sqlite')
	print dbpath
	srcdb = liteBase(dbpath)
	tab = srcdb.getTable('nouns')
	
	queryengine = arudquery.ArQuery()
	arpattern = pattern.Pattern(u'مَفْعَل')
	
	queryengine.setPattern(arpattern)#wazn.V3I4R3B
	queryengine.setEnd(u'ب')
	
	conditions = queryengine.getResult()
	print conditions
	
	rows = tab.getData(conditions)
	for row in rows:
		word = tab.getColumnIndex('word')
		patt = tab.getColumnIndex('pattern')
		print row[word] + "   " + row[patt]
