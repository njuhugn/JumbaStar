#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if items[-1] == 'token':
    	token = items[1]
    else:
    	print '%s\t%s' % (items[1], token)
    		
