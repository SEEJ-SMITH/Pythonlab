import numpy as np

# Step 1: Create 3x3 matrix (3 subjects × 3 students)
marks = np.array([
    [75, 80, 65],
    [88, 92, 70],
    [60, 78, 85]
])

print("Original 3x3 Marks Matrix:")
print(marks)

# Step 2: Convert into single row format
single_row = marks.reshape(1, 9)
print("\nConverted to Single Row Format:")
print(single_row)

# Step 3: Double the marks (bonus allocation)
bonus_marks = single_row * 2
print("\nBonus Allocated Marks (Doubled):")
print(bonus_marks)