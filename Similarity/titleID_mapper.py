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
    items = line.split('\t')
    if len(items) == 14:
        title_id = items[11]
        print '%s\t%s' % (title_id, items)
    if len(items) == 2:
        title_id = items[0]
        tokens = items[1]
        print '%s\t%s\t%s' % (title_id, tokens, 'token')
