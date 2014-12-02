#!/usr/bin/python
# author:Jiajun Chen
import sys

age = None
gender = None

for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if items[-1] == 'gender' and len(items) == 5:
    	age = items[1]
    	gender = items[3]
    else:
    	print '%s\t%s\t%s\t%s\t%s' % (items[1], age, 'age', gender, 'gender')

