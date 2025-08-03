import pandas as pd

# Loading of the dataset
df = pd.read_csv('teamstats.csv')

# To calculate total wins per team and sort descending
team_wins = df.groupby('team')['w'].sum().sort_values(ascending=False)

print("Total wins per team:")
print(team_wins)
