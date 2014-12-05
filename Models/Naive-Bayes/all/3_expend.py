#!/usr/bin/env python
#Author:Victor Jiang

#3_expend.py: expand what I have for previous step so that each line only has one impression
#input:  featurename \t adid \t value \t  P(click | feature=value) \t click \t impression
#output:  featurename \t adid \t value \t  P(click | feature=value) \t click \t impression

import sys
import os.path
sys.path.append(os.path.dirname(__file__))


for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    click = float(fields[3])
    nonclick = float(fields[4]) - float(fields[3])
    while nonclick != 0:
        if click == 0:
            print "%s\t%s\t%s" %(fields[2], 1.0, 0.0)
            nonclick -= 1
        else:
            print "%s\t%s\t%s" %(fields[2], 1.0, 1.0)
            click -= 1           
