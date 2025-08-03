import pandas as pd

# Load your dataset
df = pd.read_csv('teamstats.csv')

# Select key numeric columns to validate
cols_to_check = ['w', 'ppg', 'ast', 'gp', 'tov', 'pf', 'l']

# Generate summary stats (count, mean, std, min, 25%, 50%, 75%, max)
summary_stats = df[cols_to_check].describe()

print("Summary Statistics:\n", summary_stats)
