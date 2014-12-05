Instructions to calculate similarity features between titldID and queryID
=========
## MapJoin One
* First, combine original instance data file and titleID_token file together as the input for first mapjoin work.

* Second, create a cluster which takes the titleID_mapper.py as mapper and titleID_reducer.py as redcuer.

* The output file's format is instance /t titleID_token

## MapJoin Two
* First, combine the output of Mapjoin One and queryID_token file together as the input for the second mapjoin work.

* Second, create a cluster which takes the queryID_mapper.py as mapper and queryID_reducer.py as reducer.

* The output file's format is instance /t titleID_token /t queryID_token

## 1-token Similarity calculation
* First, use the output from second MapJoin Two as input.

* Second, take the 1token_similarity_mapper.py as mapper and use an identity reducer

* The reducer is the "identify reducer", you can used 
```
org.apache.hadoop.mapred.lib.IdentityReducer
```
The output's format is instance /t 1-token_similarity_index

## 2-token similarity calculation
* First, use the output from second MapJoin Two as input.

* Second, take the 1token_similarity_mapper.py as mapper and use an identity reducer

* The reducer on is the "identify reducer", you can used 
```
org.apache.hadoop.mapred.lib.IdentityReducer
```
* The output's format is instance /t 2-token_similarity_index

