#Author: Victor Jiang

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


"""
crs=open('out.txt', 'rb')
for columns in ( raw.strip().split() for raw in crs ):
    print columns[1]


# shuffle and split training and test sets
X, y = shuffle(X, y, random_state=random_state)
half = int(n_samples / 2)
X_train, X_test = X[:half], X[half:]
y_train, y_test = y[:half], y[half:]

# Run classifier
classifier = svm.SVC(kernel='linear', probability=True)
probas_ = classifier.fit(X_train, y_train).predict_proba(X_test)

# Compute ROC curve and area the curve
fpr, tpr, thresholds = roc_curve(y_test, probas_[:, 1])
roc_auc = auc(fpr, tpr)
print "Area under the ROC curve : %f" % roc_auc

# Plot ROC curve
plt.clf()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.show()
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()
"""
