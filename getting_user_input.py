#  Welcome to the Wizarding Input Tutorial 🪄
# This program shows how to take input from the user using input()
# Input lets the user type something, and your program can use it!

print(" Welcome, young wizard! Let's get to know you.")

# Asking the user's name
wizard_name = input(" What is your wizarding name? ")
print(" Ah, the legendary wizard", wizard_name, "!")

# Asking the user's favorite spell
fav_spell = input(" What is your favorite spell? ")

# 📝 TIP: f-strings make it easy to insert variables into strings
# Just write: f"some text {variable} more text"
print(f" {fav_spell} is a powerful choice, {wizard_name}!")

# Asking for the user's age
# 📝 TIP: input() gives text, so convert to number using int()
age = input(" How old are you? (Just the number): ")
age = int(age)
print(f" In wizard years, that's {age * 7} years! Impressive!")

print(f" Thanks for visiting the Wizard Input Chamber, brave {wizard_name}!")
