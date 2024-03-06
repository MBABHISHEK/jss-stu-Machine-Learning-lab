# Ask the user to input the tuple elements separated by spaces
tuple_data = tuple(input("Enter the tuple elements separated by spaces: ").split())

# Initialize the count to 0
tuple_length = 0

# Iterate over the tuple elements and increment count for each element
for i in tuple_data:
    tuple_length += 1

print("Length of the tuple:", tuple_length)
