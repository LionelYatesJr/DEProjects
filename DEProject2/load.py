import pandas as pd

# Provide the path to your CSV file
csv_path = 'data/financial_data.csv'


# Load the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# Display basic information about the DataFrame
print(df.info())

# Display the first few rows of the DataFrame
print(df.head())
