# Election Analysis
## Overview of Election Audit
The purpose of this project is to assist Seth, who works for the Colorado Elections Commission, and his manager Tom to 
analyze and confirm the results of the election. To accomplish this goal Tom and Seth produced the data for every vote
in the election. This data came in the format of a csv (comma separated values) file. Here is an example of what that
raw data looked like:

![Raw Data](https://user-images.githubusercontent.com/71234992/94379654-ad020180-00e6-11eb-81b6-c4bc1416c4ef.PNG)

Subsequently, a python program was necessary in order to count through every vote. 
## Election-Audit Results
- How many votes were cast in this congressional election?

For this first step in the analysis the python code needed to count every vote, or every row except the header row, in 
the csv file. So, to complete this task the index function of the panda dataframe was used. Note that is saved a float 
for computational purposes later in the code.
```python
total_votes = float(len(df.index))
```

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Which county had the largest number of votes?
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?