#!/usr/bin/python
import sys
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if len(items) == 12:
        ad_id = items[3]
        query_id = items[7]
        title_id = items[9]
        impression = items[1]
        click = items[0]
        print '%s\t%s\t%s' % (query_id, impression, click)
    else:
        query_id = items[0]
        tokens = items[1]
        print '%s\t%s' % (query_id, tokens)
