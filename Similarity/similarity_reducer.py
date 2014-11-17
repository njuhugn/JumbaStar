#!/usr/bin/python
def get_tokens(id_val, filename):
    """ Given (ID, filename), return the list of tokens associated with it"""

    id_token_list = [line.strip() for line in open(filename)]
    clean_line = id_token_list[int(id_val)].split("\t")
    if clean_line[0] == id_val:
        return clean_line[1].split("|")

def get_all_ad_tokens(ad_id):
    """Given an ad ID, find the combined list of all tokes in its
    keyword, title and description"""

    instance_list = [line.strip() for line in open("instances.txt")]
    for i in range(0, len(instance_list)):
        clean_line = instance_list[i].split("\t")
        if clean_line[3] == ad_id:
            lst = [clean_line[8], clean_line[9], clean_line[10]]
            return get_tokens(lst[0], 'purchasedkeywordid_tokensid.txt') + \
            get_tokens(lst[1], 'titleid_tokensid.txt') + \
            get_tokens(lst[2], 'descriptionid_tokensid.txt')


def get_similarity_index(query_id, ad_id):
    """Given a query_id, adID find the SimilarityIndex"""

    list1 = get_tokens(query_id, 'queryid_tokensid.txt')
    list2 = get_all_ad_tokens(ad_id)
    count = 0
    for item in list1:
        if item in list2:
            count += 1
    return float(count) / float(len(list1))


import sys

for line in sys.stdin:
    line = line.strip()
    AdID, QueryID = line.split('\t')
    print '%s\t%s\t%s' %(AdID, QueryID, get_similarity_index(AdID, QueryID))


