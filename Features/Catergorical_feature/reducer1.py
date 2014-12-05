#!/usr/bin/python
# author: Jiajun Chen
# sum up click and impression for unique ad_id, depth and position
import sys

current_value = None
current_name = None
click = 0
impression = 0
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    feature_value = items[1]
    
    if current_value == feature_value:
        click = click + int(items[3])
        impression = impression + int(items[2])
    else:
        if current_value and current_name:
            print '%s\t%s\t%s\t%s' % (current_name, current_value,\
                                      impression, click)
        current_value = feature_value
        current_name = items[0]
        click = int(items[3])
        impression = int(items[2])
            
print '%s\t%s\t%s\t%s' % (current_name, current_value, impression, click)

