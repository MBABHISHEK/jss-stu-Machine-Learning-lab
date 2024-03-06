# Ask the user to input a string
input_string = input("Enter a string: ")

# Split the string into words
words = input_string.split()

# Initialize an empty dictionary to store word counts
word_counts = {}

# Count the occurrences of each word
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Print the word counts
print("Word counts:")
for word, count in word_counts.items():
    print(word, ":", count)
