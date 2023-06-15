# Program name:
# Program description:
# Author: Saran Wagner
# Date: January 20 2023

# Imports library
import csv
import matplotlib.pyplot as plt

# Reads csv fil
with open('Lottery_Powerball_Winning_Numbers__Beginning_2010.csv', 'r') as readObj:
    heading = next(readObj)
    csvReader = csv.reader(readObj)
    listOfCSV = list(csvReader)

# List of values
date_list = []
numbers_list = []
multiplier_list = []

# Adds numbers to list
for row in listOfCSV:
    date_list.append(row[0])
    numbers_list.append(row[1].split())
    multiplier_list.append(row[2])

# Makes number and powerball list dictionary
numberListDictonary = {}
powerballListDictionary = {}
for small_list in numbers_list:
    for number in range(len(small_list)):
        if small_list[number] not in numberListDictonary:
            numberListDictonary[small_list[number]] = 1
        else:
            numberListDictonary[small_list[number]] += 1
        if number == len(small_list) - 1:
            print(number)
            if small_list[number] not in powerballListDictionary:
                powerballListDictionary[small_list[number]] = 1
            else:
                powerballListDictionary[small_list[number]] += 1


# Makes amount of x and y coordiantes of number list dictionary
numbers_key_list = numberListDictonary.keys()
numbers_value_list = numberListDictonary.values()

# Makes amount of x and y cooridinates of powerball list dictonary
powerball_key_list = powerballListDictionary.keys()
powerball_value_list = powerballListDictionary.values()

# Makes all number graph
plt.title("Frequency of all numbers")
plt.xlabel("Numbers")
plt.ylabel("Amount of numbers")
plt.bar(numbers_key_list, numbers_value_list)
plt.show()

# Makes powerball number graph
plt.title("Frequency of powerball numbers")
plt.xlabel("Numbers")
plt.ylabel("Amount of numbers")
plt.bar(powerball_key_list, powerball_value_list)
plt.show()





