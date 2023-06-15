# Program name: Caeser Cipher
# Program description: Encodes and decodes based on the Caeser Cipher
# Author: Saran Wagner
# Date: December 17, 2022

# Asks user to type in message
message = input("type in a message")
shift = int(input("type in an integer"))

# Whitelist of characters
keep = set(' .,?!')
# List comprehension to check for spaces and shifts letters based on shift given
print("".join([c if c == ' ' else chr((ord(c)-ord('a')+shift)%26+ord('a')) for c in message]))
