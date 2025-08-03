import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading of the dataset
df = pd.read_csv('teamstats.csv')

# Summary statistics for points per game grouped by team
print("Points per game summary by team:")
print(df.groupby('team')['ppg'].describe())

# Box plot for perfroming visual validation
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='team', y='ppg', palette='Set2')
plt.title("Box Plot of Points per Game by Team")
plt.xlabel("Team")
plt.ylabel("Points per Game")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
