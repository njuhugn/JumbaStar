#!/usr/bin/python
# author: Sida Ye, Jiajun Chen
import sys

token = None

for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if items[-1] == 'token' and len(items) == 3:
    	token = items[1]
    else:
    	print '%s\t%s' % (items[1], token)
    		
