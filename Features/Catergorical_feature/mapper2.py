#!/usr/bin/python
# author: Jiajun Chen
# identity mapper
import sys
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    print '%s\t%s\t%s\t%s' % (items[0], items[1], items[2], items[3])


