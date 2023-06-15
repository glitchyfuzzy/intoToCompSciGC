# Program name: Bill, Tax, and Tip Adder
# Program description: Adds bill, tax and tip and outputs numbers
# Author: Saran Wagner
# Date: December 8, 2022

# Asks user to input bill
bill = float(input("What is your bill?"))

# Asks user to input tax and tip percentage
taxPercent = float(input("How much percentage of tax?"))
tipPercent = float(input("How much do you want to tip?"))

# Math to figure out tax and tip cost
tax = taxPercent * bill
tip = tipPercent * bill

# Prints bill, tax, tip, and total cost
print('Bill: $','{:5.2f}'.format(bill))
print('Tax: $','{:5.2f}'.format(tax))
print('Tip: $','{:5.2f}'.format(tip))
print("Total: $", sum([bill + tax + tip]))
