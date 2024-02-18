import pandas as pd

# Load the CSV file
csv_path = 'data/financial_data.csv'
df = pd.read_csv(csv_path)

# Display basic information
print("Basic Information:")
print(df.info())

# Display the first few rows
print("\nFirst Few Rows:")
print(df.head())
