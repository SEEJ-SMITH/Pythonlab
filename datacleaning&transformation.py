import pandas as pd

# Load dataset
data = pd.read_csv("hr_dataset.csv")

# Display original data
print("Original Dataset:")
print(data.head())

# -------------------------------
# 1. Handling Missing Values
# -------------------------------

# Fill missing Salary with mean
if 'Salary' in data.columns:
    data['Salary'].fillna(data['Salary'].mean(), inplace=True)

# Fill missing Performance Score with median
if 'Score' in data.columns:
    data['Score'].fillna(data['Score'].median(), inplace=True)

# Drop rows where important fields are missing
data.dropna(subset=['Employee_ID'], inplace=True)

# -------------------------------
# 2. Remove Duplicate Records
# -------------------------------

data.drop_duplicates(inplace=True)

# -------------------------------
# 3. Data Transformation
# -------------------------------

# Convert Date column to datetime
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Convert Salary to numeric (in case it's string)
if 'Salary' in data.columns:
    data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce')

# Normalize Score (0–100 scale)
if 'Score' in data.columns:
    data['Score'] = (data['Score'] - data['Score'].min()) / (data['Score'].max() - data['Score'].min()) * 100

# -------------------------------
# Final Cleaned Data
# -------------------------------

print("\nCleaned Dataset:")
print(data.head())

# Save cleaned dataset
data.to_csv("cleaned_hr_dataset.csv", index=False)

print("\nData cleaning and transformation completed successfully!")