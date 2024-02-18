import pandas as pd

# Load the transformed data
transformed_csv_path = '../data/transformed_data.csv'
df_transformed = pd.read_csv(transformed_csv_path)

# Additional loading steps if needed
# ...

# Display the loaded DataFrame
print("\nLoaded DataFrame:")
print(df_transformed.head())

# Your further processing or loading steps go here
# ...

# Example: Save the DataFrame to a MySQL database
# Make sure to replace 'your_database_name', 'your_username', and 'your_password' with your actual MySQL database credentials

from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:19328678Qw!@localhost/usa_car_dataset')
df_transformed.to_sql('car_data', con=engine, index=False, if_exists='replace')

print("\nData loaded to MySQL database.")
