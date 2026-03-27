import numpy as np

# Test Case 1: Calculate standard deviation of weekly rainfall data
rainfall = []

n = int(input("Enter number of days rainfall data: "))

for i in range(n):
    value = float(input("Enter rainfall value: "))
    rainfall.append(value)

rainfall_array = np.array(rainfall)
std_dev = np.std(rainfall_array)

print("Weekly Rainfall Data:", rainfall_array)
print("Standard Deviation of Rainfall:", std_dev)


# Test Case 2: Find mean and median of student exam scores
scores = []

m = int(input("Enter number of student scores: "))

for i in range(m):
    value = int(input("Enter score: "))
    scores.append(value)

scores_array = np.array(scores)
mean_value = np.mean(scores_array)
median_value = np.median(scores_array)

print("Student Scores:", scores_array)
print("Mean Score:", mean_value)
print("Median Score:", median_value)