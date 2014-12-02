#!/usr/bin/python
# this reducer aggregate all the instances with impression <= 5 and leave
# other instance unchanged

import sys

sep_click = 0
sep_impression = 0

for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    ad_id = items[0]
    position = items[1]
    depth = items[2]
    if int(items[4]) <= 5:
        sep_click = sep_click + int(items[3])
        sep_impression = sep_impression + int(items[4])
    else:
        print '%s\t%s\t%s\t%s\t%s' % (ad_id, position, \
                                  depth, items[3],items[4])

print '%s\t%s\t%s\t%s\t%s' % ('UNK', 'UNK', \
                                  'UNK', sep_click, sep_impression)
