#  Basic Calculator (Addition and Subtraction Only)
#  Beginner friendly version — no conditions, no confusion.

# Take two whole numbers as input
num1 = int(input("Enter first number (integer only): "))
num2 = int(input("Enter second number (integer only): "))

# Show results of addition and subtraction
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")

# Tip:
# int() is used here, which means users should enter whole numbers only.
# If you want to allow decimals later, switch to float().
