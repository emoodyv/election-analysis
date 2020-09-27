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

# Getting the amount of votes per candidates
canidate_votes = {canidate_options[0]: 0, canidate_options[1]: 0, canidate_options[2]: 0}
for i in range(0, len(df.index)):
    if df[headers[2]][i] == canidate_options[0]:
        canidate_votes[canidate_options[0]] += 1
    elif df[headers[2]][i] == canidate_options[1]:
        canidate_votes[canidate_options[1]] += 1
    elif df[headers[2]][i] == canidate_options[2]:
        canidate_votes[canidate_options[2]] += 1

# Getting the percentages
vote_percentage = []
vote_percentage.append(canidate_votes[canidate_options[0]] / total_votes * 100)
vote_percentage.append(canidate_votes[canidate_options[1]] / total_votes * 100)
vote_percentage.append(canidate_votes[canidate_options[2]] / total_votes * 100)

# Winning Candidate and Winning Count Tracker
winner_index = np.int(np.where(vote_percentage == np.amax(vote_percentage))[0])
winning_candidate = canidate_options[winner_index]
winning_count = canidate_votes[canidate_options[winner_index]]
winning_percentage = "{:.1f}".format(vote_percentage[winner_index])

# Printing the results
for i in range(0, 3):
    print(canidate_options[i] + ": " + str("{:.1f}".format(vote_percentage[i])) + "% (" +
          str(canidate_votes[canidate_options[i]]) + ")")

print('\n-------------------------\nWinner: ' + winning_candidate + '\nWinning Vote Count: '
      + str(winning_count) + '\nWinning Percentage: ' + str(winning_percentage) +
      '%\n-------------------------\n')