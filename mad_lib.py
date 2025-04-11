#  Harry Potter Mad Lib Game
# A beginner-friendly fill-in-the-blanks game using input() and f-strings.

print(" Welcome to the Harry Potter Mad Lib Adventure ")
print("Just answer a few questions to complete your magical story...\n")
input("Press Enter to enter Hogwarts...")

# Gathering magical words from the user
wizard_name = input("Enter the name of a wizard or witch: ")
magical_creature = input("Name a magical creature: ")
spell = input("Your favorite spell: ")
place = input("A magical place (e.g. Hogwarts, Hogsmeade): ")
object_found = input("An object you might find in the Room of Requirement: ")

print("\nYour story is ready!")
input("Press Enter to reveal your magical tale...")

# Mad lib story using f-strings
story = f"""
Once upon a time, the legendary wizard {wizard_name} was walking through the halls of {place}.
Suddenly, a wild {magical_creature} appeared from the shadows!
Without hesitation, {wizard_name} shouted "{spell}!" and tamed the creature.
Hidden behind it was a mysterious {object_found}, glowing with enchantments.
From that day on, {wizard_name} became the true hero of {place}.
"""

print("\n Your Magical Story:\n")
print(story)
