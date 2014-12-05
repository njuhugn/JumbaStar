Instructions: Relative Position Feature
=========
## Calculate relative position
* First, use output from Mapjoin file in the second mapjoin in similarity calcuation process. 

* Input format is instance /t titleID_token /t queryID_token

* Second, create a cluster which takes the relative_pos_mapper.py as mapper

* The reducer is the "identify reducer", you can used 
```
org.apache.hadoop.mapred.lib.IdentityReducer
```

* The output file's format is instance /t titleID_token /t queryID_token /t relative_pos

