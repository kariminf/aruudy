#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgi
import cgitb
import json
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import urlparse, urllib

import ar_metre

cgitb.enable()

args = cgi.FieldStorage()

res = {}

r = u""

r = args.getvalue("text")

r = unicode(r)

r = ar_metre.ar_filter(r)
res["filtred"] = r.encode('utf-8')

r = ar_metre.fix_al(r)
res["fix-al"] = r.encode('utf-8')

r = ar_metre.fix_awy(r)
res["fix-awy"] = r.encode('utf-8')
    
r = ar_metre.get_cv(r)
res["cv"] = r.encode('utf-8')
    
r = ar_metre.get_metre(r)
res["metre"] = r.encode('utf-8')
    
r = ar_metre.get_metre_name(r)
res["metre-name"] = r
    
print "Content-type: application/json;charset=utf-8"
print
print (json.dumps(res))
