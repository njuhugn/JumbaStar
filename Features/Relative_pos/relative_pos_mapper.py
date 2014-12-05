#!/usr/bin/python
# author: Sida Ye
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

Input format: instance(list) /t similarity_index
Output format : instance /t similarity_index /t relative_pos

"""
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    lst = items[0].split(',')
    if len(items) == 2:
        pos = int(lst[7].replace("'",""))
        depth = int(lst[8].replace("'",""))
        relative_pos = float((depth - pos)) / float(depth)
        print '%s\t%s' % (items[0], relative_pos)
        
# use identity reducer
