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
for computational purposes later in the code. Here is what that code looked like:
```python
total_votes = float(len(df.index))
```

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

In order to obtain county specific results the program first had to sort through the data to find the counties where the
votes came from. Since the county data was in the second column of the raw data, a loop was created to go through all of
the data in the second column. If a new county was discovered it was added to a list. This is the code that was tasked 
to that:
```python
county_options = []
for i in range(0, len(df.index)):
    if df[headers[1]][i] not in county_options:
        county_options.append(df[headers[1]][i])
```
What was returned from that loop was the following array:
```python
['Jefferson', 'Denver', 'Arapahoe']
```
From there a dictionary was created to store the votes for each county. Then the program looped through every row in the
data associated each vote to a county:
```python
county_votes = {county_options[0]: 0, county_options[1]: 0, county_options[2]: 0}
for i in range(0, len(df.index)):
    if df[headers[1]][i] == county_options[0]:
        county_votes[county_options[0]] += 1
    elif df[headers[1]][i] == county_options[1]:
        county_votes[county_options[1]] += 1
    elif df[headers[1]][i] == county_options[2]:
        county_votes[county_options[2]] += 1
```
The resulting dictionary was:
```python
{'Jefferson': 38855, 'Denver': 306055, 'Arapahoe': 24801}
```
After that the percentage of the vote that each county accounted for was simply calculated by dividing the votes that 
where in each county by the total. Here is the code and resulting array:
```python
county_percentage = [county_votes[county_options[0]] / total_votes * 100,
                     county_votes[county_options[1]] / total_votes * 100,
                     county_votes[county_options[2]] / total_votes * 100]
```
```python
[10.509560169970598, 82.78222719908253, 6.708212630946875]
```
After all that code the program was able to come to the conclusion that Jefferson County received 10.5% of the vote with 
38,855 votes, Denver County had 306,055 votes (82.8%), and Arapahoe County had 24,801 votes (6.7%).

- Which county had the largest number of votes?

In order to determine which county had the highest amount of votes several NumPy functions were utilized. These found 
the index of the largest value in the county_percentage array. With that index the program was able to find the name, 
amount of votes, and percentage of the vote of the county that had the largest amount of votes. This is the code:
```python
highest_county_index = np.int(np.where(county_percentage == np.amax(county_percentage))[0])
highest_county_name = county_options[highest_county_index]
highest_county_count = '{:,}'.format(county_votes[county_options[highest_county_index]])
highest_county_percentage = '{:.1f}'.format(county_percentage[highest_county_index])
```
What was found was that Denver County had the most votes with 306,055 of them. That was 82.8% of the vote.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

The process of acquiring the amount of votes and the percentage of the vote per candidate was very similar to the 
process explained above 

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?