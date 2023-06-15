# Program name: Count the Words
# Program description:
# Author: Saran Wagner
# Date: February 4 2023

# Asks user to input file
fileName = input("Input file with extension")

# Checks to see if file exists
try:
    with open(fileName, 'r') as f:
        f.close()
except:
    print("File does not exist")
    quit()

# Asks user to input number and checks to see if it's an integer
try:
    numberOfWords = int(input("How many top words to display: "))
except:
    print("Not a valid number")
    quit()

# Word blacklist
stopWords = ["the", "and", "if", "when", "how", "who", "what", "when", "where", "a", "I", "if", "it", "to", "in"]
# Dictionary to keep amount of words
countOfWords = {}

# Opens file and adds words to dictionary
with open(fileName, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if stopWords.count(word) == 0:
                if word not in countOfWords:
                    countOfWords[word] = 1
                else:
                    countOfWords[word] = countOfWords[word] + 1

# Closes file
file.close()

# Checks for highest word counts
highestWordCount = 0
highestWord = ""
for num in range(0, numberOfWords):
    for key, value in countOfWords.items():
        if value > highestWordCount:
            highestWord = key
            highestWordCount = value
    print(highestWord, ":", highestWordCount)
    countOfWords[highestWord] = -1
    highestWordCount = 0




