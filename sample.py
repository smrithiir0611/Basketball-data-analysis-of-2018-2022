import pandas as pd

# Load the dataset
df = pd.read_csv('teamstats.csv')

# Print the first 7 rows as a markdown table
print(df.head(7).to_markdown())

# Print the dataset info summary
print("\nInfo:")
print(df.info())
