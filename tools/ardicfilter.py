#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ardicfilter.py
#  Used to create the database from another which contains only the words vocalised and not vocalized
#  
#  Copyright 2015 Abdelkrime Aries <kariminfo0@gmail.com>
#  
#  ---- AUTHORS ----
#  2015    Abdelkrime Aries <kariminfo0@gmail.com>
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

import sys
import os
sys.path.insert(0,'../')

import re
from db import litebase
from trans.buckwalter import Buckwalter
import pattern

	
if __name__ == '__main__':

	# 
	'''theword = "AbotAE"
	theword_u = "AbtAE"
	print distance(theword, "AfotaAEa")
	print getTemplate(theword, theword_u)
	exit()'''
	srcdb = litebase.liteBase(os.path.realpath('../test/ardic.sqlite'))
		
	dstdb = litebase.liteBase(os.path.realpath('../test/words.sqlite'))
	
	tab = litebase.liteTable()
	tab.beginTable("words")
	tab.addColumn('id', litebase.litePK_INT_INC(), u'', False)
	tab.addColumn('word', litebase.liteVARCHAR(20), u'DEFAULT NULL', True)
	tab.addColumn('pattern', litebase.liteVARCHAR(20), u'DEFAULT NULL', True)
	tab.addColumn('vocalized', litebase.liteVARCHAR(20), u'DEFAULT NULL', True)
	tab.endTable()
	# print tab.getSqlQuery()
	
	dstdb.addTable(tab)
	
	src = srcdb.getTable('ardict')
	
	print src.getSqlQuery()
	
	rows = src.getData()
	
	vocalized = src.getColumnIndex('vocal')
	unvocalized = src.getColumnIndex('unvocal')
	i=0
	for row in rows:
		i = i + 1
		print "processing " + row[unvocalized]
		wtranslate = Buckwalter.translaterate(row[vocalized])
		#print deleteDiacritics(deleteRoot(wtranslate))
		wpattern = getTemplate(wtranslate)
		#wpattern_u = Buckwalter.untranslaterate(wpattern)
		#print deleteDiacritics(deleteRoot(wpattern))
		#pattern.getPattern(row[vocalized], row[unvocalized])
		data = u"'%s', '%s', '%s'" % (row[unvocalized], wpattern, row[vocalized])
		print data
		tab.insertData(data, u'word, pattern, vocalized')
		if i == 5000:
			dstdb.commit() 
			i=0
	
	dstdb.commit() 
