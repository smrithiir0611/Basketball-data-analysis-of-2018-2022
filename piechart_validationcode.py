import pandas as pd
import matplotlib.pyplot as plt

# Loading of the dataset
df = pd.read_csv('teamstats.csv')

# Calculating win percentage per team
team_wins = df.groupby('team')['w'].sum()
team_games = df.groupby('team')['gp'].sum()
win_pct = (team_wins / team_games).sort_values(ascending=False)

print("Win percentage per team:")
print(win_pct)

# Pie chart for visual validation
plt.figure(figsize=(8, 8))
win_pct.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Win Percentage Share by Team")
plt.ylabel("")
plt.tight_layout()
plt.show()
