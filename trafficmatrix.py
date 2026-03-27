import numpy as np

traffic_matrix = np.array([[120, 80], [100, 60]])

print("Initial Traffic Matrix :")
print(traffic_matrix)

transformation_matrix = np.array([[0.9, 0.2],
                                  [0.1, 0.8]])

print("\nTransformation Matrix :")
print(transformation_matrix)

new_traffic = np.dot(transformation_matrix, traffic_matrix)

print("\nUpdated Traffic Matrix After Signal Optimization :")
print(new_traffic)

print("\nTotal traffic before optimization :")
print(np.sum(traffic_matrix))

print("Total traffic after optimization :")
print(np.sum(new_traffic))