Instructions: GBM in R and EC2
=========
## Prepare input data frame
* First, follow the R code in gbm.R file to shrink data size and categorical variable's levels.

* Input data frame has 8 columns: y(reponse), ad_id, position, depth, impression, click, w(weight)
```
train$ad_id <- reduceFactorLevels(train, "ad_id", 20)
```
* This function changes the factor levels of original ad_id into 20 levels. In this case, we can apply gbm function without memory lack problem.

## Apply gbm function

* Second, apply gbm function in gbm R package to get the result
```
gbm.model2 <- gbm(y ~  ad_id + position + depth, n.trees= 10, weights=w, data=train, train.fraction=1.0)
```

## Test by validation dataset

```
validation$prob <- predict(gbm.model2, newdata=validation, n.trees=10, type="response")

write.csv(validation, "gbm_validation_results.csv", quote=FALSE)
```
* Output gbm_validation_results.csv file

