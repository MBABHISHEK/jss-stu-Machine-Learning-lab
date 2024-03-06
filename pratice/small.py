# input the tuple elements separated by spaces
tuple_data = tuple(map(int, input("Enter the tuple elements separated by spaces: ").split()))

# Initialize the smallest_item variable with the first element of the tuple
smallest_item = tuple_data[0]

# Iterate over the tuple elements
for item in tuple_data:
    # Check if the current item is smaller than the smallest_item
    if item < smallest_item:
        # Update the smallest_item if the current item is smaller
        smallest_item = item

print("Smallest item in the tuple:", smallest_item)
