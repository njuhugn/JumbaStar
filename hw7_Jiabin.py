#========================================================================
# The goal of the assignment is to understand gini index and decision trees.
# 
# TODO: Implement the functions. Add 2 unit test cases for each function.
# Submit: hw7.py, hw7_unittest.py
#========================================================================
#Question 1:
# Given a class list, calculate gini index                    (2 points)
# Unit test case (2 nos)                                      (1 point)

# Input:    class_list - sample in unit test file
# Output:   Gini index - float
#========================================================================
def compute_gini_index(class_list):
    """Given a list of classes returns the gini index

    Input: a list of classes
    Output: a real (gini index)
    """
    total = len(class_list)
    dict1 = {}
    for i in class_list:
        if i not in dict1:
            dict1[i] = 0
        dict1[i] += 1
    gini = 0
    for k in dict1:
        gini += float(dict1[k])/total*(1-float(dict1[k])/total)
    return gini

#========================================================================
# Question 2:
# Given a data set and the index of a numerical attribute, output the
# best split using the binary splitting algorithm discussed     (2 points)
# Unit test case - 2 nos                                        (1 point)
# 
# Input:    The data set with numerical values for the attributes
#           Index of the attribute (see sample in unit test)
# Output:   The attribute value that gives the best split (float)
# Hint:     Compute information gain using gini index for every split
#========================================================================
def best_attribute_split(data, attribute_index):
    """ Compute the best value to split on.
    Input:
        data, (subset of the dataset)
        attribute_index (integer)
    Return: value
    """
    sorted_data = sorted(data, key=lambda x: x[attribute_index])
    length_data = len(sorted_data)
    target = [j[0] for j in sorted_data]
    ginitotal = compute_gini_index(target)
    ig = []
    for i in range(length_data-1):
        target1 = target[:(i+1)]
        target2 = target[(i+1):]
        ig_temp = ginitotal - float(len(target1))/length_data*\
                compute_gini_index(target1) - float(len(target2))/\
                length_data*compute_gini_index(target2)
        ig.append([i, ig_temp])
    sorted_ig = sorted(ig, key=lambda x: x[1])
    return sorted_data[sorted_ig[len(sorted_ig)-1][0]][attribute_index]

#========================================================================
# Question 3:
# Given a tree and a test observation return the prediction     (3 points)
# Use the example as a guide. Write your own tree and test observation in your
# unit test case                                                (1 point)
# Input:    x - test observation
#           tree - a decision tree
# Output:   The prediction for the observation
#========================================================================
def tree_prediction(x, tree):
    """
    Input: test observation, tree
    Output: prediction for the target variable"""
    depth = 0
    subtree = tree
    number_attributes = 100 #Max recursion
    while depth < number_attributes:
        depth += 1
        node = subtree.keys()[0]
        subtree = subtree[node]
        node = x[node]
        subtree = subtree[node]
        if type(subtree) == str:
            return subtree
