#!/usr/bin/python
import sys
"""
        1.
        2.
        3. Click
        4. Impression
        5. DisplayURL
        6. AdID
        7. AdvertiserID
        8. Depth
        9. Position
        10. QueryID
        11. KeywordID
        12. TitleID
        13. DescriptionID
        14. UserID
"""
for line in sys.stdin:
    line = line.strip()
    lst = line.split("\t")
    try:
        if len(lst) == 14:
            print '%s\t%s' % (lst[9], lst[5]) # remember to change index
    except Exception:
        continue


