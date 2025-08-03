import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('teamstats.csv')

# Summary statistics for assists and points per game
print("Summary stats for assists (ast):")
print(df['ast'].describe())
print("\nSummary stats for points per game (ppg):")
print(df['ppg'].describe())

# Correlation between assists and points per game
correlation = df['ast'].corr(df['ppg'])
print(f"\nCorrelation between assists and points per game: {correlation:.3f}")

# Scatter plot for visual validation
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='ast', y='ppg', hue='team', palette='tab10')
plt.title('Assists vs Points per Game by Team')
plt.xlabel('Assists per Game')
plt.ylabel('Points per Game')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
