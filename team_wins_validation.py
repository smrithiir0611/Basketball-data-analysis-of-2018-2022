import pandas as pd

# Loading of the dataset
df = pd.read_csv('teamstats.csv')

# To calculate total wins per team
team_wins = df.groupby('team')['w'].sum().sort_values(ascending=False)
print(team_wins)
