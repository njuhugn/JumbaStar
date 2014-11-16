""" The goal of the assignment is to know measure how much a query is
related to an advertisement.

==========================================================================

*** Read "https://www.kddcup2012.org/c/kddcup2012-track2" before you start.***

==========================================================================

Rules:
1.  For all the questions, you are required to maintain the name and
     signature of the functions.
2.  Also, it is important that your code is syntacticaly correct and
     compiles without errors(warnings are OK).
3.  Run your code through pylint and correct style errors.

==========================================================================
NOTE:
    1. You can test your code by running "python hw4.py"
    All supporting files can be downloaded from
        "https://www.kddcup2012.org/c/kddcup2012-track2/data"
    Download track2.zip. You will find all these files there.
    List of files used for this assignment:
        a. 'queryid_tokensid.txt'
        b. 'purchasedkeyword_tokensid.txt'
        c. 'titleid_tokensid.txt'
        d. 'descriptionid_tokensid.txt'
        e. 'instances.txt'    - This file should be downloaded from bcourses.

    Ensure all these files are in the same folder as your python script.

    2. File format:
        Each line of files a, b, c and d have 2 fields delimited by TAB.
            1. ID - string
            2. Tokens - string
        'Tokens' field is a list of numbers(token id strings) separated by "|".
        Eg. "197 75|31|1545"

        For file e:
        Each instance is a string with the following fields delimited by TAB.
        Each field is again of type 'string'.
        1. Click
        2. Impression
        3. DisplayURL
        4. AdID
        5. AdvertiserID
        6. Depth
        7. Position
        8. QueryID
        9. KeywordID
        10. TitleID
        11. DescriptionID
        12. UserID

    3. There are sample input output values given for each question.
    An test() function is written to facilitate easy testing.
    These will help you test your logic and output format.
    However, while grading additional testing will be done.
    4. In each function, the file is read and a list of instances is created
    for your convenience.
==========================================================================
Question 1:                                                        (1 point)
Task:
    Given a ID and a filename, return the list of tokens associated with it.
    As mentioned in the note earlier, each line in the file is of the format
        "ID<TAB>token1|token2|token3"
Input:
    1. ID string.
    2. File name string.
Output:
    A list of all the token ID strings.
"""
def get_tokens(id_val, filename):
    """ Given (ID, filename), return the list of tokens associated with it"""

    id_token_list = [line.strip() for line in open(filename)]
    result = []
    for i in range(0, len(id_token_list)):
        temp = id_token_list[i].split()
        if temp[0] == id_val:
            result = (temp[1].split("|"))
    return result

"""
==========================================================================
Question 2:                                                     (2 points)
Task:
    Given an ad ID, find the combined list of all tokes in its
    keyword, title and description.
Input:
    1. Ad ID - string
Output:
    A list of all the token IDs.
"""
def get_all_ad_tokens(ad_id):
    """Given an ad ID, find the combined list of all tokes in its
    keyword, title and description"""

    instance_list = [line.strip() for line in open("instances.txt")]
    result = []
    for i in range(0, len(instance_list)):
        temp = instance_list[i].split()
        if temp[3] == ad_id:
            result.extend(get_tokens(temp[8],
                'purchasedkeywordid_tokensid.txt'))
            result.extend(get_tokens(temp[9], 'titleid_tokensid.txt'))
            result.extend(get_tokens(temp[10], 'descriptionid_tokensid.txt'))


    return result

"""
==========================================================================
Question 3:                                                     (3 points)
The similarity between a query and an advertisement is measured as the
similarity of keywords between the query and the keyword, title and description.
    SimilarityIndex:
 sum of(num of tokens in the query that are also in keyword,title,description
    / num of tokens in the query).

    Note: If a query has more than one token, SimilarityIndex is the sum of the
indices calculated for each token in the query.

Task:
    Given a (query, adID) find the SimilarityIndex.
Input:
    1. query id - string
    2. Ad ID - string
Output:
    SimilarityIndex calculated by the above formula - float.
"""
def get_similarity_index(query_id, ad_id):
    """Given a query_id, adID find the SimilarityIndex"""
    query_list = get_tokens(query_id, "queryid_tokensid.txt")
    ad_list = get_all_ad_tokens(ad_id)
    match = 0
    total = len(query_list)
    for i in range(0, len(query_list)):
        if query_list[i] in ad_list:
            match += 1
    return float(match)/float(total)


"""
==========================================================================
Question 4:                                                     (2 points)
A 2-token phrase is any two consecutive tokens for an ID.
Get all the 2-token phrases for the given ID.

Task:
    Given a (ID, filename) find all 2-token phrases.
Input:
    1. ID - string
    2. filename - string
Output:
    A list of 2 token phrases - list"""

def get_2_token_phrases(id_val, filename):
    """Given a (ID, filename) find all 2-token phrases"""
    original = get_tokens(id_val, filename)
    output = []
    i = 0
    prev = original[0]
    while i < len(original) - 1:
        output.append([prev, original[i+1]])
        prev = original[i+1]
        i += 1
    return output

"""
==========================================================================
Question 5:                                                     (2 points)
SimilarityIndex2 follows the same formula as Q3. But here,instead of calculating
the index for every single token and adding them, you pick 2-token phrases from
the query and find their similarity with 2-token phrases in keyword, title,
description of the ad.

SimilarityIndex2 = sum of(num of 2-token phrase in a query that are also in
    keyword, title, description/ num of 2-token phrases in the query)

Task:
    Given a (query, adID) find the SimilarityIndex2.
Input:
    1. query id - string
    2. Ad ID - string
Output:
    SimilarityIndex2 calculated by the above formula - float"""

def get_all_ad_tokens2(ad_id):
    """Given an ad ID, find the combined list of all tokes in its
    keyword, title and description"""

    instance_list = [line.strip() for line in open("instances.txt")]
    result = []
    for i in range(0, len(instance_list)):
        temp = instance_list[i].split()
        if temp[3] == ad_id:
            result.extend(get_2_token_phrases(temp[8],
                'purchasedkeywordid_tokensid.txt'))
            result.extend(get_2_token_phrases(temp[9],
                'titleid_tokensid.txt'))
            result.extend(get_2_token_phrases(temp[10],
                'descriptionid_tokensid.txt'))
    return result

def get_similarity_index_2(query_id, ad_id):
    """Given a query_id, adID find the SimilarityIndex"""
    query_list = get_2_token_phrases(query_id, "queryid_tokensid.txt")
    ad_list = get_all_ad_tokens2(ad_id)
    match = 0
    total = len(query_list)
    for i in range(0, len(query_list)):
        if query_list[i] in ad_list:
            match += 1
    return float(match)/float(total)


def test(got, expected):
    """ Test function to display test cases"""
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

    # Calls the above functions with interesting inputs.

def main():
    """ Calls the test function"""
    """
    print '\n\nGet list of tokens for an id\n\n'

    test(get_tokens('165', 'queryid_tokensid.txt'),\
            ['13521', '12266', '91658', '3835'])
    test(get_tokens('62', 'queryid_tokensid.txt'), ['310'])
    test(get_tokens('33', 'purchasedkeywordid_tokensid.txt'), ['45', '31'])
    test(get_tokens('29', 'titleid_tokensid.txt'),\
            ['45', '31', '571', '1916', '38'])

    print '\n\nGet all ad tokens\n\n'
    test(get_all_ad_tokens('21162422'), ['10772', '327', '6', '45', '572',\
    '2', '10772', '327', '6', '334', '34', '271', '209', '158', '3', '271',\
    '209', '158', '958', '381', '2282', '3610', '2773', '1781', '1', '173',\
    '597', '274', '2', '10772', '327', '6', '1056', '28', '29', '665',\
    '191', '3'])

    test(get_all_ad_tokens('4418786'), ['6410', '971', '37', '1270', '1',\
    '69', '6410', '971', '466', '582', '1', '1159', '6410', '971', '1',\
    '1192', '5010', '1', '329', '146', '1', '414', '89', '720', '4958',\
    '330', '7590', '3'])
    """
    print '\n\nGet Similarity Index\n\n'
    print(get_tokens('97',"queryid_tokensid.txt"))
    print(get_all_ad_tokens('21822275'))
    test(get_similarity_index('97', '21822275'), 0.5)
    test(get_similarity_index('1000', '20395615'), 0.0)
    """
    print '\n\nGet Two phrased tokens\n\n'

    test(get_2_token_phrases('27', "queryid_tokensid.txt"),\
        [['25', '20'], ['20', '18'], ['18', '4174'], ['4174', '4469']])
    test(get_2_token_phrases('21', "titleid_tokensid.txt"), [['824', '1963'],\
    ['1963', '3'], ['3', '0'], ['0', '616'], ['616', '50'], ['50', '605'],\
    ['605', '334'], ['334', '34'], ['34', '582']])
    test(get_2_token_phrases('78', "purchasedkeywordid_tokensid.txt"), [])
    """
    print ('\n\nGet Similarity Index2\n\n')
    print(get_2_token_phrases('97',"queryid_tokensid.txt"))
    print(get_all_ad_tokens2('21822275'))
    test(get_similarity_index_2('97', '21822275'), 0.0)

if __name__ == "__main__":
    main()


