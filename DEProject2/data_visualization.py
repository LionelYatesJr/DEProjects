import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
csv_path = 'data/financial_data.csv'
df = pd.read_csv(csv_path)

# Visualize data using seaborn or matplotlib
# Example: Pairplot for numerical columns
sns.pairplot(df)
plt.show()
