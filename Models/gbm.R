# author: Sida Ye
# R code to run gbm
# Run the code on EC2

"""
Input data frame format: ad_id, position, depth, impression, clicks, non-clicks
Then we are trying to run gbm on this dataframe.
"""


train  <- read.delim("part.txt", header=FALSE)
validation <- read.delim("validation_input.txt", header=FALSE)
variables <- c("ad_id", "position", "depth", "impressions","clicks")
names(train) <- variables # name valriables
names(validation) <- variables
train$no_clicks <- with(train, impressions - clicks) # calculate non-click
validation$no_clicks <- with(validation, impressions - clicks)
train[,2:6]<-lapply(2:6,function(x) as.numeric(train[,x])) # change data format
validation[,2:6]<-lapply(2:6,function(x) as.numeric(validation[,x])) 
train = train[train$impressions<100,] # choose the threfold to reduce train data

# the input is dataframe with a column impressions
reduceFactorLevels <- function(data, var, n=1024) {
  data <- data[,c(var, "impressions")]
  vec <- as.character(data[,var])
  data_grouped <- aggregate(data["impressions"], data[var], sum)
  data_grouped <- data_grouped[order(data_grouped$impressions, decreasing=T),]
  new_n <- min(nrow(data_grouped), n - 1)
  keep <- as.character(data_grouped[1:new_n,var])
  vec <- ifelse(vec %in% keep, vec, "other")
  as.factor(vec)
}


matchFactorLevels <- function(data, data_to_match, var) {
  keep <- as.character(levels(data_to_match[,var]))
  vec <- as.character(data[, var])
  vec <- ifelse(vec %in% keep, vec, "other")
  as.factor(vec)
}

train$ad_id <- reduceFactorLevels(train, "ad_id", 20) # change the number of level

# transforming data
train_no_clicks <- train
train_no_clicks$y <- 0
train_no_clicks$w <- train_no_clicks$no_clicks

# y needs to be numeric
train$y <- 1
train$w <- train$clicks

train <- rbind(train, train_no_clicks)
train$impressions <- NULL
train_no_clicks <- NULL
train$clicks <- NULL
train$no_clicks <- NULL

library(gbm)
gbm.model2 <- gbm(y ~  ad_id + position + depth, n.trees= 10, weights=w, data=train, train.fraction=1.0)

validation$ad_id <- matchFactorLevels(validation, train, "ad_id")
validation$prob <- predict(gbm.model2, newdata=validation, n.trees=10, type="response")

write.csv(validation, "gbm_validation_results.csv", quote=FALSE)
