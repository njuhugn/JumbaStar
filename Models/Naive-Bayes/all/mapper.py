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
        query = float(items[0].replace('"',' ').split(',')[9].replace('\''," "))
        title = float(items[0].replace('"',' ').split(',')[11].replace('\''," "))
        s = float(items[1])
        try:
            if len(items) == 2:
                click = float(items[0].replace('"',' ').split(',')[2].replace('\''," "))
                impression = float(items[0].replace('"',' ').split(',')[3].replace('\''," "))
        except Exception:
            continue
        key = "%s%s%s" % (int(query),"_", int(title))
        print '%s\t%s\t%s\t%s' % (s,'query_title', click, impression)
find_probability()
