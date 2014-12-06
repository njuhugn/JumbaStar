Instructions to train GLM 
=========
## Step1-find ad_id, depth, position, click, impression for each instance
* python file: mapper1.py
* Input file:training-60
* Output: output is inthe format of ad_id \t position \t depth \t click \t impression

## Step2-aggregate click and impression by unique ad_id, depth and position
*  python file: reducer1.py
*  Input file: output from above
*  Output: output is in the format of ad_id \t position \t depth \t click \t impression

## Step3-identity mapper
*  python file: mapper2.py
*  Input file: output from above
*  Output: output is in the format of ad_id \t position \t depth \t click \t impression

## Step4-aggreage all the instance with less than 20 impressions, assign them to "UNK"
*  python file: reducer2.py
*  Input file: output from above
*  Output: output is in the format of ad_id \t position \t depth \t click \t impression

## Step5-use EC2 to run glm in R
* R file: glm.R
* Input file: output from the reducer above
* Output: output is in the format of ad_id \t position \t depth \t click \t impression \t Probability of being clicked
