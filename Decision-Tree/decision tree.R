# Author: Sida Ye
#### raprt
library(rpart)
fit <- rpart(response ~ click+ctr,
             method="class", data=output)

printcp(fit) # display the results 
plotcp(fit) # visualize cross-validation results 
summary(fit) # detailed summary of splits

# plot tree 
plot(fit, uniform=TRUE)
text(fit, use.n=TRUE, all=TRUE, cex=.6)
post(fit, file = "~/Desktop/tree.ps", 
     title = "Classification Tree")

#### party
############# use library party
library(party)
str(iris) # example data
str(output)
myFormula <- response ~ imp + ctr
output_ctree <- ctree(myFormula, data=output)
# check the prediction
table(predict(output_ctree), output$response)
print(output_ctree)
plot(output_ctree)
plot(output_ctree, type="simple")

# predict on test data
testPred <- predict(iris_ctree, newdata = testData)
table(testPred, testData$Species)
