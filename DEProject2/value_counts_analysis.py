import pandas as pd

# Load the CSV file
csv_path = 'data/financial_data.csv'
df = pd.read_csv(csv_path)

# Display value counts for a specific column
column_of_interest = 'Sentiment'
print(f"Value Counts for {column_of_interest}:")
print(df[column_of_interest].value_counts())
