#!/usr/bin/python
# this mapper returns feature value \t feature name \t impression \t click
import sys
for line in sys.stdin:
    line = line.strip()
    ids = line.split('\t')
    try:
        if len(ids) == 14:
            feature = ids[5]
            impression = ids[3]
            click = ids[2]
            print '%s\t%s\t%s\t%s' % (feature, "ad", impression, click)
    except Exception:
        continue
