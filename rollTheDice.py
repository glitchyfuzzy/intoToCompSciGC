# Program name: Roll the Dice
# Program description: Rolls dice based on given a given amount of sides and dice rolls
# Author: Saran Wagner
# Date: January 12 2023

# Imports randrange from random
from random import randrange

# Defines variables for the amount of sides, rolls, and the results
diceSides = int(input('Enter the amount of sides of the dice'))
diceRolls = int(input('Enter the amount of dice rolls'))
result = [[]]
resultCounter = 0

# For loop that makes lists
for i in range((diceSides * 2) -1):
    result.append([])

# Randomizes the numbers rolled to make results
for i in range(diceRolls):
    dice1 = randrange(1, diceSides + 1)
    dice2 = randrange(1, diceSides + 1)
    diceSum = dice1 + dice2
    result[diceSum - 2].append('#')

# Prints results
print("Frequences of sums for two ", diceSides, "-sided dice rolled ", diceRolls, " times", sep ='')
print("sum : count of the times occured")
while resultCounter < (diceSides * 2) - 1:
    print(resultCounter + 2, ":", end='')
    print(*result[resultCounter], sep='')
    resultCounter = resultCounter + 1








