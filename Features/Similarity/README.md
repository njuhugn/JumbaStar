Instructions to calculate similarity features between titldID and queryID
=========
## MapJoin One
First, combine original instance data file and titleID_token file together as the input for first mapjoin work.

Second, create a cluster which takes the titleID_mapper.py as mapper and titleID_reducer.py as redcuer.

The output file's format is instance /t titleID_token

## Mapjoin Two
First, combine the output of Mapjoin One and queryID_token file together as the input for the second mapjoin work.

Second, create a cluster which takes the queryID_mapper.py as mapper and queryID_reducer.py as reducer.

The output file's format is instance /t titleID_token /t queryID_token
