import pandas as pd
import numpy as np

# Opening the file
df = pd.read_csv('election_results.csv')
headers = df.columns.tolist()

# Getting the amount of votes
total_votes = float(len(df.index))

# Getting the candidates
canidate_options = []
for i in range(0, len(df.index)):
    if df[headers[2]][i] not in canidate_options:
        canidate_options.append(df[headers[2]][i])

# Getting the counties
county_options = []
for i in range(0, len(df.index)):
    if df[headers[1]][i] not in county_options:
        county_options.append(df[headers[1]][i])

# Getting the amount of votes per candidates
canidate_votes = {canidate_options[0]: 0, canidate_options[1]: 0, canidate_options[2]: 0}
for i in range(0, len(df.index)):
    if df[headers[2]][i] == canidate_options[0]:
        canidate_votes[canidate_options[0]] += 1
    elif df[headers[2]][i] == canidate_options[1]:
        canidate_votes[canidate_options[1]] += 1
    elif df[headers[2]][i] == canidate_options[2]:
        canidate_votes[canidate_options[2]] += 1

# Getting the amount of votes per county
county_votes = {county_options[0]: 0, county_options[1]: 0, county_options[2]: 0}
for i in range(0, len(df.index)):
    if df[headers[1]][i] == county_options[0]:
        county_votes[county_options[0]] += 1
    elif df[headers[1]][i] == county_options[1]:
        county_votes[county_options[1]] += 1
    elif df[headers[1]][i] == county_options[2]:
        county_votes[county_options[2]] += 1

# Getting the percentages
vote_percentage = [canidate_votes[canidate_options[0]] / total_votes * 100,
                   canidate_votes[canidate_options[1]] / total_votes * 100,
                   canidate_votes[canidate_options[2]] / total_votes * 100]

# Getting the county percentages
county_percentage = [county_votes[county_options[0]] / total_votes * 100,
                     county_votes[county_options[1]] / total_votes * 100,
                     county_votes[county_options[2]] / total_votes * 100]

# Winning Candidate and Winning Count Tracker
winner_index = np.int(np.where(vote_percentage == np.amax(vote_percentage))[0])
winning_candidate = canidate_options[winner_index]
winning_count = '{:,}'.format(canidate_votes[canidate_options[winner_index]])
winning_percentage = '{:.1f}'.format(vote_percentage[winner_index])

# Highest turnout county
highest_county_index = np.int(np.where(county_percentage == np.amax(county_percentage))[0])
highest_county_name = county_options[highest_county_index]
highest_county_count = '{:,}'.format(county_votes[county_options[highest_county_index]])
highest_county_percentage = '{:.1f}'.format(county_percentage[highest_county_index])

# Printing the results
print('Election Results\n-------------------------\nTotal Votes: ' + str('{:,}'.format(int(total_votes))) +
      '\n-------------------------\nCounty Votes:')

for i in range(0, len(headers)):
    print(county_options[i] + ': ' + str('{:.1f}'.format(county_percentage[i])) + '% (' +
          str('{:,}'.format(county_votes[county_options[i]])) + ')')

print('-------------------------\nLargest County Turnout: ' + highest_county_name + '\n-------------------------')

for i in range(0, len(headers)):
    print(canidate_options[i] + ': ' + str('{:.1f}'.format(vote_percentage[i])) + '% (' +
          str('{:,}'.format(canidate_votes[canidate_options[i]])) + ')')

print('-------------------------\nWinner: ' + winning_candidate + '\nWinning Vote Count: '
      + str(winning_count) + '\nWinning Percentage: ' + str(winning_percentage) +
      '%\n-------------------------\n')

# Recording the results
f = open('election_analysis.txt', 'w')
f.write('Election Results\n-------------------------\nTotal Votes: ' + str('{:,}'.format(int(total_votes))) +
        '\n-------------------------\nCounty Votes:\n')

for i in range(0, len(headers)):
    f.write(county_options[i] + ': ' + str('{:.1f}'.format(county_percentage[i])) + '% (' +
          str('{:,}'.format(county_votes[county_options[i]])) + ')\n')

f.write('-------------------------\nLargest County Turnout: ' + highest_county_name + '\n-------------------------\n')

for i in range(0, len(headers)):
    f.write(canidate_options[i] + ': ' + str('{:.1f}'.format(vote_percentage[i])) + '% ('
            + str('{:,}'.format(canidate_votes[canidate_options[i]])) + ')\n')

f.write('-------------------------\nWinner: ' + winning_candidate + '\nWinning Vote Count: ' + str(winning_count) +
        '\nWinning Percentage: ' + str(winning_percentage) + '%\n-------------------------\n')
f.close()