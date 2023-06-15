# Program name: Letter Grade Predictor
# Program description: Predicts letter grade based on Guerin Catholic grading scale
# Author: Saran Wagner
# Date: December 8, 2022

# Asks user to input grade percentage
gradePercentage = float(input("What is your grade percentage?"))

# Makes function to round percentage
def roundNumber(gradeNum):
    return int(gradeNum + 0.5)

# Calls function to round percentage
numRounded = roundNumber(gradePercentage)

# Checks if the rounded percentage falls under grade and reports back to user
if numRounded >= 98:
    print("Your grade is an A+!")
elif numRounded >= 95:
    print("You're grade is an A!")
elif numRounded >= 92:
    print("You're grade is an A-!")
elif numRounded >= 89:
    print("You're grade is a B+!")
elif numRounded >= 86:
    print("Your grade is a B!")
elif numRounded >= 83:
    print("Your grade is a B-!")
elif numRounded >= 80:
    print("Your grade is a C+!")
elif numRounded >= 77:
    print("Your grade is a C!")
elif numRounded >= 74:
    print("Your grade is a C-!")
elif numRounded >= 64:
    print("Your grade is NCD!")
elif numRounded <= 64:
    print("Your grade is NCF!")
