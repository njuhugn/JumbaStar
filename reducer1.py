#!/usr/bin/python
# this reducer return each unqiue feature \t sum of impression \t sum of click
import sys

current_id = None
click = 0
impression = 0
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    feature = items[0]
    if current_id == feature:
        click = click + int(items[3])
        impression = impression + int(items[2])
    else:
        if current_id:
            print '%s\t%s\t%s\t%s' % (feature, "ad", impression, click)
        current_id = feature
        click = int(items[3])
        impression = int(items[2])
            
print '%s\t%s\t%s\t%s' % (feature, "ad", impression, click)
