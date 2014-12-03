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

Input format: instance(list) /t title_id_token/ query_id_token

"""
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if len(items) == 3:
        title_id_token = items[1].split("|")
        query_id_token = items[2].split("|")

        titleresult = []
        i = 0
        if len(title_id_token) > 1:
            while i < len(title_id_token) - 1:
                titleresult.append([title_id_token[i], title_id_token[i + 1]])
                i = i + 1
        queryresult = []
        k = 0
        if len(query_id_token) > 1:
            while k < len(query_id_token) - 1:
                queryresult.append([query_id_token[k], query_id_token[k + 1]])
                k = k + 1

        count = 0
        for item in queryresult:
            if item in titleresult:
                count += 1
        index = float(count) / float(len(query_id_token))
        print '%s\t%s' % (items[0], index)
