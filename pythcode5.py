import numpy as np

# Step 1: Coefficient matrix (for equations in a mechanical system)
A = np.array([
    [4, 3],
    [2, 1]
])

# Step 2: Compute determinant and inverse
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)

# Step 3: Round values for readability
inv_A_rounded = np.round(inv_A, 2)

print("Matrix A:\n", A)
print("Determinant of A:", det_A)
print("Inverse of A:\n", inv_A_rounded)