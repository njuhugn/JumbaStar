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
This code is going to calculate 1-token similarity.
Input format: instance(list) /t title_id_token/ query_id_token
Output format: instance /t 1-token_similarity_index
"""
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if len(items) == 3:
        title_id_token = items[1].split("|")
        query_id_token = items[2].split("|")
        count = 0
        for item in query_id_token:
            if item in title_id_token:
                count += 1
        index = float(count) / float(len(query_id_token))
        print '%s\t%s' % (items[0], index)
