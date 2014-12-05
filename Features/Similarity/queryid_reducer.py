#!/usr/bin/python

# author: Sida Ye

import sys

token = None

"""
Input format: query_id /t instance /t titel_id_token
              query_id /t query_id_token /t 'token'

Output format: instance /t titleID_token /t queryID_token 
"""

for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if items[-1] == 'token':
    	token = items[1]
    else:
    	print '%s\t%s\t%s' % (items[1], items[2], token)
    		
