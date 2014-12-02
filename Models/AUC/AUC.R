#Author: Victor Jiang


install.packages('AUC')
library(AUC)
help(accuracy)

data(churn)
churn$labels
x=accuracy(churn$predictions,churn$labels)
auc(x)
out <- read.delim("~/Downloads/out.txt", header=F)
View(out)
x[x[,5]>1,5]=1
y=accuracy(x$V3,factor(x$V5))
