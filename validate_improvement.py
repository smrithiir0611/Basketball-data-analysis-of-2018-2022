import pandas as pd

# Here we are loading the dataset
df = pd.read_csv('teamstats.csv')

df_sorted = df.sort_values(['team', 'season'])

# To calculate year-over-year win improvement
df_sorted['win_diff'] = df_sorted.groupby('team')['w'].diff()

# To find out the average improvement per team
team_improvement = df_sorted.groupby('team')['win_diff'].mean().sort_values(ascending=False)

print("Top teams by average yearly improvement in wins:")
print(team_improvement.head(5))
