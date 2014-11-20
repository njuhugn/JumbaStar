#!/usr/bin/python
import sys

current_key = None
impression = 0
click = 0
tokens = None

for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    key = items[0]
    if current_key == key and len(items) == 3:
        impression = impression + int(items[1])
        click = click + int(items[2])
        current_key = key
    elif len(items) == 2 and key == current_key:
        tokens = items[1]
    else:
        if impression != 0 and current_key:
            print '%s\t%s\t%s' % (impression, click, tokens)
        if len(items) == 3:
            impression = int(items[1])
            click = int(items[2])
            current_key = key
        else:
            tokens = items[1]
            current_key = key
            impression = 0
            click = 0

