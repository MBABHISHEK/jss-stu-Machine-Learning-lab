import numpy as np

# Ask the user to input the array
arr = np.array(input("Enter the array elements separated by spaces: ").split(),dtype=int)

# Ask the user for the number of positions to left rotate
k = int(input("Enter the number of positions to left rotate: "))

# Perform left rotation using a loop
rotated_arr = np.empty_like(arr)
for i in range(len(arr)):
    rotated_arr[i] = arr[(i + k) % len(arr)]

print("Original array:", arr)
print("Left rotated array:", rotated_arr)
