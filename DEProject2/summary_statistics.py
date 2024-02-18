import pandas as pd

# Load the CSV file
csv_path = 'data/financial_data.csv'
df = pd.read_csv(csv_path)

# Display summary statistics
print("Summary Statistics:")
print(df.describe())
