# Program name: Conservation of Letters
# Program description: Takes every vowel out of a message except Y
# Author: Saran Wagner
# Date: December 17, 2022

# Asks user to type in a message
message = str(input("type in a message"))

# Takes vowels out of the message
print(message.translate({ord(vowel): None for vowel in 'aeiouAEIOU'}))