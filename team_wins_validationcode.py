import pandas as pd

# Load dataset
df = pd.read_csv('teamstats.csv')

# Calculate total wins per team and sort descending
team_wins = df.groupby('team')['w'].sum().sort_values(ascending=False)

print("Total wins per team:")
print(team_wins)
