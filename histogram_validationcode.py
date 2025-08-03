import pandas as pd

df = pd.read_csv('teamstats.csv')

print("Points per Game (ppg) Summary Statistics:")
print(df['ppg'].describe())
