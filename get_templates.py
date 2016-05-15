#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  after creating database, you can try this to test the program
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
import os
import sys
import pattern
from trans.buckwalter import Buckwalter

if __name__ == '__main__':
	
	reload(sys)  
	sys.setdefaultencoding('utf8')
	
	print "To exit enter an empty word"
	
	while (True):
		sys.stdout.write("Please enter an Arabic word: ")
		word = raw_input()
		if len(word)< 2:
			print "Thank you for using me"
			break
			
		wtrans = Buckwalter.translaterate(unicode(word))
		#print wtrans # Translateration
		templates = pattern.getTemplateNoDiac(wtrans)
		print Buckwalter.untranslaterate(templates)
		
