#!/usr/bin/python
### extract all the features
import sys
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    lst = items[0].split(',')
    ad_id = int(lst[5].replace("'",""))
    position = int(lst[8].replace("'",""))
    depth = int(lst[7].replace("'",""))
    impression = int(lst[3].replace("'",""))
    click = int(lst[2].replace("'",""))
    user_id = lst[13].replace("']","")
    user_id = int(user_id.replace("'",""))
    similarity = items[1]
    relative_pos = items[2]
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (ad_id, position, \
                                          depth, similarity, relative_pos,user_id,\
                                          click, impression)

