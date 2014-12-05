#!/usr/bin/env python
#Author:Victor Jiang


import sys
import os.path
sys.path.append(os.path.dirname(__file__))

feature_dict = { 5: "ad", 7: "depth", 8:"position"}

"""
        2. Click
        3. Impression
        4. DisplayURL
        5. AdID
        6. AdvertiserID
        7. Depth
        8. Position
        9. QueryID
        10. KeywordID
        11. TitleID
        12. DescriptionID
        13. UserID
"""
### get prior probability for each feature for naive bayes
### put "input.txt" in the same directory and run this file directly in terminal.

def find_probability(train):
    click = 0
    impression = 0
    data = [line.strip() for line in open(train)]
    total = 0
    info ={}
    current = None
    for line in data:
        line = line.strip()
        items = line.split('\t')
        key = items[0]
        if len(items) ==4 and (key == current or current == None):
            current = key
            click = click + int(items[3])
            impression = impression + int(items[2])
            total += 1
        else:
            no_click = impression - click
            info[current] = [click,no_click,impression,total]
            current = key
            click = int(items[3])
            impression = int(items[2])
            total = 1
    no_click = impression - click
    info[current] = [click,no_click,impression,total]
    current = None
    for line in data:
        line = line.strip()
        items = line.split('\t')
        value = items[1]
        feature_type = items[0]
        if current != None and current != feature_type:
            print '%s\t%s\t%s\t%s' % (current, 'Total', float(click)/impression,\
                              float(no_click)/impression)
        current = feature_type
        click = info[feature_type][0]
        impression = info[feature_type][2]
        no_click = info[feature_type][1]
        total = info[feature_type][3]

        P_fea_click = (float(items[3])+1)/(click+total)
        P_fea_no_click = float(int(items[2])-int(items[3])+1)/(no_click+total)
        print '%s\t%s\t%s\t%s' % (feature_type, value, P_fea_click,\
                                  P_fea_no_click)
    print '%s\t%s\t%s\t%s' % ('Total', 'Total', float(click)/impression,\
                              float(no_click)/impression)

find_probability('input.txt')

