# author: Jiajun Chen, Sida Ye
# R code to run glm 

"""
Input data frame format: ad_id, position, depth, impression, clicks, non-clicks
Then we are trying to run a logistic regression on this dataframe.

"""


train <- part # change data name
variables <- c("ad_id", "position", "depth", "impressions","clicks")
names(train) <- variables # name valriables
train$no_clicks <- with(train, impressions - clicks) # calculate non-click
train[,2:6]<-lapply(2:6,function(x) as.numeric(train[,x])) # change data format
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

train$ad_id <- reduceFactorLevels(train, "ad_id", 50) # change the number of level
      
      
#### GLM
library(stats)
# run logistic regression
model.glm <- glm(cbind(clicks, no_clicks) ~ ad_id + position + depth, family = binomial, data = train)



####################
#### GLM
library(stats)
model.glm <- glm(cbind(clicks, no_clicks) ~ ad_id + advertiser_id + position,
                 family = binomial, data = train)

model.glm <- glm(cbind(click, no_clicks) ~ AdID + Pos + Depth + impressions, family = binomial, data = train)

validation <- read.table("validation-bs1.tsb", header=FALSE, colClasses=colClasses)
names(validation) <- variables

validation$ad_id <- matchFactorLevels(validation, train, "ad_id")
validation$advertiser_id <- matchFactorLevels(validation, train, "advertiser_id")

validation$prob <- predict(model.glm, newdata=validation, type="response")

#got this
#prediction from a rank-deficient fit may be misleading

write.csv(validation, "validation_results.csv", quote=FALSE)
