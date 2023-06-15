# Program name: Roll the Dice
# Program description: Rolls dice based on given a given amount of sides and dice rolls
# Author: Saran Wagner
# Date: January 12 2023

# Imports libraries
from random import randrange
import matplotlib.pyplot as plt

# Defines variables for the amount of sides, rolls, and the results
diceSides = int(input('Enter the amount of sides of the dice'))
diceRolls = int(input('Enter the amount of dice rolls'))
result = []
resultCounter = 0

# Makes list for dice sides
for i in range((diceSides * 2) -1):
    result.append([0])

# Randomizes the numbers rolled to make results
for i in range(diceRolls):
    dice1 = randrange(1, diceSides + 1)
    dice2 = randrange(1, diceSides + 1)
    diceSum = dice1 + dice2
   # result[diceSum - 2].append("#")
    result[diceSum - 2] = [x + 1 for x in result[diceSum - 2]]

# Result variable
result = [x[0] for x in result]

# Makes graph
plt.title("Frequenceis of dice")
plt.xlabel("Roll")
plt.ylabel("Freuencey")
plt.bar(range(len(result)), result)
plt.show()









