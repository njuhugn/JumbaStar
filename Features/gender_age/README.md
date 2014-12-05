Instructions to calculate age and gender feature
=========
## Step1
* python file: mapper1.py
* this mapper takes in two input file, training-60 and userid_profile.txt. it extract userid 
* and the whole instance from training file. It extracts userid, age and gender from userid_profile.txt
* Input file:training-60 and userid_profile.txt
* Output: output is inthe format of 
*                                   userid \t instance
*                                   userid \t age \t "age" \t gender \t "gender"

## Step2- match the instance file with age and gender using userid
*  python file: reducer1.py
*  Input file: output from above
*  Output: output is in the format of 
*                                   instance \t age \t "age" \t gender \t "gender"
