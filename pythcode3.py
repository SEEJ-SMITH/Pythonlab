import numpy as np

# Step 1: Create 1D array of 12 pixel values
pixels = np.array([10, 20, 30, 40, 50, 60,
                   70, 80, 90, 100, 110, 120])

print("Original 1D Pixel Data:")
print(pixels)

# Step 2: Reshape into 3 × 4 image matrix
image = pixels.reshape(3, 4)

print("\nReshaped Image Matrix (3x4):")
print(image)

# Step 3: Slice - Extract first 2 rows and first 2 columns
cropped = image[0:2, 0:2]

print("\nCropped Image (Top-Left 2x2 Part):")
print(cropped)