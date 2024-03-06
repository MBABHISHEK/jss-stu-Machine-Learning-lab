# input the list elements separated by spaces
input_list = input("Enter the elements of the list separated by spaces: ").split()

# Convert each element of the list to integer (assuming integers are input)
input_list = [int(item) for item in input_list]

# Initialize an empty tuple
result_tuple = ()

# Iterate over the list elements and append them to the tuple
for item in input_list:
    result_tuple += (item,)

print("Tuple:", result_tuple)
