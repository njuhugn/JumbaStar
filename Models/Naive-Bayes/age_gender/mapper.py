#!/usr/bin/env python
#Author: Victor Jiang


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
def find_probability():
    click = 0
    impression = 0
    total = 0
    

    for instance in sys.stdin:
        line = instance.strip()
        items = line.split('\t')
        age = items[14]
        gender = items[15]
        click = items[2]
        impression = items[3]
        print '%s\t%s\t%s\t%s' % (age,'age', click, impression)
        print '%s\t%s\t%s\t%s' % (gender,'gender', click, impression)
find_probability()
