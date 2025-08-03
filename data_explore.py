import pandas as pd

# Loading of the dataset
df = pd.read_csv('teamstats.csv')

print("Dataset shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nFirst 5 rows:\n", df.head())

# Data types and null counts
print("\nInfo:")
print(df.info())

# Summary statistics for numeric columns
print("\nNumeric columns summary:")
print(df.describe())

# Value counts for categorical columns
print("\nCategorical columns summary:")
for col in df.select_dtypes(include='object').columns:
    print(f"\nColumn: {col}")
    print(df[col].value_counts().head(5))

