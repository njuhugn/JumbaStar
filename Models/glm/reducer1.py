#!/usr/bin/python
# author: Jiajun Chen
# aggregate click and impression for unqiue combination of ad_id, position, depeth
import sys

current_id = None
current_pos = None
current_dep = None
click = 0
impression = 0
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    ad_id = items[0]
    position = items[1]
    depth = items[2]
    if current_id == ad_id and current_pos == position and current_dep == depth:
        click = click + int(items[3])
        impression = impression + int(items[4])
    else:
        if current_id and current_pos and current_dep:
            print '%s\t%s\t%s\t%s\t%s' % (current_id,current_pos,current_dep,click,impression)
        current_id = ad_id
        current_pos = position
        current_dep = depth
        click = int(items[3])
        impression = int(items[4])
            
print '%s\t%s\t%s\t%s\t%s' % (ad_id,position,depth,click,impression)
