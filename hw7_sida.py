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
    dict_class = {}
    for i in class_list:
        dict_class[i] = class_list.count(i)
    total = 0
    for key in dict_class:
        p_ki = float(dict_class[key]) / float(len(class_list))
        total += p_ki * (1 - p_ki)
    return total

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
def information_gain_for_numeric_data(data, index, index_of_split):
    """  Returns information gain for a subset of the data and an index.

    Input: data (subset of the original training set)
           index (index of a feature)
    Output: information gain (a real)
    We assume here that all variables are categorical
    data = [["yes", 1.1], ["yes", 1.0], ["no", 1.5], ["no", 1.3],\
["no", 1.8], ["yes", 0.3], ["yes", 0.7], ["no", 2.3]]
    """
    # Splitting labels by the value of row[index]
    gini_index_T = compute_gini_index([lst[0] for lst in data])
    gini_index_T_i = 0
    sorted_list = sorted(data, key=lambda x: x[index])
    group1 = [lst[0] for lst in sorted_list \
    if lst[index] <= sorted_list[index_of_split][index]]
    group2 = [lst[0] for lst in sorted_list \
    if lst[index] > sorted_list[index_of_split][index]]
    gini_index_T_i += (float(len((group1))) / float(len(data))) \
    * compute_gini_index(group1)
    gini_index_T_i += (float(len((group2))) / float(len(data))) * \
    compute_gini_index(group2)
    return gini_index_T - gini_index_T_i

def best_attribute_split(data, attribute_index):
    """ Compute the best value to split on.
    Input:
        data, (subset of the dataset)
        attribute_index (integer)
    Return: value
    """
    sorted_list = sorted(data, key=lambda x: x[attribute_index])
    i = 0
    info = []
    while i < len(data):
        info.append(information_gain_for_numeric_data(data, attribute_index, i))
        i = i + 1
    return sorted_list[info.index(max(info))][attribute_index]


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
    if type(tree) == str:
        return tree
    else:
        for index in tree:
            tree = tree[index][x[index]]
        return tree_prediction(x, tree)






