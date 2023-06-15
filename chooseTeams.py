# Program name: Team Chooser
# Program description: Has 2 users choose names based on given list of names.
# Author: Saran Wagner
# Date: January 9 2023

# Defines the list of names and team lists
name = ["Bob", "Billy", "Rob", "Robby", "Saran", "Jim", "Sarah", "John", "Jane", "Mike"]
user1Team = []
user2Team = []

# Prints all avalible names
print(name)

# Functions that tells user to choose people
def user1():
    user1choice = input("User 1, choose a member of your team")
    name.remove(user1choice)
    user1Team.append(user1choice)
    print(name)
def user2 ():
    user2choice = input("User 2, choose a member of your team")
    name.remove(user2choice)
    user2Team.append(user2choice)
    print(name)

# Functions being called 5 times each
def main():
    user1()
    user2()
    user1()
    user2()
    user1()
    user2()
    user1()
    user2()
    user1()
    user1()

# Prints final team lists
print("User 1's team:", user1Team)
print("User 2's team:", user2Team)
