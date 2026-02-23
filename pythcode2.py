import numpy as np

# Rows = Areas
# Columns = Months
electricity = np.array([
    [1200, 1350, 1100],  # Area A
    [1500, 1600, 1550],  # Area B
    [1000, 1050, 980]    # Area C
])

print("Electricity Consumption Matrix:")
print(electricity)

# Average consumption per area
area_avg = np.mean(electricity, axis=1)
print("\nAverage Consumption Per Area:")
print(area_avg)

# Find maximum consumption value
max_value = np.max(electricity)
print("\nMaximum Consumption Recorded:")
print(max_value)