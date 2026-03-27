import pandas as pd

# Load the CSV file
data = pd.read_csv("covid19_data.csv")

# Display first 5 records
print("First 5 Records:")
print(data.head())

# Display structure of dataset
print("\nDataset Information:")
print(data.info())

# Display important columns if available
print("\nSelected Data (Cases, Deaths, Recoveries):")
print(data[['Cases', 'Deaths', 'Recovered']].head())