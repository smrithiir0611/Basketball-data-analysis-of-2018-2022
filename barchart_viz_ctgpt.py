import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset (adjust the path to where your CSV file is)
df = pd.read_csv("teamstats.csv")  # Make sure the file is in the same directory or provide full path

# Group and sort total wins per team
total_wins = df.groupby('team')['w'].sum().sort_values(ascending=False)

# Plot the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=total_wins.values, y=total_wins.index, palette='Blues_d')
plt.title("Total Wins per Team (2018–2022)")
plt.xlabel("Total Wins")
plt.ylabel("Team")
plt.tight_layout()
plt.show()
