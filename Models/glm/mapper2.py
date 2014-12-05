#!/usr/bin/python
# author: Jiajun Chen
# identity mappery
import sys
for line in sys.stdin:
    line = line.strip()
    ids = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s' % (ids[0], ids[1], ids[2], ids[3], ids[4])

