# ------------------------------------------
# 3. Variables and Data Types
# ------------------------------------------
wizard_name = "Hermione Granger"  # String (text)
wizard_age = 17                   # Integer (whole number)
is_muggleborn = True              # Boolean (True or False)

# Display information using different methods
print("Wizard name: " + wizard_name)
print("Age: " + str(wizard_age))  # Convert int to string for printing

# Using f-strings for cleaner output
print(f"Muggle-born: {is_muggleborn}")

# ------------------------------------------
# 4. String Functions
# ------------------------------------------
spell = "Expelliarmus"

print(spell.upper())           # Shout the spell!
print(spell.lower())           # Whisper the spell
print(spell.isupper())         # Check if shouted
print(spell.upper().isupper()) # Convert then check
print(len(spell))              # Number of letters
print(spell[0])                # First letter
print(spell.index("a"))        # Find position of 'a'
print(spell.replace("Expelliarmus", "Lumos"))  # Change the spell

# ------------------------------------------
# 5. Working with Numbers
# ------------------------------------------

# Basic math in magic classes
print(7 + 3)       # Potions class: addition
print(5 * 5)       # Transfiguration magic multiplication
print(20 / 4)      # Division spell
print(2 + 3 * 4)   # Follow order of operations => 14

# Modulo spell: gives remainder
print(13 % 5)      # 13 divided by 5 leaves remainder 3

# Magical number functions
mana = -9
print(abs(mana))       # Absolute mana level
print(pow(7, 2))       # Power spell: 7 squared => 49
print(max(12, 21))     # Greater magic level
print(min(12, 21))     # Lesser magic level
print(round(9.8))      # Round up magic energy
print(round(2.2))      # Round down spell power
