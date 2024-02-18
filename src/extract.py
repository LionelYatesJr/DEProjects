import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the CSV file
csv_path = '../data/USA_cars_datasets.csv'
df = pd.read_csv(csv_path)

# Data Exploration
print("Basic Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Data Transformation
# Example: Extract year and month from the 'year' column
df['year'] = pd.to_datetime(df['year'], format='%Y').dt.year
df['month'] = 1  # Assuming 1 for the month as 'date' was not present

# Example: Label encode 'state' column
label_encoder = LabelEncoder()
df['state_encoded'] = label_encoder.fit_transform(df['state'])

# Example: Drop unnecessary columns
columns_to_drop = ['Unnamed: 0', 'vin', 'lot']
df = df.drop(columns=columns_to_drop)

# Example: Handling missing values
# For simplicity, let's drop rows with missing values in this example
df_cleaned = df.dropna()

# Save the transformed DataFrame to a new CSV file
cleaned_csv_path = '../data/cleaned_data.csv'
df_cleaned.to_csv(cleaned_csv_path, index=False)

print("\nTransformed DataFrame:")
print(df_cleaned.head())

print(f"\nCleaned DataFrame saved to: {cleaned_csv_path}")
