# Program name: Barnyard Program
# Program description:
# Author: Saran Wagner
# Date: December 28, 2022

headNum = int(input("insert number of heads:"))
legNum = int(input("insert number of legs:"))

i = 0
j = 0
k = 0

for i in range(0, headNum):
    numCow = i
    for j in range(0, headNum - i):
        numChicken = j
        for k in range(0, headNum - i - j):
            numCrick = k
            k += 1
            if i + j + k == headNum:
                legSum = 4 * i + 2 * j + 6 * k
                if legSum == legNum:
                    print("Cows:", i, "Chickens:", j, "Crickets:", k)
        j += 1
    i += 1












