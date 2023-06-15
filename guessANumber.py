# Program name: Guess a number
# Program description: Guessing game where user guesses random number between 1 and 100
# Author: Saran Wagner
# Date: December 10, 2022

# allows computer to get a random number
import random

# asks user to guess a number between 1 and 100
guess = int(input(print("Guess a number between 1 and 100!")))

# sets guessNum variable and string for guessList
guessNum = 1
guessList=[]
guessList.append(guess)

# checks if guess is higher or lower than number
num = random.randint(1, 100)
while guess != num:
    if guess > num:
        guess = int(input("Guess lower"))
        guessNum = guessNum + 1
    if guess < num:
        guess= int(input("Guess higher"))
        guessNum = guessNum + 1
    if guess not in guessList:
        guessList.append(guess)
    # tells answer if 10 guesses are used
    if guessNum > 9:
        print("Sorry, you used up all of your tries, the answer was", num)
        break

# tells user guess was correct if guessed correctly
if guess == num:
    print("Congratualtions, your guess was correct!")


