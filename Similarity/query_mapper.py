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
Input format: instance /t title_id_token
              query_id /t query_id_token
Output format: query_id /t instance /t title_id_token
                query_id /t query_id_token /t 'token'
    

"""
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if len(items[0]) >= 3:
        for item in items:
           query_id = item[9]
        print '%s\t%s\t%s' % (query_id, items[0], items[1])
    else:
        query_id = items[0]
        tokens = items[1]
        print '%s\t%s\t%s' % (query_id, tokens, 'token')
