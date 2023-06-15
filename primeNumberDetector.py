# Program name: Prime number detector
# Program description: Detects if a number is prime or not
# Author: Saran Wagner
# Date: December 10, 2022

# Tells user to insert non-negative integer
integer = int(input("enter a non-negative integer:"))

# Checks if integer is divisable by any integer and prints result
if integer > 1:
    for i in range(2,int(integer/2)+1):
        if (integer % i) == 0:
            print("Number:", integer, "IS NOT PRIME")
            break
    else:
        print("Number:", integer, "IS PRIME")
else:
    print("Number:", integer, "IS NOT PRIME")
