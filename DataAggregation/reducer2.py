#!/usr/bin/python
# this reducer aggregate all the instances with impression <= 20 and leave
# other instance unchanged

import sys

sep_click = 0
sep_impression = 0

current_name = None


for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    feature_name = items[0]
    feature_value = items[1]
    click = int(items[3])
    impression = int(items[2])

    
    if feature_name == current_name:
        if impression <= 20:
            sep_click = sep_click + click
            sep_impression = sep_impression + impression
            current_name = feature_name
        else:
            print '%s\t%s\t%s\t%s' % (feature_name, feature_value,\
                                  impression, click)
            current_name = feature_name

    else:
        if current_name != None:
            print '%s\t%s\t%s\t%s' % (current_name, "UNK",\
                                  sep_impression, sep_click)
            sep_click = 0
            sep_impression = 0
            
            if impression <= 20:
                sep_click = sep_click + click
                sep_impression = sep_impression + impression
                current_name = feature_name
            else:    
                print '%s\t%s\t%s\t%s' % (feature_name, feature_value, \
                                  impression, click)
                current_name = feature_name
        else:        
            if impression <= 20:
                sep_click = sep_click + click
                sep_impression = sep_impression + impression
                current_name = feature_name
            else:    
                print '%s\t%s\t%s\t%s' % (feature_name, feature_value, \
                                  impression, click)
                current_name = feature_name


print '%s\t%s\t%s\t%s' % (current_name, "UNK", sep_impression, sep_click)
