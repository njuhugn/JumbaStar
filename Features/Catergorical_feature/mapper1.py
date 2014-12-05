#!/usr/bin/python
# Author: Jiajun Chen 
# this mapper extract the catergorical features: ad_id, depth and position and the click and impression
# according to these features
import sys
for line in sys.stdin:
    line = line.strip()
    ids = line.split('\t')
    try:
        if len(ids) == 14:
            ad_id = ids[5]
            depth = ids[7]
            position = ids[8]
            impression = ids[3]
            click = ids[2]
            print '%s\t%s\t%s\t%s' % ("ad_id", ad_id, impression, click)
            print '%s\t%s\t%s\t%s' % ("depth", depth, impression, click)
            print '%s\t%s\t%s\t%s' % ("position", position, impression, click)
    except Exception:
        continue

