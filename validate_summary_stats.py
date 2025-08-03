import pandas as pd

# Loading the dataset
df = pd.read_csv('teamstats.csv')

# To select key numeric columns to validate
cols_to_check = ['w', 'ppg', 'ast', 'gp', 'tov', 'pf', 'l']

# To generate summary stats (count, mean, std, min, 25%, 50%, 75%, max)
summary_stats = df[cols_to_check].describe()

print("Summary Statistics:\n", summary_stats)
