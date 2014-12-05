#!/usr/bin/env python
#Author: Victor Jiang

#reducer.py:aggregate the values with the same key
#input: value \t featurename \t click \t impression
#output:  value \t featurename \t  click \t impression

import sys
from operator import itemgetter

current_click = 0
current_impression = 0
currentkey = None
currenttype= None
key = None
typeclass = None

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    key, typeclass, click, impression = line.split('\t',3)
    # convert count (currently a string) to int
    try:
        click = float(click)
    except ValueError:
        continue
    try:
        impression = float(impression)
    except ValueError:
        continue

    if  (currentkey == key and currenttype==typeclass) or currenttype == None:
        currentkey = key 
        currenttype=typeclass
        current_click += click
        current_impression += impression

    else:    
        print '%s\t%s\t%s\t%s' % ( typeclass,currentkey, current_impression, current_click)
        currenttype=typeclass
        currentkey = key
        current_click = click
        current_impression = impression

# do not forget to output the last word if needed!
if currentkey == key:
    print '%s\t%s\t%s\t%s' % (typeclass,currentkey, current_impression, current_click)
