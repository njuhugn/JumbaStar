#!/usr/bin/python
# author: Sida Ye
import sys

for line in sys.stdin:
    line = line.strip()
    lst = line.split("\t")
    try:
        if len(lst) == 2:
            print '%s\t%s' % (lst[0], lst[1]) # remember to change index
    except Exception:
        continue


