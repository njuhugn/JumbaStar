#!/usr/bin/python
# this reducer aggregate all the instances with impression <= 20 and leave
# other instance unchanged

import sys

sep_click = 0
sep_impression = 0

for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    feature = items[0] 
    if int(items[2]) <= 20:
        sep_click = sep_click + int(items[3])
        sep_impression = sep_impression + int(items[2])
    else:
        print '%s\t%s\t%s\t%s' % (feature, "ad", items[2], items[3])

print '%s\t%s\t%s\t%s' % ("UNK", "ad", sep_impression, sep_click)

