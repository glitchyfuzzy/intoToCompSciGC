# Program name: Input numbers Output statistics
# Program description: Gives stats about given numbers
# Author: Saran Wagner
# Date: January 11 2023

# Function that finds all integers in the list
def stringToList(string):
    store = ""
    listOfNumbers = []
    for char in range(0, len(string)):
        if string[char] ==" ":
            string.replace(string[char] ,'')
        elif string[char] != ",":
            store += string[char]
        elif string[char] == ",":
            listOfNumbers.append(int(store))
            store = ""
    listOfNumbers.append(int(store))
    return listOfNumbers

# Sorts numbers in acsending order
def sortingListOfNumbers(listOfNumbers):
    listOfNumbers.sort()
    print(listOfNumbers)

# Finds maximum number
def maxNumberEntered(listOfNumbers):
    print("Max number is:", max(listOfNumbers))

# Finds minimum number
def minNumberEntered(listOfNumbers):
    print("Min number is:", min(listOfNumbers))

# Counts total amount of numbers
def countNumbersEntered(listOfNumbers):
    print("Total amount of numbers is:", len(listOfNumbers))

# Finds range of numbers
def rangeOfNumbers(listOfNumbers):
    minNum = min(listOfNumbers)
    maxNum = max(listOfNumbers)
    print("The range is:", maxNum-minNum)

# Finds average of numbers
def averageOfNumbers(listOfNumbers):
    average = sum(listOfNumbers) / len(listOfNumbers)
    print("The average is:", average)

# Asks user to input numbers and calls all other functions
def main():
    stringOfNumbers = input("Type in a list of numbers seperated by commas")
    listOfNumbers = stringToList(stringOfNumbers)
    sortingListOfNumbers(listOfNumbers)
    maxNumberEntered(listOfNumbers)
    minNumberEntered(listOfNumbers)
    countNumbersEntered(listOfNumbers)
    rangeOfNumbers(listOfNumbers)
    averageOfNumbers(listOfNumbers)

main()
