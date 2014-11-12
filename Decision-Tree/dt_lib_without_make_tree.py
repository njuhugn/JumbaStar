import csv
import math
import random

def load_data(filename):
    """ Given a filename in csv format return a list.

    Input: a filename
    Output and list of lists
    Example:
    [['6.2', '3.4', '5.4', '2.3', 'Iris-virginica'],
     ['5.9', '3.0', '5.1', '1.8', 'Iris-virginica']]
    """
    lines = []
    with open(filename, "rb") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) > 1:
                lines.append(row)
    return lines

def get_training_testing(data, train_ratio=0.7):
    """Divides the data into training and testing

    """
    train = []
    test = []
    # number between 0 and 1 random.random()
    for row in data:
        if random.random() < train_ratio:
            train.append(row)
        else:
            test.append(row)
    return train, test

def shannon_entropy(class_list):
    """Given a list of classes returns the shannon entropy

    Input: a list of classes
    Output: a real (shannon entropy)
    """
    return entropy

def information_gain(data, index):
    """  Returns information gain for a subset of the data and an index.

    Input: data (subset of the original training set)
           index (index of a feature)
    Output: information gain (a real)
    We assume here that all variables are categorical
    """
    # Splitting labels by the value of row[index]
    return

def best_attribute_index(data, list_attribute_indices):
    """ Compute the best attribute to slit on.
    Input: 
        data (subset of the training set)
        list_attribute_indices (list of indices)
    Return: best index
    Compute information gain for every element of 
    list_attribute_indices and return the best index
    (largest information gain)
    """
    return

def split_data(data, index):
    """Splits data with respect to attribute in "index"
  
    Input: data a dataset
    Ouput: a dictionary values to a subset of data
    Example:
    data = [["yes", "sunny", "a"], ["yes", "sunny", "b"],\
            ["no", "cloudy", "c"], ["no", "cloudy", "a"]]
    split_data(data, 1)
    returns:
    {"sunny": [["yes", "sunny", "a"], ["yes", "sunny", "b"]],\ 
     "cloudy": [["no", "cloudy", "c"], ["no", "cloudy", "a"]]}
    """
    # init results
    return

def majority_class(data):
    """ Given the list of k neighbours returns the majority class.

    If there more than one in majority return a random element from
    the classes in the majority. Consider an example for k = 2
    with classes:
    'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-virginica'
    """
    # a dictionry counting the classes
    classes = {}
    for row in data:
        classes[row[0]] = classes.get(row[0], 0) + 1
    m = max(classes.values())
    # List of all classes in majority (this could be one or more)
    argmax = [z for z in classes if classes[z] == m]
    return argmax[random.randrange(0, len(argmax))]

def number_class_labels(data):
    """ Counts the number of different class labels.
    """
    return

def make_tree(data, indices, max_depth):
    """
    """
    return tree
