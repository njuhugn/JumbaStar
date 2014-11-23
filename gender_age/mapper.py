#!/usr/bin/python
#author: Jiajun Chen
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
    items = line.split('\t')
    if len(items) == 14:
        user_id = items[11]
        print '%s\t%s' % (user_id, items)
    if len(items) == 3:
        user_id = items[0]
        age = items[2]
        gender = items[1]
        print '%s\t%s\t%s\t%s\t%s' % (user_id, age, 'age', gender, 'gender')
