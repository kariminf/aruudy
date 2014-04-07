#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  create.py
#  Used to create the database from arramouz database (http://arramooz.sourceforge.net/)
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

import litebase
import pattern
import arudquery
import wazn

if __name__ == '__main__':

	#you can create the dictionary using arramouz database (http://arramooz.sourceforge.net/)
	# ory ou can find it by downloading 
	#"http://sourceforge.net/projects/mishkal/files/mishkal2013-05-18.tar.bz2/download"
	# in ./lib/qalsadi/data/arabicdictionary.sqlite
	srcdb = litebase.liteBase('arabicdictionary.sqlite')
		
	dstdb = litebase.liteBase('words.db')
	
	tab = litebase.liteTable()
	tab.beginTable("nouns")
	tab.addColumn('id', litebase.litePK_INT_INC(), u'', False)
	tab.addColumn('word', litebase.liteVARCHAR(20), u'DEFAULT NULL', True)
	tab.addColumn('pattern', litebase.liteVARCHAR(20), u'DEFAULT NULL', True)
	tab.endTable()
	print tab.getSqlQuery()
	
	dstdb.addTable(tab)
	src = srcdb.getTable('nouns')
	
	rows = src.getData()
	
	first = True
	for row in rows:
		if first:
			first = False
			continue
		vocalized = src.getColumnIndex('vocalized')
		unvocalized = src.getColumnIndex('unvocalized')
		pattern = getPattern(row[vocalized])
		data = u"'%s', '%s'" % (row[unvocalized],pattern)
		#~ print data
		tab.insertData(data, u'word, pattern')
	
	dstdb.commit() 
