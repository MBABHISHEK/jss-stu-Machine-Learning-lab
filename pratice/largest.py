# user to input the tuple elements separated by spaces
tuple_data = tuple(map(int, input("Enter the tuple elements separated by spaces: ").split()))

# Initialize the largest_item variable with the first element of the tuple
largest_item = tuple_data[0]

# Iterate over the tuple elements
for item in tuple_data:
    # Check if the current item is larger than the largest_item
    if item > largest_item:
        # Update the largest_item if the current item is larger
        largest_item = item

print("Largest item in the tuple:", largest_item)
