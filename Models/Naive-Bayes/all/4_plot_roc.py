#Author:Victor Jiang

#4_plot_roc.py: calculate the auc
#input:  featurename \t adid \t value \t  P(click | feature=value) \t click \t impression
#output: auc value

print __doc__

import numpy as np
#import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.utils import shuffle
from sklearn.metrics import roc_curve, auc

import numpy as np
from sklearn.metrics import roc_auc_score



import sys
import csv
target=[]
prob=[]
for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    prob.append(float(fields[0]))
    target.append(float(fields[2]))


y_true = np.array(target)
y_scores = np.array(prob)
print y_true
print y_scores
output = roc_auc_score(y_true, y_scores)
print float(output)

