# Program name: Count the Words
# Program description:
# Author: Saran Wagner
# Date: February 4 2023

fileName = input("Input file with extension")

try:
    with open(fileName, 'r') as f:
        f.close()
except:
    print("File does not exist")
    quit()

try:
    numberOfWords = int(input("How many top words to display: "))
except:
    print("Not a number")
    quit()

stopWords = ["the", "and", "if", "when", "how", "who", "what", "when", "where", "a", "I", "if", "it", "to"]
countOfWords = {}
with open(fileName, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if stopWords.count(word) == 0:
                if word not in countOfWords:
                    countOfWords[word] = 1
                else:
                    countOfWords[word] = countOfWords[word] + 1

file.close()

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




