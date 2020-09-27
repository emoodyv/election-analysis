import pandas as pd

# Opening the file
df = pd.read_csv('election_results.csv')

# Analyzing the results
headers = df.columns.tolist()