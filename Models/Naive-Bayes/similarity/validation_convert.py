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
def find_probability():
    click = 0
    impression = 0
    total = 0
    

    for instance in sys.stdin:
        line = instance.strip()
        items = line.split('\t')
        new =[]
        for i in range(14):
            temp = items[0].replace('"',' ').split(',')[i].replace('\''," ").replace('[',"").replace(']',"")
            new.append(temp)
        s = float(items[1])
        t = float(items[2])
        new.append(s)
        new.append(t)
        a0=new[0]
        a1=new[1]
        a2=new[2]
        a3=new[3]
        a4=new[4]
        a5=new[5]
        a6=new[6]
        a7=new[7]
        a8=new[8]
        a9=new[9]
        a10=new[10]
        a11=new[11]
        a12=new[12]
        a13=new[13]
        a14=new[14]
        a15=new[15]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15)
find_probability()
