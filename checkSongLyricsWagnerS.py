# Program name: Checks amount of words
# Program description: Program that checks amount of words in a given file
# Author: Saran Wagner
# Date: January 19 2023

# Sets number of words to 0
numberOfWords = 0
# Asks user to enter file name
fname = input("Enter a file name")

# Reads file
with open(fname, 'r') as file:

    data = file.read()
    lines = data.split()
    numberOfWords += len(lines)

# Prints result
print(fname, "has", numberOfWords, "amount of words.")

