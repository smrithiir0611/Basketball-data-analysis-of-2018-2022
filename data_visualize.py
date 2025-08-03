import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading of the dataset
df = pd.read_csv('teamstats.csv')

# 1. Team Win Counts (Bar Chart)
team_wins = df.groupby('team')['w'].sum().sort_values(ascending=False)
plt.figure(figsize=(12,6))
sns.barplot(x=team_wins.index, y=team_wins.values)
plt.title('Total Wins per Team')
plt.xticks(rotation=45)
plt.ylabel('Wins')
plt.xlabel('Team')
plt.tight_layout()
plt.savefig("team_wins.png")
plt.close()  

# 2. Points Distribution (Histogram)
plt.figure(figsize=(8,6))
sns.histplot(df['ppg'], bins=20, kde=True)
plt.title('Distribution of Points Scored')
plt.xlabel('Points')
plt.ylabel('Frequency')
plt.savefig("points_distribution.png")
plt.close()  

# 3. Points vs Assists (Scatter Plot)
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='ast', y='ppg', hue='team')
plt.title('Points vs Assists by Team')
plt.xlabel('Assists')
plt.ylabel('Points')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("points_vs_assists.png")
plt.close()  

# 5. Win Percentage Pie Chart
total_wins = team_wins.sum()
win_pct = (team_wins / total_wins) * 100
plt.figure(figsize=(8,8))
plt.pie(win_pct, labels=win_pct.index, autopct='%1.1f%%', startangle=140)
plt.title('Win Percentage per Team')
plt.savefig("Win_Percentage_Pie_Chart.png")
plt.close()  

# 6. Box Plot of Points per Team
plt.figure(figsize=(12,6))
sns.boxplot(x='team', y='ppg', data=df)
plt.title('Points Distribution per Team')
plt.xticks(rotation=45)
plt.savefig("Box_Plot_of_Points_per_team.png")
plt.close()  

