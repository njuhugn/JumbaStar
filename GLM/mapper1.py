#!/usr/bin/python
### create data frame for glm in R -- JiajunChen
import sys
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    ad_id = int(items[5])
    position =  int(items[8])
    depth =  int(items[7])
    impression =  int(items[3])
    click =  int(items[2])
    print '%s\t%s\t%s\t%s\t%s' % (ad_id, position, depth, click, impression)

