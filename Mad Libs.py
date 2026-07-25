# ==========================
# Mad Libs Game in Python
# ==========================

print("===== WELCOME TO MAD LIBS GAME =====")

name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
color = input("Enter a color: ")
food = input("Enter a food: ")
verb = input("Enter a verb (action): ")
adjective = input("Enter an adjective: ")

print("\n===== YOUR FUNNY STORY =====\n")

story = f"""
One day, {name} went to {place}.
Suddenly, a {color} {animal} appeared.
The {animal} was very {adjective} and wanted to {verb}.
To make friends, {name} gave the {animal} some {food}.
They both laughed, became best friends, and had an amazing adventure together!
"""

print(story)