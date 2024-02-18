import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the cleaned data
cleaned_csv_path = '../data/cleaned_data.csv'
df_cleaned = pd.read_csv(cleaned_csv_path)

# Additional transformations
# Add your specific transformations here

# Save the transformed DataFrame to a new CSV file
transformed_csv_path = '../data/transformed_data.csv'
df_cleaned.to_csv(transformed_csv_path, index=False)

print("\nTransformed DataFrame:")
print(df_cleaned.head())

print(f"\nTransformed DataFrame saved to: {transformed_csv_path}")
