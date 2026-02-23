import numpy as np

# Step 1: Represent forces and displacements as matrices
forces = np.array([
    [2, 3, 5],   # Force components in X, Y, Z directions
    [4, 1, 2],   # Another force vector
])

displacement = np.array([
    [1, 0, 2],   # Displacement components in X, Y, Z
    [0, 3, 1],
    [2, 1, 0]
])

# Step 2: Transpose and dot product
forces_T = forces.T                 # Transpose: swap rows and columns
work_done = np.dot(forces, displacement)

print("Forces Matrix:", forces)
print("Displacement Matrix:", displacement)
print("Transpose of Forces:", forces_T)
print("Work Done (Dot Product):",work_done)