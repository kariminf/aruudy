#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(1,'./')
sys.path.insert(1,'../')

from trans.buckwalter import Buckwalter

print Buckwalter.translaterate(u'هذا البرنامج يعطينا نطق الحروف')
print Buckwalter.untranslaterate('h*A AlbrnAmj yETynA nTq AlHrwf') 
