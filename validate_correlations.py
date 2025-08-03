import pandas as pd

# Loading of the dataset
df = pd.read_csv('teamstats.csv')

# Here we are including all relevant numeric columns for correlation
numeric_cols = ['gp', 'w', 'l', 'tov', 'stl', 'blk', 'pf', 'pfd', 'ppg', 'ast', 'win_percent', 'fg_percent']

# To calculate correlation matrix
corr_matrix = df[numeric_cols].corr()

# To print correlations with wins and win percentage
print("Correlation of stats with wins (w):")
print(corr_matrix['w'].sort_values(ascending=False))
print("\nCorrelation of stats with win_percent:")
print(corr_matrix['win_percent'].sort_values(ascending=False))
