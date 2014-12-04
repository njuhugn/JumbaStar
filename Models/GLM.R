#author: Sida Ye

part <- read.delim("C:/Users/lenovo/Desktop/part.txt", header=FALSE) # import data
train <- part # change data name
variables <- c("ad_id", "position", "depth", "impressions","clicks")
names(train) <- variables
train$no_clicks <- with(train, impressions - clicks)
train[,2:6]<-lapply(1:6,function(x) as.numeric(train[,x])) # change data format

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
class(train[,2]
train$ad_id <- reduceFactorLevels(train, "ad_id", 10)


#### GLM
library(stats)
model.glm <- glm(cbind(clicks, no_clicks) ~ ad_id + position + depth,
                 family = binomial, data = train)
