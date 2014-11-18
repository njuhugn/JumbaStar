#!/usr/bin/python
import sys

current_AdID = None
current_QueryID = None

for line in sys.stdin:
    line = line.strip()
    QueryID, AdID = line.split('\t')
    if QueryID != current_QueryID or AdID != current_AdID:
    	print '%s\t%s' %(QueryID, AdID)
    current_AdID = AdID
    current_QueryID = QueryID
